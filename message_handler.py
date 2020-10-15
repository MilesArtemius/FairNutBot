from importlib import import_module
from inspect import getmembers, isclass
import command
from vk_io import *

api = VkApi()


def get_answer(message):
    text = get_message_text(message).split()
    message, attachment = "", ""

    if text[0][0] == '/':
        try:
            module = import_module("commands." + text[0][1:])
            inst = command.Command()

            for name, obj in getmembers(module):
                if isclass(obj) and issubclass(obj, command.Command):
                    inst = obj()
                    break

            message, attachment = inst.process(text[1:])

        except ModuleNotFoundError:
            message = "There is no such command!\nType \"/help\" for extra info."

    return message, attachment


def handle(in_message):
    if answerable(in_message):
        out_message, attachment = get_answer(in_message["object"])
        if out_message != "":
            api.send_message(out_message, get_user_id(in_message), attachment)
