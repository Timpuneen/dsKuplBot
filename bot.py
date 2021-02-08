import discord
from discord import utils
from discord.ext import commands
import asyncio
from kuplParse import kuplinov

import datetime
import config

sg = kuplinov()
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    await client.change_presence(status=discord.Status.online,activity=discord.Game('minecraft'))

@client.command(pass_context = True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount+1)    
 
async def postTest(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        new_videos = sg.new_games()
        now = datetime.datetime.now()
        if(new_videos and now.hour == 17):
            new_videos.reverse()
            for ng in new_videos:
                try:
                    await client.get_channel(config.Post_Channel).send("Новый видосик у Куплинова: \n"+'https://www.youtube.com/watch?v='+ng)
                except Exception as error:
                    print(error)                

# RUN
loop = asyncio.get_event_loop()
loop.create_task(postTest(3600))
client.run(config.TOKEN+ 'HxdA')
