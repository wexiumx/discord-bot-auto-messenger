# discord-bot-auto-messenger

A small Discord bot built with `discord.py` that listens to messages in a server and replies automatically based on simple rules.

## Overview

This is my first project working with an external API, my first time building a bot, and my first time using environment variables (`.env`) to manage configuration and keep credentials out of source control. It was built to learn the fundamentals of the Discord API and event-driven programming with `discord.py`. The project is intentionally kept small in scope, though new response rules or small features may be added over time.

## Features

- Connects to Discord using the `discord.py` gateway client
- Listens for messages in any channel the bot has access to
- Sends an automatic reply when a message matches a defined rule
- Loads the bot token from an environment variable instead of hardcoding it

## Tech Stack

- Python 3
- [discord.py](https://github.com/Rapptz/discord.py)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Project Structure

```
discord-bot-auto-messenger/
├── main.py             Bot entry point: client setup, intents, and event handlers
├── requirements.txt    Python dependencies
├── .gitignore           Files and folders excluded from version control (.env, venv, etc.)
├── LICENSE              Project license (GPL-3.0)
└── README.md            Project documentation
```

## How It Works

The bot uses `discord.py`'s `Client` with the `message_content` intent enabled. On startup, `on_ready` confirms the bot has logged in. The `on_message` event handler checks incoming messages and sends a reply when the content matches a defined trigger, while ignoring messages sent by the bot itself to avoid responding to its own output.

## Setup

**1. Clone the repository**

```
git clone https://github.com/wexiumx/discord-bot-auto-messenger.git
cd discord-bot-auto-messenger
```

**2. Create and activate a virtual environment**

```
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```
pip install -r requirements.txt
```

**4. Configure the bot token**

Create a `.env` file in the project root:

```
TOKEN=your_discord_bot_token
```

**5. Run the bot**

```
python main.py
```

## Discord Developer Portal Requirements

- A bot application created at the [Discord Developer Portal](https://discord.com/developers/applications)
- The **Message Content Intent** enabled under the application's Bot settings
- The bot invited to a server with permission to read and send messages

## Author

Buit by wexiumx & Nortshift
