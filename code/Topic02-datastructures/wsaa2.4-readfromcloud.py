import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
#print (response.json())
data = response.json()
#with open ("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

bpi = data["bpi"]
#print(bpi)
rate = bpi["EUR"]["rate"]
print(rate)
