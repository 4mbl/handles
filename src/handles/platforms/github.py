import requests  # type: ignore[import]

from handles.platform import Platform


class Github(Platform):
    def is_available(self, username: str) -> bool:
        username_lower = username.lower()
        url = f'https://api.github.com/users/{username_lower}'
        response = requests.get(url, timeout=10).json()
        return 'message' in response and response['message'] == 'Not Found'
