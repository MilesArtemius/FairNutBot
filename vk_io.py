import vk
import sys
from random import randint

confirmation_token = "x"
access_token = "y"


def answerable(message):
    return message["object"]["from_id"] > 0


def get_message_text(message):
    return message["object"]["text"]


def get_user_id(message):
    return message["object"]["peer_id"]


class VkApi:
    def __init__(self):
        super().__init__()
        self.session = vk.Session(access_token)
        self.api = vk.API(self.session, v=5.95)

    def send_message(self, message, user_id, attachment=""):
        self.api.messages.send(access_token=access_token,
                               peer_id=str(user_id),
                               random_id=randint(0, sys.maxsize),
                               message=message,
                               attachment=attachment)
