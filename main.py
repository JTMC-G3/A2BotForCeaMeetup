# This example requires the 'message_content' intent.
# base bot model from the discord.py quickstart (actually logging in), the rest by me (the dotenv loading, the commands, etc)

from IPython import embed
import discord

import requests # for howmanyspace
from dotenv import load_dotenv 
import os 
import getfleetsyay
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

    if message.author.id == 1173257623055913072: # blob cat laugh hahah
        await message.add_reaction("😹")
        
    if message.content == "howmanyspace" or message.content == "hotmanspacemike":
        getfleetsyay.getfleetsyay()
        playercount = getfleetsyay.getdeploymentinfo("EA Calibration_22")
        finalplayercount = playercount['player_count']
        finalcl = playercount['deployment_cl']
        await message.channel.send(f'```\n+----------------+-------+----+\n| EA Calibration 22 | {finalcl} | {finalplayercount} |\n+----------------+-------+----+```')
    
    if message.channel.id == 1470544517248585788: #still needa find
        await message.delete() # to prevent spam and keep the channel bot only
        if message.content.startswith('?naping '): #startswith so we can see whats after it
            response = message.content[8:]  # Get the text after '?naping '
            embed = discord.Embed(title="NA PING",
                      description=f"{response}",
                      colour=discord.Colour.random())

            embed.set_author(name=message.author.name,
                            icon_url=message.author.avatar.url)
            await message.channel.send(content=f"<@&1470549172552994887>", embed=embed)
            
            



bot_token = os.getenv("DISCORD_BOT_TOKEN") # secure enough for a github repo
bot.run(bot_token)
