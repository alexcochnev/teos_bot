import discord

DISCORD_BOT_TOKEN = 'ODM5MDkyMzAzNjQ4OTE1NDc2.YJEnmg.o78O95FIlIJoI2HhG2u5lFcyXmg'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        print('Щас скажет, что он пидр')
        await message.channel.send('Ты пидр')

client.run(DISCORD_BOT_TOKEN)
