# 14. Automate Slack Notifications
from slack_sdk import WebClient



def send_slack_message(token, channel, text):
    client = WebClient(token=token)
    client.chat_postMessage(channel=channel, text=text)
