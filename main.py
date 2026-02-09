# This example requires the 'message_content' intent.

from IPython import embed
import discord

import requests # for howmanyspace
from dotenv import load_dotenv 
import os 
load_dotenv()

intents = discord.Intents.all()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "howmanyspace" or message.content == "hotmanspacemike":
        await message.channel.send('ts not implemented yet.')
    
    if message.channel.id == 11: #still needa find
        await message.delete() # to prevent spam and keep the channel bot only
        if message.content.startswith('?naping '): #startswith so we can see whats after it
            response = message.content[8:]  # Get the text after '?naping '
            embed = discord.Embed(title="NA PING",
                      description=f"{response}",
                      colour=0x00b0f4)

            embed.set_author(name=message.author.name,
                            icon_url=message.author.avatar.url)
            await message.channel.send(content=f"ping: <@&ROLEID>", embed=embed)
            
            



bot_token = os.getenv("DISCORD_BOT_TOKEN") # secure enough for a github repo
bot.run(bot_token)
