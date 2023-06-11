import requests


def is_available(username: str) -> bool:
    username_lower = username.lower()
    url = f'https://instagram.com/{username_lower}'
    response = requests.get(url.format(username_lower), timeout=10)
    return response.status_code == 404


def are_available(usernames: list) -> list:
    return list(filter(is_available, usernames))
