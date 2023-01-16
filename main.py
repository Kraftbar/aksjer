import requests
import json

api_key = "6EYUE1X4T46W3H8S"
symbol = "AAPL"

url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}&interval=annual"

response = requests.get(url)
data = json.loads(response.text)

# Extracting the data
revenue = data["annual"]["Revenue"]
profit = data["annual"]["Net Income"]

# print the data for several years
for year in revenue:
    print(f"Year: {year}")
    print(f"Revenue: {revenue[year]}")
    print(f"Profit: {profit[year]}")
