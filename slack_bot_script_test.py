import os
import slack
import asyncio
from config import config

loop = asyncio.get_event_loop()
slack_token = config['Slacker Squad'].get("oauth")

client = slack.WebClient(
    token=slack_token,
    run_async=True
)

response = loop.run_until_complete(
    client.chat_postMessage(
        channel='#random',
        text="Hello world!",
    ),
)
assert response["ok"]
assert response["message"]["text"] == "Hello world!"
