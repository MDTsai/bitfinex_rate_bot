# Bitfinex Rate Bot
A Bitfinex lending rate notification bot for telegram. The bot will get funding history in last 5 minutes and get APY. If the APY is greater than a threshold, the bot will send notification to specific telegram channel.

## Prepare your telegram bot
1. Register a new bot on [BotFather](https://t.me/botfather)
2. Create a pubic telegram channel
3. Add your bot as administrator in the telegram channel

## Setup the program and run
1. Replace **TG_BOT_API** and **TG_CHAT_ID** with your bot API key and channel ID in **bitfinex_rate_bot.py**. Chat ID starts with **@**.
2. Run `pip install -r requirements.txt`
3. Run `python3 bitfinex_rate_bot.py`

Feel free to clone for your need. It's welcome to send PR for any request.