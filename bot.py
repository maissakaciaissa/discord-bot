import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json
from datetime import datetime

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


bot.run(TOKEN)