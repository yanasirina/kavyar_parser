import asyncio

from file_writer import write_followers_to_file
from logging_config import logger
from parser import get_followers


if __name__ == '__main__':
    logger.info(msg='Программа начала работу, ищем популярные журналы')
    followers = asyncio.run(get_followers())
    write_followers_to_file(followers=followers)
