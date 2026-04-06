# ✦ personalbot

A Discord bot built with Python — featuring news integration, chat moderation, announcements and more.

---

## ✦ Features

- `!hello` — greets the user
- `!news [category]` — fetches latest headlines from the news scraper (World, Technology, Culture, Fashion, Science)
- `!pin` — pins a message by replying to it
- `!clear [number]` — deletes X messages from the channel
- `!announce [message]` — sends a formatted announcement embed

---

## ✦ Tech Stack

- **Python 3**
- **discord.py** — Discord API wrapper
- **python-dotenv** — secure token management
- **json** — reads news data from news-scraper project

---

## ✦ Setup

**1. Clone the repository**

```bash
git clone https://github.com/maissakaciaissa/discord-bot.git
cd discord-bot
```

**2. Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create a `.env` file**

```
DISCORD_TOKEN=your_token_here
```

**5. Run the bot**

```bash
python bot.py
```

---

## ✦ Getting a Discord Bot Token

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Create a new application
3. Go to **Bot** tab
4. Copy your token and paste it in `.env`
5. Enable **Message Content Intent** under Privileged Gateway Intents
6. Invite the bot to your server via **OAuth2 → URL Generator**

---

## ✦ News Integration

This bot connects to the [news-scraper](https://github.com/maissakaciaissa/news-scraper) project.

To use `!news`, first run the news scraper to generate `news.json`, then update `NEWS_PATH` in `bot.py` to point to your local `news.json` file.

---

## ✦ Permissions Required

The bot needs these permissions on your server:

- Read Messages
- Send Messages
- Manage Messages (for `!clear` and `!pin`)
- Read Message History

---

## ✦ Project Structure

```
discord-bot/
│
├── bot.py           # Main bot code
├── .env             # Token (never push this!)
├── .gitignore       # Ignores venv, .env, pycache
└── requirements.txt # Dependencies
```

---

## 🐧 Linux / Mac Users

```bash
source venv/bin/activate
pip install -r requirements.txt
python bot.py
```
