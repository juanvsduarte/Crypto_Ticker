import json
import requests
  
# defining key/request url
keybtc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
# requesting data from url
data = requests.get(keybtc)  
data = data.json()
btc = (f"{data['symbol']} price is {data['price']}")

# defining key/request url
keyeth = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
  
# requesting data from url
data = requests.get(keyeth)  
data = data.json()
eth = (f"{data['symbol']} price is {data['price']}")
