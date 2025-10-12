from http.client import OK

import requests  # type: ignore[import]

from handles.platform import Platform


class Bluesky(Platform):
    def is_available(self, username: str) -> bool:
        handle = username.strip()
        handle = handle + '.bsky.social'
        handle = handle.lower()
        url = f'https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?handle={handle}'
        response = requests.get(url, timeout=10)
        return response.status_code != OK

    def format_username(self, username: str) -> str:
        return '@' + username + '.bsky.social'
