from models import User


def get_publisher_slugs() -> list[str]:
    pass


def get_publisher_follower_slugs(publisher_slug: str) -> list[str]:
    pass


def get_all_follower_slugs(publisher_slugs: list['str']) -> list[str]:
    followers = []
    for publisher_slug in publisher_slugs:
        publisher_followers = get_publisher_follower_slugs(publisher_slug)
        followers.extend(publisher_followers)
    return followers


def get_follower(follower_slug: str) -> User:
    pass


def get_followers(follower_slugs: list[str]) -> list[User]:
    followers = []
    for follower_slug in follower_slugs:
        followers.append(get_follower(follower_slug=follower_slug))
    return followers


def write_publishers_to_file(publisher_slugs: list['str']):
    pass


def write_followers_to_file(followers: list[User]):
    pass


def write_data_to_files():
    publisher_slugs = get_publisher_slugs()
    follower_slugs = get_all_follower_slugs(publisher_slugs=publisher_slugs)
    followers = get_followers(follower_slugs=follower_slugs)
    write_publishers_to_file(publisher_slugs=publisher_slugs)
    write_followers_to_file(followers=followers)


if __name__ == '__main__':
    write_data_to_files()
