# Discord Bot

A simple Discord bot built with discord.py featuring basic commands.

## Features

- `!ping` - Check bot latency
- `!hello` - Get a friendly greeting
- `!serverinfo` - Display server information
- `!help` - Show all available commands (built-in)

## Setup

### Prerequisites

- Python 3.8 or higher
- A Discord bot token ([How to get one](https://discord.com/developers/applications))

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd discord-bot-project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create your `.env` file:
   ```bash
   cp .env.example .env
   ```

5. Edit `.env` and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_actual_token_here
   ```

### Discord Developer Portal Setup

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section and create a bot
4. Copy the bot token and add it to your `.env` file
5. Enable these Privileged Gateway Intents:
   - Message Content Intent
   - Server Members Intent
6. Go to OAuth2 > URL Generator
7. Select scopes: `bot`
8. Select bot permissions: `Send Messages`, `Read Message History`, `Embed Links`
9. Use the generated URL to invite the bot to your server

## Running the Bot

```bash
python bot.py
```

## Project Structure

```
discord-bot-project/
├── bot.py              # Main bot file
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .env                # Your actual environment variables (not in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## License

MIT
