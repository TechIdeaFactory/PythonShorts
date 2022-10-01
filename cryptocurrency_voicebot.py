import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import requests
import json

def get_bitcoin_price():
    req = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true"
        "-H 'accept: application/json"
    ).text

    req = json.loads(req)
    return req["bitcoin"]["usd"]

def get_ethereum_price():
    req = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_last_updated_at=true"
        "-H 'accept: application/json"
    ).text

    req = json.loads(req)
    return req["ethereum"]["usd"]


def bot_listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as microphone:
            voice_input = (
                listener.listen(
                    microphone
                )
            )
            input_text = listener.recognize_google(
                voice_input
            )
            print(input_text)
            return input_text
    except:
        return "bitcoin"


def bot_talk(text):
    language = "en"
    obj = gTTS(
        text=text,
        lang=language,
        slow=False,
    )
    obj.save("speech.mp3")
    playsound("speech.mp3")


def run_bot():
    while True:
        bot_talk(
            "Are you interested in Bitcoin or Ethereum"
        )
        crypto = bot_listen()
        if (
            "eth" in crypto.lower()
            or "rium" in crypto.lower()
        ):
            response = (
                "Price in dollars for Ethereum is "
                + str(
                    get_ethereum_price()
                )
            )
        else:
            response = (
                "Price in dollars for Bitcoin is "
                + str(
                    get_bitcoin_price()
                )
            )

        bot_talk(response)
        bot_talk(
            "Would you like another price, yes or no?"
        )
        user_input = bot_listen()

        if "no" in user_input.lower():
            print(user_input)
            bot_talk("Goodbye")
            break


run_bot()
