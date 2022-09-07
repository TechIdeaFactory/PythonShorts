import requests
import json


def get_bitcoin_price():
    req = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true"
        "-H 'accept: application/json"
    ).text

    req = json.loads(req)
    return req["bitcoin"]["usd"]


print("Bitcoin usd price = " + str(get_bitcoin_price()))
