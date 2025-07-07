# Philo — A Pycord Discord Bot



Philo is a Discord bot with a deeply human, tragic, and comforting personality — designed to serve as a quiet, philosophical guide for your server. Built using **Pycord** (a maintained fork of discord.py), Philo integrates with Google Gemini to deliver meaningful, melancholic yet hopeful responses to your questions.

> *“I am no one — just a scar the world could not erase.”*

---

## 🌑 Features

✅ Responds to direct mentions and DMs in its unique tone.

✅ `/quote` — Receive a profound, comforting quote from the bot.

✅ `/ask` — Ask a question to the bot.

✅ Memory system to maintain context per user.

✅ Personality rooted in existential resignation yet kindness, configured via `personality.txt`.

✅ Deployed with Pycord's native slash commands.

---

## 📄 Commands

| Command       | Description                                   |
| ------------- | --------------------------------------------- |
| `/ask`        | Ask the bot any kind of question.             |
| `/quote`      | Get a meaningful, comforting quote.           |
| Mention or DM | This bot replies directly in DM too.          |

---

## 🛠️ Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AaYuSh11233/py-cord-bot.git
cd py-cord-bot
```

### 2️⃣ Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3️⃣ Create `.env`

```env
DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4️⃣ Configure `personality.txt`

Edit the included `personality.txt` to adjust Your own tone.

---

## 🚀 Run

```bash
python philo.py
```

✅ The bot will log in and sync slash commands.\
✅ You can now invite it to your server and type `/` to see commands.

---

## 🌌 Future Ideas

- Integrate vector database for long-term memory
- Add sentiment analysis for emotional awareness
- Fine-tune your own LLM for truly personalized replies

---

## 🤝 Contributing

PRs are welcome! Open an issue or submit a pull request if you’d like to contribute.

---
