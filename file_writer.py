import datetime


def write_instagrams(followers):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'instagrams_{current_time}.txt', 'w') as file:
        for follower in followers:
            if follower.instagram:
                file.write(f'{follower.instagram}\n')


def write_emails(followers):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'emails_{current_time}.txt', 'w') as file:
        for follower in followers:
            if follower.email:
                file.write(f'{follower.email}\n')


def write_slugs_emails_instagrams(followers):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'info_{current_time}.txt', 'w') as file:
        for follower in followers:
            file.write(f'slug: {follower.slug}\n')
            if follower.email:
                file.write(f'email: {follower.email}\n')
            if follower.instagram:
                file.write(f'instagram: {follower.instagram}\n')
            file.write('\n')


def write_followers_to_file(followers):
    write_instagrams(followers=followers)
    write_emails(followers=followers)
    write_slugs_emails_instagrams(followers=followers)
