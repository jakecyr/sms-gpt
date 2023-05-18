# SMS GPT

A simple service to SMS Chat with OpenAI GPT models. Was built to receive requests to the webhook from Twilio when messages are received. The message received is sent to the OpenAI GPT model and then returned to the user via SMS.

## Development

Poetry is used for package management. To get started, make sure you have poetry installed and then run `poetry install`.

## Deploying

The service can be deployed to any web server that supports Python. A Twilio account must be setup, and configured with an activate phone number that supports SMS. A webhook should be added to send messages to the /sms/respond route.

Before deploying to server, if the pyproject.toml file has changed, update the requirements.txt file with:

```bash
poetry export --without-hashes > requirements.txt 
```
