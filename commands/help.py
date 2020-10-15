import pathlib
from importlib import import_module
from inspect import getmembers, isclass
from os import listdir

from command import Command


class HelpCommand(Command):
    def __init__(self, vk):
        super().__init__(vk)
        self.description = "Shows all commands descriptions"

    def process(self, args, message):
        message = ""
        files = listdir(pathlib.Path(__file__).parent.absolute())
        modules = filter(lambda x: not x == "__init__.py" and x.endswith(".py"), files)
        for m in modules:
            mod = import_module("commands." + m[0:-3])
            inst = Command(self.api)

            for name, obj in getmembers(mod):
                if isclass(obj) and issubclass(obj, Command):
                    inst = obj(self.api)
                    break
            message += '/' + m[0:-3] + " - " + inst.description + '\n'

        return message, ""
