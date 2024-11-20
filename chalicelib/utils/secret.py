import json

import boto3


def get_secret(secret: str, bot_id: str) -> str:
    """
    Retrieve the secret from AWS Secrets Manager.

    :param secret_name: The name of the secret in AWS Secrets Manager.
    :return: The secret value as a string.
    """
    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name="eu-central-1")

    try:
        response = client.get_secret_value(SecretId=secret)

        # Secrets Manager can return the secret as a JSON string or plaintext
        if "SecretString" in response:
            secret = response["SecretString"]
        else:
            secret = response["SecretBinary"].decode("utf-8")

        # If the secret is JSON, parse it to extract the required key
        try:
            secret_dict = json.loads(secret)
            print(secret_dict.get(bot_id))
            return secret_dict.get(
                bot_id
            )  # Adjust key name based on your stored format
        except json.JSONDecodeError:
            return secret  # Return as is if it's not JSON

    except Exception as e:
        raise RuntimeError(f"Error retrieving secret '{secret}': {e}")
