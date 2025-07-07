import discord
import os
import requests
from dotenv import load_dotenv
from memory import add_to_memory, get_memory

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Load personality prompt
with open("personality.txt", "r", encoding="utf-8") as f:
    BOT_PERSONALITY_PROMPT = f.read()

# Set intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize Pycord Bot
bot = discord.Bot(intents=intents)


# Gemini API call
def call_gemini(user_message: str, memory: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    full_message = f"{BOT_PERSONALITY_PROMPT}\n\nPast context:\n{memory}\n\nUser: {user_message}"

    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": full_message}
                ]
            }
        ]
    }

    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 200:
        response_json = resp.json()
        reply_text = response_json.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return reply_text if reply_text.strip() else "…"
    else:
        print(f"Gemini API error: {resp.status_code} - {resp.text}")
        return "I am silent… something went wrong."


# Events & Commands
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}!")
    try:
        await bot.sync_commands(force=True)
        print(f"✅ Synced global slash commands with Discord.")
    except Exception as e:
        print(f"⚠️ Failed to sync commands: {e}")


@bot.slash_command(name="ask", description="Ask Phlio anything.")
async def ask(ctx, *, question: str):
    await ctx.defer()
    user_id = ctx.author.id
    add_to_memory(user_id, f"Ask: {question}")
    memory = get_memory(user_id)
    reply = call_gemini(question, memory)
    add_to_memory(user_id, f"Philo: {reply}")
    await ctx.respond(reply)


@bot.slash_command(name="quote", description="Ask Philo for a quote.")
async def quote(ctx):
    await ctx.defer()
    user_id = ctx.author.id
    add_to_memory(user_id, "Quote requested")
    memory = get_memory(user_id)
    reply = call_gemini("Give me a meaningful quote.", memory)
    add_to_memory(user_id, f"Philo: {reply}")
    await ctx.respond(reply)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user and (bot.user in message.mentions or isinstance(message.channel, discord.DMChannel)):
        user_id = message.author.id
        add_to_memory(user_id, f"You: {message.content}")
        memory = get_memory(user_id)
        reply = call_gemini(message.content, memory)
        add_to_memory(user_id, f"Philo: {reply}")
        await message.channel.send(reply)

    await bot.process_application_commands(message)


if not DISCORD_TOKEN:
    raise ValueError("🚨 DISCORD_TOKEN is missing. Check your .env file and make sure it contains DISCORD_TOKEN.")

bot.run(DISCORD_TOKEN)
