import os
import slack

from config import config

slack_token = config['Slacker Squad'].get("oauth")

client = slack.WebClient(
    token=slack_token,
    run_async=True
)


async def send_async_message(channel='#random', text=''):
    response = await client.chat_postMessage(
        channel=channel,
        text=text
    )
    assert response["ok"]
    assert response["message"]["text"] == "Hello world!"
