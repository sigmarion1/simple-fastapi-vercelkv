import os
import requests

from dotenv import load_dotenv

load_dotenv()


class KV:
    def __init__(self) -> None:
        self.url = os.getenv("KV_REST_API_URL")
        token = os.getenv("KV_REST_API_TOKEN")

        print(self.url)

        if not (self.url and token):
            raise Exception(
                "Both KV_REST_API_URL and KV_REST_API_TOKEN are required in .env file!"
            )

        self.headers = {"Authorization": f"Bearer {token}"}

    def get(self, key):
        get_url = f"{self.url}/get/{key}"
        response = requests.get(url=get_url, headers=self.headers)

        return response.json()["result"]

    def set(self, key, value):
        set_url = f"{self.url}/set/{key}/{value}"
        response = requests.get(url=set_url, headers=self.headers)

        return response.json()["result"]
