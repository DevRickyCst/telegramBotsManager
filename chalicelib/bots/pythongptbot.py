from chalicelib.src.gpt import Gpt
from chalicelib.src.message import Message
from chalicelib.src.telegram import TelegramInterface

gpt = Gpt(api_key=os.environ["gpt_key"])


def handle_message(msg: Message, telegram: TelegramInterface):
    response = gpt.call_image(msg.text)
    telegram.sendImage(response, chat_id=msg.chat["id"])
