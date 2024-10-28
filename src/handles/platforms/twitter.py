import random
from http.client import OK
from typing import ClassVar

import requests  # type: ignore[import]


class Twitter:
    USER_AGENTS: ClassVar[list[str]] = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36',  # noqa: E501
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/111.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',  # noqa: E501
    ]

    NOT_FOUND = 404

    def is_available(self, username: str) -> bool:
        username_lower = username.lower()
        url = f'https://x.com/{username_lower}'
        headers = {
            'User-Agent': random.choice(self.USER_AGENTS),  # noqa:  S311
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
        }

        response = requests.get(url, headers=headers, timeout=10)
        return response.status_code != OK
