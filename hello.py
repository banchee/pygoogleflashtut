from flask import Flask, render_template
import os
import json
import urllib.request as urllib2


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


def getExchangeRates():
    rates = []
    response = urllib2.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data, parse_float=float)

    rates.append(rdata['rates']['USD'])
    rates.append(rdata['rates']['GBP'])
    rates.append(rdata['rates']['HKD'])
    rates.append(rdata['rates']['AUD'])
    return rates


@app.route("/")
def index():
    rates = getExchangeRates()
    return render_template('test.html', **locals())


@app.route("/activationstate")
def index2():
    # rates = getExchangeRates()
    return render_template('activationstate.html', **locals())


@app.route("/test3")
def index3():
    # rates = getExchangeRates()
    return render_template('test3.html', **locals())


@app.route("/test4")
def index4():
    # rates = getExchangeRates()
    return render_template('test4.html', **locals())


@app.route("/test5")
def index5():
    # rates = getExchangeRates()
    return render_template('test5.html', **locals())

@app.route("/test6")
def index6():
    # rates = getExchangeRates()
    return render_template('test6.html', **locals())


@app.route("/main")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
