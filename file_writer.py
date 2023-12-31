import datetime

from logging_config import logger
from models import User


def write_instagrams(followers: list[User]):
    logger.info(msg='Собираем инстаграмы.')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'instagrams_{current_time}.txt', 'w', encoding="utf-8") as file:
        for follower in followers:
            if follower.instagram:
                file.write(f'{str(follower.instagram)}\n')


def write_emails(followers: list[User]):
    logger.info(msg='Собираем электронные адреса.')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'emails_{current_time}.txt', 'w', encoding="utf-8") as file:
        for follower in followers:
            if follower.email:
                file.write(f'{str(follower.email)}\n')


def write_slugs_emails_instagrams(followers: list[User]):
    logger.info(msg='Собираем общую информацию.')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'info_{current_time}.txt', 'w', encoding="utf-8") as file:
        for follower in followers:
            file.write(f'slug: {str(follower.slug)}\n')
            if follower.email:
                file.write(f'email: {str(follower.email)}\n')
            if follower.instagram:
                file.write(f'instagram: {str(follower.instagram)}\n')
            file.write('\n')


def write_followers_to_file(followers: list[User]):
    write_instagrams(followers=followers)
    write_emails(followers=followers)
    write_slugs_emails_instagrams(followers=followers)
