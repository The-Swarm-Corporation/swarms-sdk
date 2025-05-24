from swarms_client import SwarmsClient


def main():
    # Initialize the Swarms client
    client = SwarmsClient()

    models = client.swarm.list_types()
    print(models)


if __name__ == "__main__":
    main()
