import requests

urls = ["https://api.mercadolibre.com/items/MLB1150156997"]*20

for url in urls:
    response = requests.get(url)
    print(response.json()["title"])