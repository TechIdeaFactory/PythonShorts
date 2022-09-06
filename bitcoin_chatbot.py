import json
import requests


def get_bitcoin_price():
    try:

        req = requests.get(
            "https://api.coingecko.com/api/v3/simple/"
            + "price?ids=bitcoin&vs_currencies=usd"
        ).text

        req = json.loads(req)

        return req["bitcoin"]["usd"]

    except:

        return "Error"


def lambda_handler(event, context):
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {"contentType": "PlainText"},
        }
    }

    if event["currentIntent"]["name"] == "GetBitcoinPriceIntent":
        response["dialogAction"]["message"]["content"] = "Bitcoin USD Price = " + str(
            get_bitcoin_price()
        )

    return response
