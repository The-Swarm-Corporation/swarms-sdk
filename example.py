import os

from dotenv import load_dotenv

from src.swarms_client import SwarmsClient

load_dotenv()

client = SwarmsClient(
    api_key=os.environ.get("SWARMS_API_KEY"),  # This is the default and can be omitted
)

response = client.get_root()
models = client.models.list_available()
print(models)
