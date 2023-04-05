import requests


def is_available(username: str) -> bool:
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url.format(username), timeout=10).json()
    return "message" in response and response['message'] == "Not Found"


def are_available(usernames: list) -> list:
    available = []
    for username in usernames:
        if is_available(username):
            available.append(username)
    return available
