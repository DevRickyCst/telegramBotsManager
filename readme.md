# Telegram Bot Handler with Chalice

This repository contains a Python script for handling Telegram bots using the Chalice framework. The script allows you to create and manage multiple Telegram bots effortlessly.

## Prerequisites
- Python 3.x
- Chalice framework
- Access to the Telegram Bot API

## Installation
1. Clone this repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt`.
3. Configure your Telegram bot(s) and obtain API tokens.
4. Set up your Chalice environment.

## Usage
1. Define your Telegram bots under the `chalicelib/bots` directory.
2. Each bot should be implemented as a separate Python module with a class named `Bot`.
3. Implement bot functionalities within the `Bot` class, inheriting from the `BotInterface` interface.
4. Start the Chalice server using `chalice local`.
5. Configure your Telegram bot webhook to point to your Chalice server.

## How It Works
- The `webhook_index` function serves as the entry point for handling incoming webhook requests from Telegram.
- When a message is received, it's processed by the `bot_handler` function, which dynamically imports the appropriate bot module based on the `bot_id`.
- The bot module is expected to have a `Bot` class with methods to handle different commands and messages.
- Incoming messages are routed to the corresponding bot's `handle_message_command_checker` method for processing.
- The `send_message` endpoint allows sending messages through a specific bot identified by `bot_id` and specified parameters.
- Other endpoints are provided for general functionality and testing.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License