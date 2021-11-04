from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)

@app.route('/<ticker>', methods=['POST', 'GET'])
def index(ticker):

    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-profile"

    querystring = {"symbol":ticker,"region":"US"}

    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "3881371422mshef5287c1e084505p1b5e4cjsn4e06a31bae67"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    print(res['assetProfile']['longBusinessSummary'])
    print(res['price']['regularMarketPrice']['fmt'])
    data = {
        'description': res['assetProfile']['longBusinessSummary'],
        'price': res['price']['regularMarketPrice']['fmt']
        }
    return data

if __name__ == "__main__":
    app.run(debug=True)