from swarms_client.client import SwarmsClient
import os
from dotenv import load_dotenv

load_dotenv()

client = SwarmsClient(api_key=os.getenv("SWARMS_API_KEY"))

if __name__ == "__main__":
    out = client.models.list()
    print(out.model_dump_json(indent=4))
