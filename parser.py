from models import User
from workers import UserHttpWorker
from logging_config import logger


http_worker = UserHttpWorker()


def get_publisher_slugs() -> list[str]:
    json_data = http_worker.get_user_list(user_type='trending-publishers', limit=10000)
    slugs = [publisher['profile']['slug'] for publisher in json_data]
    logger.info(f'Найдено {len(slugs)} журналов для обработки')
    return slugs


def get_publisher_follower_slugs(publisher_slug: str) -> list[str]:
    json_data = http_worker.get_user_followers(user_slug=publisher_slug, limit=100000)
    slugs = [follower['slug'] for follower in json_data]
    return slugs


def get_all_follower_slugs() -> list[str]:
    follower_slugs = []
    publisher_slugs = get_publisher_slugs()
    for index, publisher_slug in enumerate(publisher_slugs):
        logger.info(f'Обработка журнала "{publisher_slug}", осталось {len(publisher_slugs) - index} журналов')
        try:
            publisher_followers = get_publisher_follower_slugs(publisher_slug)
        except ConnectionError:
            logger.warning(f'Не удалось собрать подписчиков журнала "{publisher_slug}"')
            continue
        else:
            follower_slugs.extend(publisher_followers)
    return list(set(follower_slugs))


def get_follower(follower_slug: str) -> User:
    json_data = http_worker.get_user_detail(user_slug=follower_slug)
    email = json_data['detail']['contact'].get('email')
    instagram = json_data['detail']['contact'].get('instagram')
    return User(slug=follower_slug, email=email, instagram=instagram)


def get_followers() -> list[User]:
    followers = []
    follower_slugs = get_all_follower_slugs()
    for follower_slug in follower_slugs:
        try:
            follower = get_follower(follower_slug=follower_slug)
        except ConnectionError:
            continue
        else:
            followers.append(follower)
    return followers


def write_followers_to_file(followers: list[User]):
    pass


def write_data_to_file():
    followers = get_followers()
    write_followers_to_file(followers=followers)


if __name__ == '__main__':
    logger.info(msg='Программа начала работу, ищем популярные журналы')
    write_data_to_file()
