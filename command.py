class Command:
    def __init__(self, vk):
        self.description = ""
        self.api = vk

    def process(self, args, message):
        return "", ""
