from flask import Flask, render_template, url_for, request, redirect
import requests
from getCrypto import getInfo

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    response = requests.get("https://cs361-currency-scraper.herokuapp.com/currency/")
    currencyList = response.json()
    if request.method == 'POST':

        req = request.form
        crypto = getFormData(req)
        rate = 1.00

        rate = getExchangeRate(currencyList, crypto)

        # get required crypto
        cr1 = getCrypto(crypto, rate, 'cr1')
        cr2 = getCrypto(crypto, rate, 'cr2')
        cr3 = getCrypto(crypto, rate, 'cr3')

        data = {
            'cr1': cr1,
            'cr2': cr2,
            'cr3': cr3
        }

        return render_template('index.html', data=data, currency = crypto['currency'])
    else:
        return render_template('index.html')

def getFormData(req):
    crObj = {
        'cr1': req['crypto1'],
        'cr2': req['crypto2'],
        'cr3': req['crypto3'],
        'currency': req['currency']
    }
    return crObj

def getExchangeRate(currencyList, crypto):
    for obj in currencyList:
        if crypto['currency'] == obj['country']:
            rate = obj['rate']
    return rate

def getCrypto(crypto, rate, input):
    if crypto[input] != "":     
        name, price = getInfo(crypto[input])
        price *= float(rate)
        format_price = "{:,.2f}".format(price)
    else:
        name = ''
        format_price = ''
    return {'name': name, 'price': format_price}

if __name__ == "__main__":
    app.run(debug=True)