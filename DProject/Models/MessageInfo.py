import json


class MessageInfo():
    senderEmail = ""
    messageTitle = ""
    messageContent = ""

    def __init__(self, senderEmail, messageTitle, messageContent):
        self.senderEmail = senderEmail
        self.messageTitle = messageTitle
        self.messageContent = messageContent

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
