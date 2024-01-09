class Message:
    """
    A class representing a Message.

    Attributes:
        user (dict): id, is_bot, first_name, username, langage_code.
        chat (dict): id, first_name, username, type
        date (str)
        text (str)
    """

    def __init__(self, json_body):
        self.user = self.get_user_from_request(json_body)
        self.chat = self.get_chat_from_request(json_body)
        self.date = self.get_date_from_request(json_body)
        self.text = self.get_text_from_request(json_body)

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
        date = json_body["message"]["date"]
        return date

    @staticmethod
    def get_text_from_request(json_body: dict):
        text = json_body["message"]["text"]
        return text
