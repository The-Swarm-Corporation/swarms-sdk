"""
Swarms API Client

A production-grade Python client for the Swarms API with both synchronous and asynchronous interfaces.
"""

import asyncio
import os
import json
import time
from typing import Dict, List, Optional, Union, Any, Literal, Type, TypeVar, cast
from urllib.parse import urljoin

import aiohttp
import requests
from dotenv import load_dotenv
from pydantic import BaseModel, field_validator, ConfigDict
from pydantic.v1 import root_validator
from loguru import logger

# Check if tqdm is installed for progress tracking
try:
    from tqdm.auto import tqdm
    TQDM_INSTALLED = True
except ImportError:
    TQDM_INSTALLED = False

# ===== Type definitions =====
T = TypeVar('T')
ModelNameType = str
AgentNameType = str
SwarmTypeType = Literal[
    "AgentRearrange",
    "MixtureOfAgents",
    "SpreadSheetSwarm",
    "SequentialWorkflow",
    "ConcurrentWorkflow",
    "GroupChat",
    "MultiAgentRouter",
    "AutoSwarmBuilder",
    "HiearchicalSwarm",
    "auto",
    "MajorityVoting",
    "MALT",
    "DeepResearchSwarm",
]

# ===== Models =====

class SwarmsObject(BaseModel):
    """Base class for Swarms API objects"""
    model_config = ConfigDict(
        extra='allow',
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

class AgentTool(SwarmsObject):
    """Tool configuration for an agent"""
    type: str
    function: Dict[str, Any]

class AgentSpec(SwarmsObject):
    """Configuration for an agent"""
    agent_name: str
    description: Optional[str] = None
    system_prompt: Optional[str] = None
    model_name: ModelNameType = "gpt-4o-mini"
    auto_generate_prompt: bool = False
    max_tokens: int = 8192
    temperature: float = 0.5
    role: str = "worker"
    max_loops: int = 1
    tools_dictionary: Optional[List[Dict[str, Any]]] = None

    @field_validator('temperature')
    def validate_temperature(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Temperature must be between 0 and 1")
        return v

class AgentCompletion(SwarmsObject):
    """Agent completion request"""
    agent_config: AgentSpec
    task: str
    history: Optional[Dict[str, Any]] = None

class ScheduleSpec(SwarmsObject):
    """Schedule specification for swarm execution"""
    scheduled_time: str  # ISO formatted datetime
    timezone: str = "UTC"

class SwarmSpec(SwarmsObject):
    """Configuration for a swarm"""
    name: Optional[str] = None
    description: Optional[str] = None
    agents: Optional[List[AgentSpec]] = None
    max_loops: int = 1
    swarm_type: Optional[SwarmTypeType] = None
    rearrange_flow: Optional[str] = None
    task: Optional[str] = None
    img: Optional[str] = None
    return_history: bool = True
    rules: Optional[str] = None
    schedule: Optional[ScheduleSpec] = None
    tasks: Optional[List[str]] = None
    messages: Optional[List[Dict[str, Any]]] = None
    stream: bool = False
    service_tier: str = "standard"

    @root_validator
    def validate_task_or_tasks(cls, values):
        if not any([values.get('task'), values.get('tasks'), values.get('messages')]):
            raise ValueError("Either task, tasks, or messages must be provided")
        return values

# ===== API Response Models =====

class Usage(SwarmsObject):
    """Token usage information"""
    input_tokens: int
    output_tokens: int
    total_tokens: int

class AgentCompletionResponse(SwarmsObject):
    """Response from an agent completion request"""
    id: str
    success: bool
    name: str
    description: Optional[str] = None
    temperature: float
    outputs: Dict[str, Any]
    usage: Usage
    timestamp: str

class SwarmCompletionResponse(SwarmsObject):
    """Response from a swarm completion request"""
    job_id: str
    status: str
    swarm_name: Optional[str] = None
    description: Optional[str] = None
    swarm_type: Optional[SwarmTypeType] = None
    output: Dict[str, Any]
    number_of_agents: int
    service_tier: str
    tasks: Optional[List[str]] = None
    messages: Optional[List[Dict[str, Any]]] = None

class LogEntry(SwarmsObject):
    """API request log entry"""
    id: Optional[str] = None
    api_key: str
    data: Dict[str, Any]
    created_at: Optional[str] = None

class LogsResponse(SwarmsObject):
    """Response from a logs request"""
    status: str
    count: int
    logs: List[LogEntry]
    timestamp: str

class SwarmTypesResponse(SwarmsObject):
    """Response from a swarm types request"""
    success: bool
    swarm_types: List[SwarmTypeType]

class ModelsResponse(SwarmsObject):
    """Response from a models request"""
    success: bool
    models: List[str]

# ===== Exceptions =====

class SwarmsError(Exception):
    """Base exception for all Swarms API errors"""
    def __init__(self, message=None, http_status=None, request_id=None, body=None):
        self.message = message
        self.http_status = http_status
        self.request_id = request_id
        self.body = body
        super().__init__(self.message)

    def __str__(self):
        msg = self.message or "Unknown error"
        if self.http_status:
            msg = f"[{self.http_status}] {msg}"
        if self.request_id:
            msg = f"{msg} (Request ID: {self.request_id})"
        return msg

class AuthenticationError(SwarmsError):
    """Raised when there's an issue with authentication"""
    pass

class RateLimitError(SwarmsError):
    """Raised when the rate limit is exceeded"""
    pass

class APIError(SwarmsError):
    """Raised when the API returns an error"""
    pass

class InvalidRequestError(SwarmsError):
    """Raised when the request is invalid"""
    pass

class InsufficientCreditsError(SwarmsError):
    """Raised when the user doesn't have enough credits"""
    pass

class TimeoutError(SwarmsError):
    """Raised when a request times out"""
    pass

class NetworkError(SwarmsError):
    """Raised when there's a network issue"""
    pass

# ===== Utilities =====

def _handle_error_response(response, body):
    """Process an error response and raise the appropriate exception"""
    request_id = response.headers.get("x-request-id")
    
    if response.status_code == 401 or response.status_code == 403:
        raise AuthenticationError(
            message=body.get("detail", "Authentication error"),
            http_status=response.status_code,
            request_id=request_id,
            body=body
        )
    elif response.status_code == 429:
        raise RateLimitError(
            message=body.get("detail", "Rate limit exceeded"),
            http_status=response.status_code,
            request_id=request_id,
            body=body
        )
    elif response.status_code == 400:
        raise InvalidRequestError(
            message=body.get("detail", "Invalid request"),
            http_status=response.status_code,
            request_id=request_id,
            body=body
        )
    elif response.status_code == 402:
        raise InsufficientCreditsError(
            message=body.get("detail", "Insufficient credits"),
            http_status=response.status_code,
            request_id=request_id,
            body=body
        )
    else:
        raise APIError(
            message=body.get("detail", f"API error: {response.status_code}"),
            http_status=response.status_code,
            request_id=request_id,
            body=body
        )

async def _handle_async_error_response(response, body):
    """Process an error response asynchronously and raise the appropriate exception"""
    request_id = response.headers.get("x-request-id")
    
    if response.status == 401 or response.status == 403:
        raise AuthenticationError(
            message=body.get("detail", "Authentication error"),
            http_status=response.status,
            request_id=request_id,
            body=body
        )
    elif response.status == 429:
        raise RateLimitError(
            message=body.get("detail", "Rate limit exceeded"),
            http_status=response.status,
            request_id=request_id,
            body=body
        )
    elif response.status == 400:
        raise InvalidRequestError(
            message=body.get("detail", "Invalid request"),
            http_status=response.status,
            request_id=request_id,
            body=body
        )
    elif response.status == 402:
        raise InsufficientCreditsError(
            message=body.get("detail", "Insufficient credits"),
            http_status=response.status,
            request_id=request_id,
            body=body
        )
    else:
        raise APIError(
            message=body.get("detail", f"API error: {response.status}"),
            http_status=response.status,
            request_id=request_id,
            body=body
        )

def _parse_response(response_class: Type[T], data: Dict[str, Any]) -> T:
    """Parse API response into the appropriate model"""
    try:
        return response_class.model_validate(data)
    except Exception as e:
        logger.error(f"Error parsing response: {e}")
        # Return raw data if parsing fails
        return cast(T, data)

# ===== Swarms API Client =====

class Swarms:
    """
    Client for the Swarms API with both synchronous and asynchronous interfaces.
    
    Example usage:
        ```python
        from swarms import Swarms
        
        # Initialize the client
        client = Swarms(api_key="your-api-key")
        
        # Make a swarm completion request
        response = client.swarm.create(
            name="My Swarm",
            swarm_type="auto",
            task="Analyze the pros and cons of quantum computing",
            agents=[
                {
                    "agent_name": "Researcher",
                    "description": "Conducts in-depth research",
                    "model_name": "gpt-4o"
                },
                {
                    "agent_name": "Critic",
                    "description": "Evaluates arguments for flaws",
                    "model_name": "gpt-4o-mini"
                }
            ]
        )
        
        # Print the output
        print(response.output)
        ```
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = os.getenv("SWARMS_API_KEY"), 
        base_url: Optional[str] = "https://swarms-api-285321057562.us-east1.run.app",
        timeout: int = 60,
        max_retries: int = 3,
        retry_delay: int = 1,
        log_level: str = "INFO"
    ):
        """
        Initialize the Swarms API client.
        
        Args:
            api_key: API key for authentication. If not provided, it will be loaded from 
                    the SWARMS_API_KEY environment variable.
            base_url: Base URL for the API. If not provided, it will be loaded from 
                     the SWARMS_API_BASE_URL environment variable or default to the production URL.
            timeout: Timeout for API requests in seconds.
            max_retries: Maximum number of retry attempts for failed requests.
            retry_delay: Initial delay between retries in seconds (uses exponential backoff).
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        """
        # Load environment variables
        load_dotenv()
        
        # Set API key
        self.api_key = api_key or os.getenv("SWARMS_API_KEY")
        if not self.api_key:
            logger.warning("No API key provided. Please set the SWARMS_API_KEY environment variable or pass it explicitly.")
        
        # Set base URL
        self.base_url = base_url or os.getenv("SWARMS_API_BASE_URL", "https://swarms-api-285321057562.us-east1.run.app")
        
        # Ensure base_url ends with a slash
        if not self.base_url.endswith('/'):
            self.base_url += '/'
        
        # Set other parameters
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
        # Set up logging
        logger.remove()  # Remove default handler
        logger.add(
            lambda msg: print(msg, end=""),
            colorize=True,
            level=log_level,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
        )
        
        # Create aiohttp session
        self._session = None
        
        # Initialize API resources
        self.agent = AgentResource(self)
        self.swarm = SwarmResource(self)
        self.models = ModelsResource(self)
        self.logs = LogsResource(self)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()
            self._session = None
    
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        retries_left: Optional[int] = None
    ):
        """
        Make a synchronous HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (relative to base_url)
            params: Query parameters
            data: Request body data
            headers: Additional headers
            retries_left: Number of retries left
        
        Returns:
            Response data as a dictionary
        """
        url = urljoin(self.base_url, endpoint)
        
        if retries_left is None:
            retries_left = self.max_retries
        
        # Set up headers
        request_headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }
        if headers:
            request_headers.update(headers)
        
        try:
            logger.debug(f"{method} {url}")
            if data:
                logger.debug(f"Request data: {json.dumps(data, indent=2)}")
            
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=data,
                headers=request_headers,
                timeout=self.timeout
            )
            
            # Try to parse JSON response
            try:
                body = response.json()
            except ValueError:
                body = {"detail": response.text}
            
            # Handle error responses
            if not response.ok:
                _handle_error_response(response, body)
            
            logger.debug(f"Response: {json.dumps(body, indent=2) if isinstance(body, dict) else body}")
            return body
        
        except (requests.Timeout, requests.ConnectionError) as e:
            # Retry on network errors with exponential backoff
            if retries_left > 0:
                delay = self.retry_delay * (2 ** (self.max_retries - retries_left))
                logger.warning(f"Request failed: {str(e)}. Retrying in {delay} seconds...")
                time.sleep(delay)
                return self._make_request(method, endpoint, params, data, headers, retries_left - 1)
            
            if isinstance(e, requests.Timeout):
                raise TimeoutError(
                    message=f"Request timed out after {self.timeout} seconds",
                    http_status=None
                ) from e
            else:
                raise NetworkError(
                    message=f"Network error: {str(e)}",
                    http_status=None
                ) from e
        
        except SwarmsError:
            # Re-raise Swarms errors
            raise
        
        except Exception as e:
            # Catch-all for unexpected errors
            logger.error(f"Unexpected error: {str(e)}")
            raise APIError(
                message=f"Unexpected error: {str(e)}",
                http_status=None
            ) from e
    
    async def _make_async_request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
        retries_left: Optional[int] = None
    ):
        """
        Make an asynchronous HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint (relative to base_url)
            params: Query parameters
            data: Request body data
            headers: Additional headers
            retries_left: Number of retries left
        
        Returns:
            Response data as a dictionary
        """
        url = urljoin(self.base_url, endpoint)
        
        if retries_left is None:
            retries_left = self.max_retries
        
        # Set up headers
        request_headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key
        }
        if headers:
            request_headers.update(headers)
        
        # Create session if not already created
        if self._session is None:
            self._session = aiohttp.ClientSession()
        
        try:
            logger.debug(f"{method} {url}")
            if data:
                logger.debug(f"Request data: {json.dumps(data, indent=2)}")
            
            async with self._session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                headers=request_headers,
                timeout=self.timeout
            ) as response:
                # Try to parse JSON response
                try:
                    body = await response.json()
                except ValueError:
                    body = {"detail": await response.text()}
                
                # Handle error responses
                if response.status >= 400:
                    await _handle_async_error_response(response, body)
                
                logger.debug(f"Response: {json.dumps(body, indent=2) if isinstance(body, dict) else body}")
                return body
        
        except aiohttp.ClientError as e:
            # Retry on network errors with exponential backoff
            if retries_left > 0:
                delay = self.retry_delay * (2 ** (self.max_retries - retries_left))
                logger.warning(f"Request failed: {str(e)}. Retrying in {delay} seconds...")
                await asyncio.sleep(delay)
                return await self._make_async_request(method, endpoint, params, data, headers, retries_left - 1)
            
            if isinstance(e, asyncio.TimeoutError):
                raise TimeoutError(
                    message=f"Request timed out after {self.timeout} seconds",
                    http_status=None
                ) from e
            else:
                raise NetworkError(
                    message=f"Network error: {str(e)}",
                    http_status=None
                ) from e
        
        except SwarmsError:
            # Re-raise Swarms errors
            raise
        
        except Exception as e:
            # Catch-all for unexpected errors
            logger.error(f"Unexpected error: {str(e)}")
            raise APIError(
                message=f"Unexpected error: {str(e)}",
                http_status=None
            ) from e

# ===== API Resources =====

class BaseResource:
    """Base class for API resources"""
    def __init__(self, client):
        self.client = client

class AgentResource(BaseResource):
    """API resource for agent operations"""
    
    def create(self, **kwargs) -> AgentCompletionResponse:
        """
        Create an agent completion.
        
        Args:
            agent_config: Configuration for the agent
            task: The task to complete
            history: Optional conversation history
            
        Returns:
            AgentCompletionResponse
            
        Example:
            ```python
            response = client.agent.create(
                agent_config={
                    "agent_name": "Researcher",
                    "description": "Conducts in-depth research",
                    "model_name": "gpt-4o"
                },
                task="Research the impact of quantum computing on cryptography"
            )
            ```
        """
        # Convert agent_config dict to AgentSpec if needed
        if isinstance(kwargs.get('agent_config'), dict):
            kwargs['agent_config'] = AgentSpec(**kwargs['agent_config'])
        
        # Create and validate request
        request = AgentCompletion(**kwargs)
        
        # Make API request
        data = self.client._make_request('POST', 'v1/agent/completions', data=request.model_dump())
        return _parse_response(AgentCompletionResponse, data)
    
    def create_batch(self, completions: List[Union[Dict, AgentCompletion]]) -> List[AgentCompletionResponse]:
        """
        Create multiple agent completions in batch.
        
        Args:
            completions: List of agent completion requests
            
        Returns:
            List of AgentCompletionResponse
            
        Example:
            ```python
            responses = client.agent.create_batch([
                {
                    "agent_config": {
                        "agent_name": "Researcher",
                        "model_name": "gpt-4o-mini"
                    },
                    "task": "Summarize the latest quantum computing research"
                },
                {
                    "agent_config": {
                        "agent_name": "Writer",
                        "model_name": "gpt-4o"
                    },
                    "task": "Write a blog post about AI safety"
                }
            ])
            ```
        """
        # Convert each completion to AgentCompletion if it's a dict
        request_data = []
        for completion in completions:
            if isinstance(completion, dict):
                # Convert agent_config dict to AgentSpec if needed
                if isinstance(completion.get('agent_config'), dict):
                    completion['agent_config'] = AgentSpec(**completion['agent_config'])
                request_data.append(AgentCompletion(**completion).model_dump())
            else:
                request_data.append(completion.model_dump())
        
        # Make API request
        data = self.client._make_request('POST', 'v1/agent/batch/completions', data=request_data)
        
        # Parse responses
        return [_parse_response(AgentCompletionResponse, item) for item in data]
    
    async def acreate(self, **kwargs) -> AgentCompletionResponse:
        """
        Create an agent completion asynchronously.
        
        Args:
            agent_config: Configuration for the agent
            task: The task to complete
            history: Optional conversation history
            
        Returns:
            AgentCompletionResponse
        """
        # Convert agent_config dict to AgentSpec if needed
        if isinstance(kwargs.get('agent_config'), dict):
            kwargs['agent_config'] = AgentSpec(**kwargs['agent_config'])
        
        # Create and validate request
        request = AgentCompletion(**kwargs)
        
        # Make API request
        data = await self.client._make_async_request('POST', 'v1/agent/completions', data=request.model_dump())
        return _parse_response(AgentCompletionResponse, data)
    
    async def acreate_batch(self, completions: List[Union[Dict, AgentCompletion]]) -> List[AgentCompletionResponse]:
        """
        Create multiple agent completions in batch asynchronously.
        
        Args:
            completions: List of agent completion requests
            
        Returns:
            List of AgentCompletionResponse
        """
        # Convert each completion to AgentCompletion if it's a dict
        request_data = []
        for completion in completions:
            if isinstance(completion, dict):
                # Convert agent_config dict to AgentSpec if needed
                if isinstance(completion.get('agent_config'), dict):
                    completion['agent_config'] = AgentSpec(**completion['agent_config'])
                request_data.append(AgentCompletion(**completion).model_dump())
            else:
                request_data.append(completion.model_dump())
        
        # Make API request
        data = await self.client._make_async_request('POST', 'v1/agent/batch/completions', data=request_data)
        
        # Parse responses
        return [_parse_response(AgentCompletionResponse, item) for item in data]

class SwarmResource(BaseResource):
    """API resource for swarm operations"""
    
    def create(self, **kwargs) -> SwarmCompletionResponse:
        """
        Create a swarm completion.
        
        Args:
            name: Name of the swarm
            description: Description of the swarm
            agents: List of agent specifications
            max_loops: Maximum number of loops
            swarm_type: Type of swarm
            task: The task to complete
            tasks: List of tasks for batch processing
            messages: List of messages to process
            service_tier: Service tier ('standard' or 'flex')
            
        Returns:
            SwarmCompletionResponse
            
        Example:
            ```python
            response = client.swarm.create(
                name="Research Swarm",
                swarm_type="SequentialWorkflow",
                task="Research quantum computing advances in 2024",
                agents=[
                    {
                        "agent_name": "Researcher",
                        "description": "Conducts in-depth research",
                        "model_name": "gpt-4o"
                    },
                    {
                        "agent_name": "Critic",
                        "description": "Evaluates arguments for flaws",
                        "model_name": "gpt-4o-mini"
                    }
                ]
            )
            ```
        """
        # Process agents if they are dicts
        if 'agents' in kwargs and kwargs['agents']:
            agents = []
            for agent in kwargs['agents']:
                if isinstance(agent, dict):
                    agents.append(AgentSpec(**agent))
                else:
                    agents.append(agent)
            kwargs['agents'] = agents
        
        # Create and validate request
        request = SwarmSpec(**kwargs)
        
        # Make API request
        data = self.client._make_request('POST', 'v1/swarm/completions', data=request.model_dump())
        return _parse_response(SwarmCompletionResponse, data)
    
    def create_batch(self, swarms: List[Union[Dict, SwarmSpec]]) -> List[SwarmCompletionResponse]:
        """
        Create multiple swarm completions in batch.
        
        Args:
            swarms: List of swarm specifications
            
        Returns:
            List of SwarmCompletionResponse
            
        Example:
            ```python
            responses = client.swarm.create_batch([
                {
                    "name": "Research Swarm",
                    "swarm_type": "auto",
                    "task": "Research quantum computing",
                    "agents": [
                        {"agent_name": "Researcher", "model_name": "gpt-4o"}
                    ]
                },
                {
                    "name": "Writing Swarm",
                    "swarm_type": "SequentialWorkflow",
                    "task": "Write a blog post about AI safety",
                    "agents": [
                        {"agent_name": "Writer", "model_name": "gpt-4o"}
                    ]
                }
            ])
            ```
        """
        # Process each swarm
        request_data = []
        for swarm in swarms:
            if isinstance(swarm, dict):
                # Process agents if they are dicts
                if 'agents' in swarm and swarm['agents']:
                    agents = []
                    for agent in swarm['agents']:
                        if isinstance(agent, dict):
                            agents.append(AgentSpec(**agent))
                        else:
                            agents.append(agent)
                    swarm['agents'] = agents
                
                request_data.append(SwarmSpec(**swarm).model_dump())
            else:
                request_data.append(swarm.model_dump())
        
        # Make API request
        data = self.client._make_request('POST', 'v1/swarm/batch/completions', data=request_data)
        
        # Parse responses
        return [_parse_response(SwarmCompletionResponse, item) for item in data]
    
    def list_types(self) -> SwarmTypesResponse:
        """
        List available swarm types.
        
        Returns:
            SwarmTypesResponse
            
        Example:
            ```python
            response = client.swarm.list_types()
            print(response.swarm_types)
            ```
        """
        data = self.client._make_request('GET', 'v1/swarms/available')
        return _parse_response(SwarmTypesResponse, data)
    
    async def acreate(self, **kwargs) -> SwarmCompletionResponse:
        """
        Create a swarm completion asynchronously.
        
        Args:
            name: Name of the swarm
            description: Description of the swarm
            agents: List of agent specifications
            max_loops: Maximum number of loops
            swarm_type: Type of swarm
            task: The task to complete
            tasks: List of tasks for batch processing
            messages: List of messages to process
            service_tier: Service tier ('standard' or 'flex')
            
        Returns:
            SwarmCompletionResponse
        """
        # Process agents if they are dicts
        if 'agents' in kwargs and kwargs['agents']:
            agents = []
            for agent in kwargs['agents']:
                if isinstance(agent, dict):
                    agents.append(AgentSpec(**agent))
                else:
                    agents.append(agent)
            kwargs['agents'] = agents
        
        # Create and validate request
        request = SwarmSpec(**kwargs)
        
        # Make API request
        data = await self.client._make_async_request('POST', 'v1/swarm/completions', data=request.model_dump())
        return _parse_response(SwarmCompletionResponse, data)
    
    async def acreate_batch(self, swarms: List[Union[Dict, SwarmSpec]]) -> List[SwarmCompletionResponse]:
        """
        Create multiple swarm completions in batch asynchronously.
        
        Args:
            swarms: List of swarm specifications
            
        Returns:
            List of SwarmCompletionResponse
        """
        # Process each swarm
        request_data = []
        for swarm in swarms:
            if isinstance(swarm, dict):
                # Process agents if they are dicts
                if 'agents' in swarm and swarm['agents']:
                    agents = []
                    for agent in swarm['agents']:
                        if isinstance(agent, dict):
                            agents.append(AgentSpec(**agent))
                        else:
                            agents.append(agent)
                    swarm['agents'] = agents
                
                request_data.append(SwarmSpec(**swarm).model_dump())
            else:
                request_data.append(swarm.model_dump())
        
        # Make API request
        data = await self.client._make_async_request('POST', 'v1/swarm/batch/completions', data=request_data)
        
        # Parse responses
        return [_parse_response(SwarmCompletionResponse, item) for item in data]
    
    async def alist_types(self) -> SwarmTypesResponse:
        """
        List available swarm types asynchronously.
        
        Returns:
            SwarmTypesResponse
        """
        data = await self.client._make_async_request('GET', 'v1/swarms/available')
        return _parse_response(SwarmTypesResponse, data)

class ModelsResource(BaseResource):
    """API resource for model operations"""
    
    def list(self) -> ModelsResponse:
        """
        List available models.
        
        Returns:
            ModelsResponse
            
        Example:
            ```python
            response = client.models.list()
            print(response.models)
            ```
        """
        data = self.client._make_request('GET', 'v1/models/available')
        return _parse_response(ModelsResponse, data)
    
    async def alist(self) -> ModelsResponse:
        """
        List available models asynchronously.
        
        Returns:
            ModelsResponse
        """
        data = await self.client._make_async_request('GET', 'v1/models/available')
        return _parse_response(ModelsResponse, data)

class LogsResource(BaseResource):
    """API resource for log operations"""
    
    def list(self) -> LogsResponse:
        """
        List API request logs.
        
        Returns:
            LogsResponse
            
        Example:
            ```python
            response = client.logs.list()
            print(f"Found {response.count} logs")
            ```
        """
        data = self.client._make_request('GET', 'v1/swarm/logs')
        return _parse_response(LogsResponse, data)
    
    async def alist(self) -> LogsResponse:
        """
        List API request logs asynchronously.
        
        Returns:
            LogsResponse
        """
        data = await self.client._make_async_request('GET', 'v1/swarm/logs')
        return _parse_response(LogsResponse, data)

# Simplified default client for convenience
client = Swarms()