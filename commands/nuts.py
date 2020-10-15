import flask

from command import Command


class NutCommand(Command):
    def __init__(self, vk):
        super().__init__(vk)
        self.description = "Counts fair nuts of given type:\n\t[] - regular nut\n\t[dog] - dog nut\n\t[seal] - seal nut"

    def process(self, args, message):
        return self.nut(args, message)

    def nut(self, text, message):
        param = ""
        if len(text) > 0:
            param = text[0]
        if param == "":
            return self.count_messages(message["peer_id"], 0, 4, 163)
        elif param == "dog":
            return self.count_messages(message["peer_id"], 0, 594, 21375)
        elif param == "seal":
            return self.count_messages(message["peer_id"], 0, 505, 17842)

    def count_messages(self, peer_id, offset, product_id, sticker_id):
        def search(msg):
            if msg["attachments"] > 0 and msg["attachments"][0]["type"] == "sticker":
                sticker = msg["attachments"][0]["sticker"]
                return sticker["product_id"] == product_id and sticker["sticker_id"] == sticker_id
            else:
                return False

        mes = flask.json.loads(self.api.method("messages.getConversations", {"offset": offset, "count": 200}))
        nuts = 0
        count = mes["count"]
        if count == 0:
            return nuts

        for message in mes["items"]:
            if search(message):
                nuts += 1

        if offset + 200 < count:
            nuts += self.count_messages(peer_id, offset + 200, product_id, sticker_id)

        return nuts
