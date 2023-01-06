import openai
import requests
import time
import os

openai.api_key = "your key"

description = input(
    "Enter art description"
)

response = openai.Image.create(
    prompt=description,
    n=1,
    size="1024x1024",
)

image_url = response["data"][0]["url"]
response = requests.get(image_url)

ts = time.time()
out_file = "ai_art." + str(ts) + ".png"

open(out_file, "wb").write(
    response.content
)

