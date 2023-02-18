import asyncio
from discord.ext import commands, tasks
from datetime import timedelta, datetime

token = 'YOUR_DISCORD_TOKEN' # click F12 to get your user token, make sure keep your token safe if you run on cloud
client = commands.Bot(command_prefix='}')
client._skip_check = lambda x, y: False

@client.event
async def on_ready():
    print(f'logged in as {client.user}')
    
@tasks.loop(seconds=0.2)
async def get_channel_history():
    await asyncio.sleep(5)
    await client.wait_until_ready()
    print('system ready')
    channel = client.get_channel(966538208315850873) # your channel id

    # startTime = str(input('input start time e.g. 2022101317 :'))
    # endTime = str(input('input end time:'))
    
    startTime = datetime.strptime(startTime, "%Y%m%d%H")
    endTime = datetime.strptime(endTime, "%Y%m%d%H")
    

    async for message in channel.history(limit=9999):
        try:
            # if message.created_at + timedelta(hours=8) > startTime and message.author.id == 926980148169965599 and '?' in message.content:
            # PUT YOUR CODE HERE
            pass
        except:
            pass

    print('done')
    await asyncio.sleep(999999)

get_channel_history.start()

client.run(token, bot=False)