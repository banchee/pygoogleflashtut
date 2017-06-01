import json
import urllib2


def getExchangeRates():
    rates = []
    response = urllib2.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data, parse_float=float)

    rates.append(rdata['rates']['USD'])
    rates.append(rdata['rates']['GBP'])
    rates.append(rdata['rates']['JPY'])
    rates.append(rdata['rates']['AUD'])
    return rates

rates = getExchangeRates()
print rates
