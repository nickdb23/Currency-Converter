import requests

class Data:

    url = "https://v6.exchangerate-api.com/v6/3e38f9c79f5fd4a32eb46f85/latest/USD"
    x = requests.get(url).json()
    rates = x['conversion_rates']

    #getter methods
    def getTable(cls):
        return cls.rates
    
    def getNames(cls):
        return cls.rates.keys()
    
    def getValues(cls):
        return cls.rates.values()
    
