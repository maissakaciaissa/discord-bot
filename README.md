# ✦ personalbot

A Discord bot built with Python — featuring weather, news integration, task tracking, chat moderation, announcements and more. Deployed 24/7 on Railway.

---

## ✦ Features

- `!hello` — greets the user
- `!flip` — flips a coin
- `!dice [sides]` — rolls a dice (default 6 sides)
- `!weather [city]` — gets live weather for any city
- `!news [category]` — fetches latest headlines from the news scraper (World, Technology, Culture, Fashion, Science)
- `!tasks` — shows today's to-do list from the todo-widget project
- `!pin` — pins a message by replying to it
- `!clear [number]` — deletes X messages from the channel
- `!announce [message]` — sends a formatted announcement embed
- Auto-welcome message when a new member joins the server

---

## ✦ Tech Stack

- **Python 3**
- **discord.py** — Discord API wrapper
- **aiohttp** — async HTTP requests for weather API
- **python-dotenv** — secure token management
- **OpenWeatherMap API** — live weather data
- **json** — reads news and task data from sister projects

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
WEATHER_API=your_openweathermap_key_here
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
5. Enable **Message Content Intent** and **Server Members Intent** under Privileged Gateway Intents
6. Invite the bot to your server via **OAuth2 → URL Generator**

---

## ✦ Getting a Weather API Key

1. Go to [openweathermap.org](https://openweathermap.org)
2. Sign up for a free account
3. Go to **API Keys** tab
4. Copy your key and paste it in `.env` as `WEATHER_API`

---

## ✦ Project Connections

This bot connects to two other projects:

- **[news-scraper](https://github.com/maissakaciaissa/news-scraper)** — run the scraper first to generate `news.json`, then update `NEWS_PATH` in `bot.py`
- **[todo-widget](https://github.com/maissakaciaissa/todo-widget)** — update `TASKS_PATH` in `bot.py` to point to your local `tasks.json`

---

## ✦ Deploying to Railway (24/7)

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) and sign in with GitHub
3. Create a new project → Deploy from GitHub repo
4. Add environment variables: `DISCORD_TOKEN` and `WEATHER_API`
5. Railway will auto-deploy and keep your bot online 24/7

---

## ✦ Permissions Required

- Read Messages
- Send Messages
- Manage Messages (for `!clear` and `!pin`)
- Read Message History
- Kick Members (optional, for moderation)

---

## ✦ Project Structure

```
discord-bot/
│
├── bot.py           # Main bot code
├── Procfile         # Railway deployment config
├── .env             # Tokens (never push this!)
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
