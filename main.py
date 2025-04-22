import requests

cities = ['London', 'Шереметьево', 'Череповец']

for city in cities:
    url = f'https://wttr.in/{city}?nTqu&lang=ru{"&m" if city != "London" else ""}'
    url_city = url.format(city)
    response = requests.get(url_city)
    response.raise_for_status()
    print(response.text)
    print('-' * 30)
