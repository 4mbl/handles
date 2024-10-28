import requests  # type: ignore[import]

from handles.platform import Platform


class Medium(Platform):
    def is_available(self, username: str) -> bool:
        hearders = {
            'headers': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'  # noqa: E501
        }
        response = requests.get(f'https://medium.com/@{username}', timeout=10, headers=hearders)
        al = response.text
        return al[al.find('<title') + 6 : al.find('</title>')].split('>')[1] == 'Medium'
