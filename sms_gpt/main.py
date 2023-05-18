from typing import Any
from flask import Flask, abort, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)


@app.route("/sms/respond", methods=["GET", "POST"])
def sms_reply() -> str:
    # Get the incoming text message
    body: str | None = request.values.get("Body", None)

    if body is None:
        abort(404)

    messaging_response = MessagingResponse()

    completion: Any = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": body}],
        model="gpt-3.5-turbo",
        max_tokens=500,
        temperature=0.7,
    )

    choices = completion["choices"]
    first_choice = choices[0]
    first_choice_text: str = (
        first_choice["message"]["content"].replace("\n", " ").strip()
    )

    messaging_response.message(first_choice_text)

    return str(messaging_response)


def start() -> None:
    OPEN_AI_KEY: str | None = os.environ.get("OPENAI_API_KEY")

    if not OPEN_AI_KEY:
        raise ValueError("Missing OPENAI_API_KEY env variable")

    openai.api_key = OPEN_AI_KEY

    port: int = int(os.environ.get("PORT", 5000))
    host: str = os.environ.get("HOST", "0.0.0.0")

    app.run(debug=True, port=port, host=host)


if __name__ == "__main__":
    start()
