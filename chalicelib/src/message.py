import re

class Message:
    """
    A class representing a Message.

    Attributes:
        user (dict): id, is_bot, first_name, username, langage_code.
        chat (dict): id, first_name, username, type
        date (str)
        input (dict): isCommand, command, text
    """

    def __init__(self, json_body):
        self.user = self.get_user_from_request(json_body)
        self.chat = self.get_chat_from_request(json_body)
        self.date = self.get_date_from_request(json_body)
        self.input = self.get_input_from_request(json_body)

    def __str__(self):
        return str({
            'user': self.user,
            'chat': self.chat,
            'date': self.date,
            'input': self.input
        })
    @staticmethod
    def get_user_from_request(json_body: dict):
        user = json_body["message"]["from"]
        return {
            "id": user["id"],
            "is_bot": user["is_bot"],
            "first_name": user["first_name"],
            "username": user["username"],
            "language_code": user["language_code"],
        }

    @staticmethod
    def get_chat_from_request(json_body: dict):
        user = json_body["message"]["chat"]
        return {
            "id": user["id"],
            "first_name": user["first_name"],
            "username": user["username"],
            "type": user["type"],
        }

    @staticmethod
    def get_date_from_request(json_body: dict):
        return json_body["message"]["date"]

    @staticmethod
    def get_input_from_request(json_body: dict):
        isCommand = False
        command = None
        text = json_body["message"]["text"]
        # Use regex to check if a command was passed
        regex_command = re.search(r'/(\w+)', text)
        if regex_command:
            isCommand = True
            command = regex_command.group(1)
            # Delete command from texte
            text = re.sub(fr'/{re.escape(command)}\s*','',text)
        return {
            'isCommand': isCommand,
            'command': command,
            'text': text
        }
