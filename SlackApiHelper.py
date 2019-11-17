import slack
from typing import List

from config import config


class SlackApiHelper:
    user_client = None
    bot_client = None

    @staticmethod
    def get_bot_client():
        if SlackApiHelper.bot_client is None:
            bot_token = config['Slacker Squad'].get("bot_oauth")
            SlackApiHelper.bot_client = slack.WebClient(token=bot_token)
        return SlackApiHelper.bot_client

    @staticmethod
    def get_user_client():
        if not SlackApiHelper.user_client:
            user_token = config['Slacker Squad'].get("user_oauth")
            SlackApiHelper.user_client = slack.WebClient(token=user_token)
        return SlackApiHelper.user_client

    @staticmethod
    def get_channels():
        client = SlackApiHelper.get_bot_client()
        all_channels = client.channels_list().data.get('channels', [])
        return all_channels

    @staticmethod
    def find_channel_id_from_name(name: str, all_channels: List):
        channel_id_to_get = None

        for channel in all_channels:
            if channel.get('name') == name:
                channel_id_to_get = channel.get('id')
        return channel_id_to_get

    @staticmethod
    def get_messages_from_channel(channel_id: str, limit: int = 10):
        user_client = SlackApiHelper.get_user_client()
        response = user_client.conversations_history(
            channel=channel_id,
            limit=limit
        )
        slack_messages = response.data.get('messages', [])
        return slack_messages
