import requests


def is_available(username: str) -> bool:
    username_lower = username.lower()
    url = f'https://api.github.com/users/{username_lower}'
    response = requests.get(url.format(username_lower), timeout=10).json()
    return "message" in response and response['message'] == "Not Found"


def are_available(usernames: list) -> list:
    return list(filter(is_available, usernames))
