import requests


def is_available(username: str) -> bool:
    hearders = {
        'headers':
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
    response = requests.get(f'https://medium.com/@{username}',
                            timeout=10,
                            headers=hearders)
    al = response.text
    return al[al.find('<title') +
              6:al.find('</title>')].split('>')[1] == "Medium"


def are_available(usernames: list) -> list:
    return list(filter(is_available, usernames))
