import discord
from datetime import datetime, timedelta, timezone
import re
import random
import time
from itertools import cycle

DISCORD_BOT_TOKEN = 'ODM5MDkyMzAzNjQ4OTE1NDc2.YJEnmg.o78O95FIlIJoI2HhG2u5lFcyXmg'
fatal = [discord.Colour.from_rgb(255, 7, 11), discord.Colour.from_rgb(0, 125, 255)]
kurazh = [discord.Colour.from_rgb(254, 39, 18),
          discord.Colour.from_rgb(253, 58, 15),
          discord.Colour.from_rgb(253, 77, 12),
          discord.Colour.from_rgb(252, 96, 10),
          discord.Colour.from_rgb(252, 115, 7),
          discord.Colour.from_rgb(251, 134, 4),
          discord.Colour.from_rgb(251, 153, 2),
          discord.Colour.from_rgb(251, 169, 10),
          discord.Colour.from_rgb(252, 186, 18),
          discord.Colour.from_rgb(252, 203, 26),
          discord.Colour.from_rgb(253, 220, 34),
          discord.Colour.from_rgb(253, 237, 42),
          discord.Colour.from_rgb(254, 254, 51),
          discord.Colour.from_rgb(228, 241, 50),
          discord.Colour.from_rgb(203, 228, 50),
          discord.Colour.from_rgb(178, 215, 50),
          discord.Colour.from_rgb(152, 202, 50),
          discord.Colour.from_rgb(127, 189, 50),
          discord.Colour.from_rgb(102, 175, 49),
          discord.Colour.from_rgb(85, 158, 84),
          discord.Colour.from_rgb(68, 141, 118),
          discord.Colour.from_rgb(52, 123, 152),
          discord.Colour.from_rgb(35, 106, 185),
          discord.Colour.from_rgb(18, 88, 220),
          discord.Colour.from_rgb(2, 71, 254),
          discord.Colour.from_rgb(24, 59, 240),
          discord.Colour.from_rgb(46, 47, 227),
          discord.Colour.from_rgb(68, 36, 214),
          discord.Colour.from_rgb(90, 24, 201),
          discord.Colour.from_rgb(112, 12, 188),
          discord.Colour.from_rgb(134, 1, 175),
          discord.Colour.from_rgb(154, 7, 148),
          discord.Colour.from_rgb(174, 13, 122),
          discord.Colour.from_rgb(194, 20, 96),
          discord.Colour.from_rgb(214, 26, 70),
          discord.Colour.from_rgb(234, 32, 44)]

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    server = client.get_guild(542043319979737100)
    role = server.get_role(609401697948795057)
    # await role.edit(colour=discord.Colour.from_rgb(255, 7, 11))
    await role.edit(name='Фаталити')
    print('111')
    # for color in cycle(kurazh):
    #     time.sleep(1)
    #     await role.edit(colour=color)


client.run(DISCORD_BOT_TOKEN)
