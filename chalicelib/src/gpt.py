import os

from openai import OpenAI


class Gpt:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.environ["gpt_key"])

    def call_chat(self, content):
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": content},
            ],
        )
        return chat_completion.choices[0].message.content

    def call_image(self, content):
        response = self.client.images.generate(prompt=content, n=1, size="1024x1024")
        print(dict(dict(response)["data"][0]))
        return dict(dict(response)["data"][0])["url"]
