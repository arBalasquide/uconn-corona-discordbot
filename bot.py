#!/usr/bin/env python3
import os
import discord
import uscrape
import asyncio
import subprocess

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

async def get():
    await client.wait_until_ready()
    guild = discord.utils.get(client.guilds, name=GUILD)
    channel = discord.utils.get(guild.channels, name="bot-test")

    while not client.is_closed():
        uscrape.get()
        if(uscrape.verify()):
            print("No new updates")
        else:
            subprocess.call(["cp", "new.txt", "stored.txt"]) 
            await channel.send("New updates : https://uconn.edu/public-notification/coronavirus/")
        await asyncio.sleep(3600)


@client.event
async def on_ready():
    print("Connection successful!")


client.loop.create_task(get())
client.run(TOKEN)
