from http.client import NOT_FOUND

import requests  # type: ignore[import]

from handles.platform import Platform


class Youtube(Platform):
    def is_available(self, package: str) -> bool:
        username_lower = package.lower()
        url = f'https://youtube.com/@{username_lower}'
        response = requests.get(url, timeout=10)
        return response.status_code == NOT_FOUND
