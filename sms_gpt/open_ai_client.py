from typing import Any
import openai
import os

OPEN_AI_KEY: str | None = os.environ.get("OPENAI_API_KEY")

if not OPEN_AI_KEY:
    raise ValueError("Missing OPENAI_API_KEY env variable")

openai.api_key = OPEN_AI_KEY


def get_chat_completion(
    user_message: str, model="gpt-3.5-turbo", max_tokens=500, temperature=0.7
) -> str:
    """Get a chat completion from the specified OpenAI GPT model.

    Args:
      user_message: The message to send to the OpenAI GPT model.
      model: The GPT model to use.
      max_token: The max number of tokens to consume in the request.
      temperature: The "creativity" of the response, 0 being more precise and consistent.

    Returns:
      The response from the model.
    """
    completion: Any = openai.ChatCompletion.create(
        messages=[{"role": "user", "content": user_message}],
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    choices: list = completion["choices"]
    first_choice: dict = choices[0]

    return first_choice["message"]["content"].replace("\n", " ").strip()
