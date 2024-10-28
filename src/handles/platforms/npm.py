import requests  # type: ignore[import]

from handles.platform import Platform


class Npm(Platform):
    def is_available(self, package: str) -> bool:
        package_lower = package.lower()
        url = f'https://registry.npmjs.org/{package_lower}'
        response = requests.get(url.format(package_lower), timeout=10).json()
        return 'error' in response and response['error'] == 'Not found'
