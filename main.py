import requests


def main():
    cities = ['London', 'svo', 'Череповец']

    payload = {
        'nTqM': '',
        'lang': 'ru',
    }

    for city in cities:
        url = f'https://wttr.in/{city}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()
