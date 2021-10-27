from flask import Flask, render_template, url_for, request, redirect
import requests
from getCrypto import getInfo

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    response = requests.get("https://top9currencyrate.herokuapp.com/currency")
    currencyList = response.json()
    if request.method == 'POST':

        # get form data
        req = request.form
        cr1 = req['crypto1']
        cr2 = req['crypto2']
        cr3 = req['crypto3']
        currency = req['currency']
        rate = 1.00

        # get exchange rate
        for obj in currencyList:
            if currency == obj['country']:
                print('matched')
                
                rate = obj['rate']

        # get required crypto
        name1, price = getInfo(cr1)
        print(type(price), type(rate))
        price *= float(rate)
        format_price1 = "{:,.2f}".format(price)

        # get other two crypto if not none
        if cr2 != "":
            name2, price = getInfo(cr2)
            price *= float(rate)
            format_price2 = "{:,.2f}".format(price)
        else:
            name2 = ""
            format_price2 = ""

        if cr3 != "":
            name3, price = getInfo(cr3)
            price *= float(rate)
            format_price3 = "{:,.2f}".format(price)
        else:
            name3 = ""
            format_price3 = ""


        return render_template('index.html', n1 = name1, p1 = format_price1, n2 = name2, p2 = format_price2, n3 = name3, p3 = format_price3, currency = currency)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)