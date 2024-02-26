import discord
from discord.ext import commands
import music_commands

bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())

# Import and register music commands from music_commands.py
bot.add_command(music_commands.play_)
bot.add_command(music_commands.queue_)
bot.add_command(music_commands.skip_)
bot.add_command(music_commands.pause_)
bot.add_command(music_commands.resume_)
bot.add_command(music_commands.disconnect_)

# Add other music commands from music_commands.py as needed

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