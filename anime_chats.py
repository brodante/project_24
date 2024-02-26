import discord
from discord.ext import commands
import os
import traceback

import googlesearch
from chatbot import Chatbot

bot = commands.Bot(command_prefix='!')
chatbot = Chatbot(model_folder='model')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def chat(ctx, *, question):
    """Ask the bot a question"""

    try:
        answer = chatbot.get_answer(question)
        if answer:
            await ctx.send(answer)
        else:
            await ctx.send("I don't know.")
    except Exception as e:
        await ctx.send(f"I don't know. {e}")


@chat.error
async def chat_error(ctx, error):
    await ctx.send('Something went wrong.')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'ara ara @TheAnimeBot':
        await message.channel.send(f'Sayonara {message.author.mention}')

    if "ara ara" in message.content and 'TheAnimeBot' in message.content:
        await message.channel.send(f'Sayonara {message.author.mention}')

    if 'TheAnimeBot' in message.content and 'where is' in message.content:
        words = message.content.split()
        if len(words) > 3:
            location = ' '.join(words[3:])
            gsearch = googlesearch.search
            results = [i for i in gsearch(f"where is {location}", tld="co.in", num=1, stop=1, pause=2)]
            if results:
                await message.channel.send(results[0])

    await bot.process_commands(message)


with open("token.txt") as file:
    token=file.read()

bot.run(token)