from flask import Flask, abort, request
from twilio.twiml.messaging_response import MessagingResponse
import os

from sms_gpt.open_ai_client import get_chat_completion

app = Flask(__name__)


@app.route("/sms/respond", methods=["GET", "POST"])
def sms_reply() -> str:
    body: str | None = request.values.get("Body", None)

    if body is None:
        abort(404)

    messaging_response = MessagingResponse()
    gpt_response: str = get_chat_completion(body)
    messaging_response.message(gpt_response)

    return str(messaging_response)


def start() -> None:
    """Start the server."""
    port: int = int(os.environ.get("PORT", 5000))
    host: str = os.environ.get("HOST", "0.0.0.0")

    app.run(debug=True, port=port, host=host)


if __name__ == "__main__":
    start()
