import slack
from typing import List

from config import config
from SlackApiHelper import SlackApiHelper

bot_client = SlackApiHelper.get_bot_client()
user_client = SlackApiHelper.get_user_client()

channel_name_to_get = 'general'
channel_id_to_get = None


channels = SlackApiHelper.get_channels()
channel_id = SlackApiHelper.find_channel_id_from_name(channel_name_to_get, channels)
slack_messages = SlackApiHelper.get_messages_from_channel(channel_id, limit=100)

messages_text = [x.get('text', '') for x in slack_messages]

print(messages_text.reverse())
