import asyncio
from typing import Optional

import aiohttp

from models import User
from workers import UserHttpWorker
from logging_config import logger


http_worker = UserHttpWorker()


def get_publisher_slugs() -> list[str]:
    json_data = http_worker.get_user_list(user_type='trending-publishers', limit=10000)
    slugs = [publisher['profile']['slug'] for publisher in json_data]
    logger.info(f'Найдено {len(slugs)} журналов для обработки')
    return slugs


async def get_publisher_follower_slugs(session, publisher_slug: str) -> list[str]:
    json_data = await http_worker.get_user_followers(session=session, user_slug=publisher_slug, limit=100000)
    slugs = [follower['slug'] for follower in json_data]
    return slugs


async def get_all_follower_slugs() -> list[str]:
    follower_slugs = []
    publisher_slugs = get_publisher_slugs()

    connector = aiohttp.TCPConnector(limit=50)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for publisher_slug in publisher_slugs:
            task = asyncio.create_task(get_publisher_follower_slugs(session=session, publisher_slug=publisher_slug))
            tasks.append(task)
        await asyncio.gather(*tasks)

        for task in tasks:
            follower_slugs.extend(await task)
        logger.info(f'Найдено {len(set(follower_slugs))} пользователей для обработки')

    return list(set(follower_slugs))


async def get_follower(session, follower_slug: str) -> Optional[User]:
    json_data = await http_worker.get_user_detail(session=session, user_slug=follower_slug)
    if json_data:
        email = json_data['detail']['contact'].get('email')
        instagram = json_data['detail']['contact'].get('instagram')
        return User(slug=follower_slug, email=email, instagram=instagram)


async def get_followers(publisher_slug=None) -> list[User]:
    followers = []
    connector = aiohttp.TCPConnector(force_close=True)
    async with aiohttp.ClientSession(connector=connector) as session:
        if publisher_slug:
            follower_slugs = await get_publisher_follower_slugs(session=session, publisher_slug=publisher_slug)
        else:
            follower_slugs = await get_all_follower_slugs()

        tasks = []
        for follower_slug in follower_slugs:
            task = asyncio.create_task(get_follower(session=session, follower_slug=follower_slug))
            tasks.append(task)
        await asyncio.gather(*tasks)

        for task in tasks:
            follower = await task
            if follower:
                followers.append(await task)
        logger.info(f'Найдено {len(set(follower_slugs))} пользователей для обработки')

    return followers
