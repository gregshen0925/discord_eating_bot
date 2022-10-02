import string
import discord
import requests
import os
from FindRestaurant import *
from discord.ui import Button, View
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# client = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()
token=os.getenv('Discord_Token')

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('要吃什麼？')
    # online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('說'):
        print(message.created_at)
        tmp = message.content.split(" ", 2)
        if len(tmp) == 1:
            await message.channel.send("是要說什麼啦？",delete_after=3)
        else:
            await message.channel.send(tmp[1])
    if message.content.startswith('菜單'):
            await message.channel.send("抽到就去吃，看三小菜單？",delete_after=3)

    # channel = client.get_channel("channel id")
    # msg = await discord.utils.get(channel.history(), author__name=message)
    # print(msg)

    if message.content.startswith('吃') or message.content.startswith('甲')or message.content.startswith('呷')or message.content.startswith('eat')or message.content.startswith('宵夜'):
            
        result = findRestaurant()
        # print(result)
        embed = discord.Embed(
            title= result[0],
            url = result[4],
            colour= discord.Colour.blue()
        )
        embed.set_footer(text='\n Created by InJoy Labs')
        # embed.set_image(url='')

        embed.add_field(name='昂貴程度', value=result[1], inline=False)
        embed.add_field(name='評價', value=result[2], inline=False)
        embed.add_field(name='地址', value=result[3], inline=False)
        embed.add_field(name='菜單', value='請輸入「菜單」查詢', inline=False)


        await message.channel.send(embed=embed)

client.run(token)

