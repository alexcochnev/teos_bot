import discord
from datetime import datetime, timedelta
import re


def time_proc(message):
    dt = re.search(r'\b[0-2]?\d:[0-5]\d\b', message)
    if type(dt) == re.Match:
        dt = datetime.strptime(dt.group(), '%H:%M')
    else:
        dt = datetime.now()
    min_kanos = dt + timedelta(hours=8)
    max_kanos = dt + timedelta(hours=24)
    min_cent = dt + timedelta(hours=11)
    max_cent = dt + timedelta(hours=13)
    return {'die': dt.strftime('%H:%M'),
            'min_kanos': min_kanos.strftime('%H:%M'), 'max_kanos': max_kanos.strftime('%H:%M'),
            'min_cent': min_cent.strftime('%H:%M'), 'max_cent': max_cent.strftime('%H:%M')}


DISCORD_BOT_TOKEN = 'ODM5MDkyMzAzNjQ4OTE1NDc2.YJEnmg.o78O95FIlIJoI2HhG2u5lFcyXmg'
resp = {'ales': ['Алес', '🤷‍♀️', '🤷‍♀️'], 'lumen': ['Люма', '🤷‍♀️', '🤷‍♀️'], 'tanya': ['Таня', '🤷‍♀️', '🤷‍♀️'],
        'dent': ['Дент', '🤷‍♀️', '🤷‍♀️'], 'cent': ['Цент', '🤷‍♀️', '🤷‍♀️']}
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # if not message.content.startswith('!'):
    #     return

    # Алес
    if message.content.lower().startswith('!алес'):
        tp = time_proc(message.content)
        resp['ales'] = ['Алес', tp['min_kanos'], tp['max_kanos']]
        await message.channel.send(f"🌪 Алес {tp['die']} --- {tp['min_kanos']}")

    # Люма
    elif message.content.lower().startswith(('!люма', '!люмен')):
        tp = time_proc(message.content)
        resp['lumen'] = ['Люма', tp['min_kanos'], tp['max_kanos']]
        await message.channel.send(f"🔥 Люма {tp['die']} --- {tp['min_kanos']}")

    # Дент
    elif message.content.lower().startswith('!дент'):
        tp = time_proc(message.content)
        resp['dent'] = ['Дент', tp['min_kanos'], tp['max_kanos']]
        await message.channel.send(f"🌿 Дент {tp['die']} --- {tp['min_kanos']}")

    # Таня
    elif message.content.lower().startswith(('!таня', '!тайнор')):
        tp = time_proc(message.content)
        resp['tanya'] = ['Таня', tp['min_kanos'], tp['max_kanos']]
        await message.channel.send(f"🌊 Таня {tp['die']} --- {tp['min_kanos']}")

    # Цент
    elif message.content.lower().startswith('!цент'):
        tp = time_proc(message.content)
        resp['cent'] = ['Цент', tp['min_cent'], tp['max_cent']]
        await message.channel.send(f"🐓 Цент {tp['die']} --- {tp['min_cent']}")

    # Инфо о рб
    elif message.content.lower().startswith('!рб'):
        await message.channel.send(f'''
🌪 {resp['ales'][0]}:    Мини {resp['ales'][1]} --- Макси {resp['ales'][2]}
🔥 {resp['lumen'][0]}:  Мини {resp['lumen'][1]} --- Макси {resp['lumen'][2]}
🌿 {resp['dent'][0]}:    Мини {resp['dent'][1]} --- Макси {resp['dent'][2]}
🌊 {resp['tanya'][0]}:    Мини {resp['tanya'][1]} --- Макси {resp['tanya'][2]}
🐓 {resp['cent'][0]}:    Мини {resp['cent'][1]} --- Макси {resp['cent'][2]}
        ''')

    # Релог
    elif message.content.lower().startswith('!релог'):
        tp = time_proc(message.content)
        resp['ales'] = ['Алес', tp['min_kanos'], tp['max_kanos']]
        resp['lumen'] = ['Люма', tp['min_kanos'], tp['max_kanos']]
        resp['dent'] = ['Дент', tp['min_kanos'], tp['max_kanos']]
        resp['tanya'] = ['Таня', tp['min_kanos'], tp['max_kanos']]
        resp['cent'] = ['Цент', '🤷‍♀️', '🤷‍♀️']
        await message.channel.send(f'''
🌪 {resp['ales'][0]}:    Мини {resp['ales'][1]} --- Макси {resp['ales'][2]}
🔥 {resp['lumen'][0]}:  Мини {resp['lumen'][1]} --- Макси {resp['lumen'][2]}
🌿 {resp['dent'][0]}:    Мини {resp['dent'][1]} --- Макси {resp['dent'][2]}
🌊 {resp['tanya'][0]}:    Мини {resp['tanya'][1]} --- Макси {resp['tanya'][2]}
🐓 {resp['cent'][0]}:    Мини {resp['cent'][1]} --- Макси {resp['cent'][2]}
        ''')

client.run(DISCORD_BOT_TOKEN)
