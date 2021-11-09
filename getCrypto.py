import requests
from datetime import date
# from dateutil.relativedelta import relativedelta

def getInfo(symbol):
    response = requests.get("https://data.messari.io/api/v1/assets/"+symbol+"/metrics")
    res = response.json()
    name = res['data']['name']
    price = res['data']['market_data']['price_usd']

    # today = date.today()
    # startDate = today - relativedelta(days=-30)

    # response = requests.get(f"https://data.messari.io/api/v1/assets/{symbol}/metrics/price/time-series?start={startDate}&end={today}&interval=1d&columns=close&format=json")
    # print(response.json())


    return name, price
