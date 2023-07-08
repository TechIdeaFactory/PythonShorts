# pip install openai
# pip install --upgrade openai

# Note chatgpt does not always
# return the score and analysis
# in brackets as requested

import openai
import re

openai.api_key = "your key"


def feedback_score(
    feedback: str,
) -> (int, str):
    # Define the system message
    system_msg = (
        "You are a helpful assistant "
        "who understands data science."
    )

    # Define the user message
    user_msg = (
        "Is the following customer "
        "feedback review negative, neutral"
        "or positive. Return a single integer "
        "score from 0 to 10,"
        "with 0 being the most negative, "
        "5 being neutral and 10"
        "the most positive score. "
        "The score must be returned as a "
        "single digit "
        "which is inside square brackets"
        "for example [5]. Only return the score"
        "inside square brackets."
        "Explain the reason for the score. "
        "The reason for the score should be "
        "text inside curly braces."
        "For example {positve as good feedback}"
        "The customer review is as follows: "
        + feedback
    )

    # Create feedback analysis using GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_msg,
            },
            {
                "role": "user",
                "content": user_msg,
            },
        ],
    )

    generated_text = response[
        "choices"
    ][0]["message"]["content"]
    print(generated_text)
    score = generated_text.split('[', 1)[1].split(']')[0]
    analysis = generated_text.split('{', 1)[1].split('}')[0]

    return (score, analysis)


feedback = (
    "The product was delivered on"
    "time, but only worked for a"
    "few days. I would need to think"
    "carefully before recommending"
    "it to friends. Last time"
    "I use this company!!!"
)

result = feedback_score(feedback)
print(result)
