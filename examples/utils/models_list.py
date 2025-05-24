from swarms_client import SwarmsClient


def main():
    # Initialize the Swarms client
    client = SwarmsClient()

    models = client.models.list_models()
    print(models)


if __name__ == "__main__":
    main()
