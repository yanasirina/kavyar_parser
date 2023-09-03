import asyncio

from file_writer import write_followers_to_file
from logging_config import logger
from kavyar_parser import get_followers


if __name__ == '__main__':
    publisher_slug = input(
        'Отправьте username журнала на kavyar. Например, redline-magazine.\n'
        'Если хотите собрать информацию по всем журналам - оставьте поле пустым: '
    )
    logger.info(msg='Программа начала работу.')
    followers = asyncio.run(get_followers(publisher_slug=publisher_slug))
    write_followers_to_file(followers=followers)
