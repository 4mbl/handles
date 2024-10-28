import requests


def is_available(package: str) -> bool:
    package_lower = package.lower()
    url = f'https://registry.npmjs.org/{package_lower}'
    response = requests.get(url.format(package_lower), timeout=10).json()
    return 'error' in response and response['error'] == "Not found"


def are_available(packages: list) -> list:
    return list(filter(is_available, packages))
