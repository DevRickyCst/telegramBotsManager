import openai
from chalicelib.utils.secret import get_secret


class Gpt:
    def __init__(self) -> None:
        # Récupération de la clé API depuis AWS Secrets Manager
        api_key = get_secret("api_keys", 'gpt')

        # Configuration de la clé API OpenAI globalement
        openai.api_key = api_key

    def call_chat(self, content):
        """
        Appelle le modèle GPT-3.5 pour générer une réponse au contenu donné.
        """
        try:
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": content},
                ],
            )
            return chat_completion.choices[0].message["content"]
        except Exception as e:
            print(f"Error in call_chat: {e}")
            return None

    def call_image(self, content):
        """
        Génère une image basée sur un prompt donné en utilisant OpenAI DALL-E.
        """
        try:
            response = openai.Image.create(prompt=content, n=1, size="1024x1024")
            return response['data'][0]['url']
        except Exception as e:
            print(f"Error in call_image: {e}")
            return None
