
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import random 
import aiohttp

NEWS_PATH = r"C:\side-projects\news-scraper\news.json"

# load token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# set up intents
intents = discord.Intents.default()
intents.message_content = True

# create bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✦ {bot.user} is online!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}! ✦")

@bot.command()
async def pin(ctx):
    if ctx.message.reference:
        msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await msg.pin()
        await ctx.send(f"✦ message pinned!")
    else:
        await ctx.send("reply to a message to pin it!")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"✦ cleared {amount} messages!", delete_after=3)

@bot.command()
async def announce(ctx, *, message):
    embed = discord.Embed(
        description=message,
        color=discord.Color.dark_red()
    )
    embed.set_footer(text=f"announced by {ctx.author.name}")
    await ctx.message.delete()
    await ctx.send(embed=embed)



@bot.command()
async def news(ctx, category=None):
    try:
        with open(NEWS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        await ctx.send("✦ no news found! run the scraper first.")
        return
    
    articles = data["articles"]
    
    # filter by category if provided
    if category:
        articles = [a for a in articles if a["category"].lower() == category.lower()]
    
    if not articles:
        await ctx.send(f"✦ no articles found for category: {category}")
        return
    
    # send top 5 articles
    articles = articles[:5]
    
    embed = discord.Embed(
        title="✦ daily news",
        description=f"scraped at {data['scraped_at']}",
        color=discord.Color.dark_red()
    )
    
    for article in articles:
        embed.add_field(
            name=f"[{article['category']}] {article['headline']}",
            value=article['description'] if article['description'] else "no description",
            inline=False
        )
    
    embed.set_footer(text="use !news [category] to filter — World, Technology, Culture, Fashion, Science")
    await ctx.send(embed=embed)

# ── Flip & Dice ──────────────────────────
@bot.command()
async def flip(ctx):
    result = random.choice(["heads", "tails"])
    embed = discord.Embed(
        title="🪙 coin flip",
        description=f"it's **{result}**!",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)
@bot.command()
async def dice(ctx, sides: int = 6):
    result = random.randint(1, sides)
    embed = discord.Embed(
        title=f"🎲 d{sides} roll",
        description=f"you rolled **{result}**!",
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)


# ── Weather ──────────────────────────────
@bot.command()
async def weather(ctx, *, city):  
    api_key = os.getenv("WEATHER_API")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                 print(f"Status: {response.status}, City: {city}")
                 data_text = await response.text()
                 print(data_text)
                 await ctx.send(f"✦ couldn't find weather for **{city}**")
                 return
            data = await response.json()
    
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    
    embed = discord.Embed(
        title=f"🌤 weather in {city.title()}",
        color=discord.Color.teal()
    )
    embed.add_field(name="temperature", value=f"{temp}°C", inline=True)
    embed.add_field(name="feels like", value=f"{feels}°C", inline=True)
    embed.add_field(name="humidity", value=f"{humidity}%", inline=True)
    embed.add_field(name="condition", value=desc, inline=False)
   
    await ctx.send(embed=embed)


# ── Tasks ────────────────────────────────
TASKS_PATH = r"C:\side-projects\todo-widget\tasks.json" 



@bot.command()
async def tasks(ctx):
    try:
        with open(TASKS_PATH, "r", encoding="utf-8") as f:
            all_tasks = json.load(f)
    except FileNotFoundError:
        await ctx.send("✦ no tasks found!")
        return
    
    from datetime import date
    today = str(date.today())
    today_tasks = [t for t in all_tasks if t["date"] == today]
    
    if not today_tasks:
        await ctx.send("✦ no tasks for today!")
        return
    
    embed = discord.Embed(
        title="✦ today's tasks",
        color=discord.Color.dark_red()
    )
    
    for task in today_tasks:
        status = "~~" if task["done"] else ""
        embed.add_field(
            name=f"{'✅' if task['done'] else '⬜'} {status}{task['text']}{status}",
            value="\u200b",
            inline=False
        )
    
    done = sum(1 for t in today_tasks if t["done"])
    embed.set_footer(text=f"{done}/{len(today_tasks)} completed")
    await ctx.send(embed=embed)

# ── Welcome ──────────────────────────────
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        embed = discord.Embed(
            title=f"✦ welcome {member.name}!",
            description=f"glad to have you here {member.mention} 🌹",
            color=discord.Color.dark_red()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        await channel.send(embed=embed)


bot.run(TOKEN)