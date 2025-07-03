# SwarmsClient

Methods:

- <code title="get /">client.<a href="./src/swarms/_client.py">get_root</a>() -> object</code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/swarms/resources/health.py">check</a>() -> object</code>

# Agent

Types:

```python
from swarms.types import AgentCompletion, AgentSpec, AgentRunResponse
```

Methods:

- <code title="post /v1/agent/completions">client.agent.<a href="./src/swarms/resources/agent/agent.py">run</a>(\*\*<a href="src/swarms/types/agent_run_params.py">params</a>) -> <a href="./src/swarms/types/agent_run_response.py">AgentRunResponse</a></code>

## Batch

Types:

```python
from swarms.types.agent import BatchRunResponse
```

Methods:

- <code title="post /v1/agent/batch/completions">client.agent.batch.<a href="./src/swarms/resources/agent/batch.py">run</a>(\*\*<a href="src/swarms/types/agent/batch_run_params.py">params</a>) -> <a href="./src/swarms/types/agent/batch_run_response.py">BatchRunResponse</a></code>

# Models

Types:

```python
from swarms.types import ModelListAvailableResponse
```

Methods:

- <code title="get /v1/models/available">client.models.<a href="./src/swarms/resources/models.py">list_available</a>() -> <a href="./src/swarms/types/model_list_available_response.py">ModelListAvailableResponse</a></code>

# Swarms

Types:

```python
from swarms.types import (
    SwarmSpec,
    SwarmCheckAvailableResponse,
    SwarmGetLogsResponse,
    SwarmRunResponse,
)
```

Methods:

- <code title="get /v1/swarms/available">client.swarms.<a href="./src/swarms/resources/swarms/swarms.py">check_available</a>() -> <a href="./src/swarms/types/swarm_check_available_response.py">SwarmCheckAvailableResponse</a></code>
- <code title="get /v1/swarm/logs">client.swarms.<a href="./src/swarms/resources/swarms/swarms.py">get_logs</a>() -> <a href="./src/swarms/types/swarm_get_logs_response.py">SwarmGetLogsResponse</a></code>
- <code title="post /v1/swarm/completions">client.swarms.<a href="./src/swarms/resources/swarms/swarms.py">run</a>(\*\*<a href="src/swarms/types/swarm_run_params.py">params</a>) -> <a href="./src/swarms/types/swarm_run_response.py">SwarmRunResponse</a></code>

## Batch

Types:

```python
from swarms.types.swarms import BatchRunResponse
```

Methods:

- <code title="post /v1/swarm/batch/completions">client.swarms.batch.<a href="./src/swarms/resources/swarms/batch.py">run</a>(\*\*<a href="src/swarms/types/swarms/batch_run_params.py">params</a>) -> <a href="./src/swarms/types/swarms/batch_run_response.py">BatchRunResponse</a></code>
