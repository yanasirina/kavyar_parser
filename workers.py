import requests

import config
from logging_config import logger


class UserHttpWorker:
    def __init__(self, base_url: str = config.BASE_API_URL):
        self.base_url = base_url
        self.headers = {"user-agent": "Mozilla/5.0"}

    def get_user_list(self, user_type: str, limit: int = 1000):
        url = self.base_url + f'discover/{user_type}?limit={limit}'
        response = requests.get(url, headers=self.headers, timeout=10000)
        if response.status_code == 200:
            return response.json()['payload'][0]['records']
        else:
            raise ConnectionError("kavyar.com didn't answer")

    async def get_user_detail(self, session, user_slug: str):
        url = self.base_url + f'profiles/{user_slug}'
        async with session.get(url, headers=self.headers, timeout=10000) as resp:
            logger.info(f'Обработка пользователя "{user_slug}"')
            if resp.status == 200:
                json_resp = await resp.json()
                return json_resp['payload'][0]['records'][0]
            else:
                return None

    async def get_user_followers(self, session, user_slug: str, limit: int = 1000):
        url = self.base_url + f'profiles/{user_slug}/followers?limit={limit}'
        async with session.get(url, headers=self.headers, timeout=10000) as resp:
            logger.info(f'Обработка журнала "{user_slug}"')
            if resp.status == 200:
                json_resp = await resp.json()
                return json_resp['payload'][0]['records']
            else:
                raise ConnectionError("kavyar.com didn't answer")
