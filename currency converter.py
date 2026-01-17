import requests

url = "https://v6.exchangerate-api.com/v6/3e38f9c79f5fd4a32eb46f85/latest/USD"
x = requests.get(url).json()

curr1 = input("Enter currency you have: ").upper()
curr2 = input("Enter currency you want to convert to: ").upper()

amount = float(input("Enter amount: "))

rates = x['conversion_rates']

for i in rates:
    if curr1 == i:
        print(rates.get(curr2) * amount)
        




