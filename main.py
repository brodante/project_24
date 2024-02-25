import inspect
from colorama import Style
import discord
from discord.ext import commands
from discord import Interaction

bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())

import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

# Rest of your code goes here

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def hello(ctx):
    """Says hello or something"""
    # Responds in the console that the command has been run
    print(f"> {ctx.author} used the command.")

    # Then responds in the channel with this message
    await ctx.send(f"Hi {ctx.author.mention}, thank you for saying hello to me.")

with open("token.txt") as file:
    token=file.read()

bot.run(token)