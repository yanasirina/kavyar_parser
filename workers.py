import config

import requests


class UserHttpWorker:
    def __init__(self, base_url: str = config.BASE_API_URL):
        self.base_url = base_url
        self.headers = {"user-agent": "Mozilla/5.0"}

    def get_user_list(self, user_type: str, limit: int = 1000):
        url = self.base_url + f'discover/{user_type}?limit={limit}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['payload'][0]['records']
        else:
            raise ConnectionError("kavyar.com didn't answer")

    def get_user_detail(self, user_slug: str):
        url = self.base_url + f'profiles/{user_slug}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['payload'][0]['records'][0]
        else:
            raise ConnectionError("kavyar.com didn't answer")

    def get_user_followers(self, user_slug: str, limit: int = 1000):
        url = self.base_url + f'profiles/{user_slug}/followers?limit={limit}'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['payload'][0]['records']
        else:
            raise ConnectionError("kavyar.com didn't answer")
