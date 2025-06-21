from chalicelib.bots import get_bot


def send_scheduled_message(bot_id, text):
    """Send a message via the bot."""
    try:
        # Get the bot instance
        bot_instance = get_bot(bot_id=bot_id)
        if not bot_instance:
            print(f"Bot {bot_id} not found or not initialized.")
            return

        # Send the message
        bot_instance.sendMessage(text=text)
    except Exception as e:
        print(f"Error sending scheduled message for {bot_id}: {e}")
