import discord
import os
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='디스코드봇 대화중', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("재혁아! 안녕"):
        await client.send_message(message.channel, "안녕하세욧")

@client.event
async def on_message(message):
    if message.content.startswith("재혁아! 나간다"):
        await client.send_message(message.channel, "안녕히가세욧")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
