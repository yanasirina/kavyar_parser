from models import User
from workers import UserHttpWorker


http_worker = UserHttpWorker()


def get_publisher_slugs() -> list[str]:
    json_data = http_worker.get_user_list(user_type='trending-publishers', limit=10000)
    slugs = [publisher['profile']['slug'] for publisher in json_data]
    return slugs


def get_publisher_follower_slugs(publisher_slug: str) -> list[str]:
    json_data = http_worker.get_user_followers(user_slug=publisher_slug, limit=100000)
    slugs = [follower['slug'] for follower in json_data]
    return slugs


def get_all_follower_slugs() -> list[str]:
    follower_slugs = []
    publisher_slugs = get_publisher_slugs()
    for publisher_slug in publisher_slugs:
        publisher_followers = get_publisher_follower_slugs(publisher_slug)
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
        followers.append(get_follower(follower_slug=follower_slug))
    return followers


def write_followers_to_file(followers: list[User]):
    pass


def write_data_to_file():
    followers = get_followers()
    write_followers_to_file(followers=followers)


if __name__ == '__main__':
    write_data_to_file()
