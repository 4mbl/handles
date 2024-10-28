from http.client import NOT_FOUND

import requests  # type: ignore[import]

from handles.platform import Platform


class Instagram(Platform):
    def is_available(self, username: str) -> bool:
        username_lower = username.lower()
        url = f'https://instagram.com/{username_lower}'
        response = requests.get(url, timeout=10)
        return response.status_code == NOT_FOUND
