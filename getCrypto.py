import requests
from datetime import date

def getInfo(symbol):
    response = requests.get("https://data.messari.io/api/v1/assets/"+symbol+"/metrics")
    res = response.json()
    name = res['data']['name']
    price = res['data']['market_data']['price_usd']
    return name, price
