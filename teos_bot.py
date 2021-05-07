import discord
from datetime import datetime, timedelta, timezone
import re

DISCORD_BOT_TOKEN = 'ODM5MDkyMzAzNjQ4OTE1NDc2.YJEnmg.o78O95FIlIJoI2HhG2u5lFcyXmg'
# DISCORD_BOT_TOKEN = 'ODM5NDYxODEzMjkyNjMwMDM4.YJJ_vA.IEnOxbcX6hkfRhcOAqFwbEQVBBw'  # тестовый бот

resp = {'ales': ['Алес', '🤷‍♀️', '🤷‍♀️'], 'lumen': ['Люма', '🤷‍♀️', '🤷‍♀️'], 'tanya': ['Таня', '🤷‍♀️', '🤷‍♀️'],
        'dent': ['Дент', '🤷‍♀️', '🤷‍♀️'], 'cent': ['Цент', '🤷‍♀️', '🤷‍♀️']}
date_string = '%d.%m %H:%M'

client = discord.Client()


def table():
    return f'''
🌪 {resp['ales'][0]}:    Мини {resp['ales'][1]} --- Макси {resp['ales'][2]}
🔥 {resp['lumen'][0]}:  Мини {resp['lumen'][1]} --- Макси {resp['lumen'][2]}
🌿 {resp['dent'][0]}:    Мини {resp['dent'][1]} --- Макси {resp['dent'][2]}
🌊 {resp['tanya'][0]}:    Мини {resp['tanya'][1]} --- Макси {resp['tanya'][2]}
🐓 {resp['cent'][0]}:    Мини {resp['cent'][1]} --- Макси {resp['cent'][2]}
        '''


def time_proc(message):
    dt = re.search(r'\b[0-2]?\d:[0-5]\d\b', message)
    if type(dt) == re.Match:
        if message.find('вчера') != -1:
            dt = datetime.strptime(
                f"{(datetime.now(tz=timezone(timedelta(hours=3))) - timedelta(1)).strftime('%d.%m')} {dt.group()}",
                date_string)
        else:
            dt = datetime.strptime(f"{datetime.now(tz=timezone(timedelta(hours=3))).strftime('%d.%m')} {dt.group()}",
                                   date_string)
    else:
        dt = datetime.now(tz=timezone(timedelta(hours=3)))
    min_kanos = dt + timedelta(hours=8)
    max_kanos = dt + timedelta(hours=24)
    min_cent = dt + timedelta(hours=11)
    max_cent = dt + timedelta(hours=13)
    return {'die': dt.strftime(date_string),
            'min_kanos': min_kanos.strftime(date_string), 'max_kanos': max_kanos.strftime(date_string),
            'min_cent': min_cent.strftime(date_string), 'max_cent': max_cent.strftime(date_string)}


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global resp_channel
    for channel in client.get_all_channels():
        if channel.name == '⏳респы':
            resp_channel = channel


@client.event
async def on_message(message):
    # if not message.content.startswith('!'):
    #     return
    if message.author == client.user:
        return

    # Алес
    if message.content.lower().startswith(('!алес', '!fktc')):
        tp = time_proc(message.content)
        resp['ales'] = ['Алес', tp['min_kanos'], tp['max_kanos']]
        if message.content.find('тест') == -1:
            await resp_channel.send(f"🌪 Алес {tp['die']} --- {tp['min_kanos']}   (записал {message.author.display_name})")
        await message.delete()

    # Люма
    elif message.content.lower().startswith(('!люма', '!люмен', '!k.vf')):
        tp = time_proc(message.content)
        resp['lumen'] = ['Люма', tp['min_kanos'], tp['max_kanos']]
        if message.content.find('тест') == -1:
            await resp_channel.send(f"🔥 Люма {tp['die']} --- {tp['min_kanos']}   (записал {message.author.display_name})")
        await message.delete()

    # Дент
    elif message.content.lower().startswith(('!дент', '!ltyn')):
        tp = time_proc(message.content)
        resp['dent'] = ['Дент', tp['min_kanos'], tp['max_kanos']]
        if message.content.find('тест') == -1:
            await resp_channel.send(f"🌿 Дент {tp['die']} --- {tp['min_kanos']}   (записал {message.author.display_name})")
        await message.delete()

    # Таня
    elif message.content.lower().startswith(('!таня', '!тайнор', '!nfyz')):
        tp = time_proc(message.content)
        resp['tanya'] = ['Таня', tp['min_kanos'], tp['max_kanos']]
        if message.content.find('тест') == -1:
            await resp_channel.send(f"🌊 Таня {tp['die']} --- {tp['min_kanos']}   (записал {message.author.display_name})")
        await message.delete()

    # Цент
    elif message.content.lower().startswith(('!цент', '!wtyn')):
        tp = time_proc(message.content)
        resp['cent'] = ['Цент', tp['min_cent'], tp['max_cent']]
        if message.content.find('тест') == -1:
            await resp_channel.send(f"🐓 Цент {tp['die']} --- {tp['min_cent']}   (записал {message.author.display_name})")
        await message.delete()

    # Инфо о рб
    elif message.content.lower().startswith('!рб'):
        date_now = datetime.strptime(datetime.now(tz=timezone(timedelta(hours=3))).strftime(date_string), date_string)
        for key in resp.keys():
            try:
                date_max = datetime.strptime(resp[key][2], date_string)
                if date_max < date_now:
                    resp[key][1] = resp[key][2] = '🤷‍♀️'
            except:
                pass
        await message.channel.send(table())

    # Релог
    elif message.content.lower().startswith('!релог'):
        tp = time_proc(message.content)
        for key in resp.keys():
            resp[key][1] = tp['min_kanos']
            resp[key][2] = tp['max_kanos']
        resp['cent'][1] = resp['cent'][2] = '🤷‍♀️'
        await resp_channel.send(table())

    # Очистка
    elif message.content.lower().startswith('!очистка'):
        for key in resp.keys():
            resp[key][1] = resp[key][2] = '🤷‍♀️'
        await message.channel.send('Респы очищены')

    # Ракета
    elif message.content.startswith('!ракета'):
        await message.channel.send(f"{message.content.replace('!ракета ', '').replace('!ракета', '')} получает 🚀")

    # Какашка
    elif message.content.startswith('!какашка'):
        await message.channel.send(f"{message.content.replace('!какашка ', '').replace('!какашка', '')} поймал 💩")

    # Автор
    elif message.content.startswith('!автор'):
        await message.channel.send('Данный бот является собственностью Кочевника')

    # Хелп
    elif message.content.startswith('!хелп'):
        await message.channel.send('''
```
!алес (люма/дент/таня/цент) - записывает респ босса, которого слили только что (по МСК).
!алес 12:50 - записывает респ босса, которого слили в определенное время (по МСК).
!алес 23:55 вчера - записывает респ босса, которого слили до 00 часов текущего дня (по МСК).
!рб - выводит актуальную информацию обо всех записанных респах. Если макси прошло - респ удаляется.
!релог - устанавливает респы всех боссов в соответствии с поведением после релога сервера.
!релог 12:50 - устанавливает респы всех боссов после релога сервера в определённое время.
!ракета @адресат - для души...
!какашка - по просьбам трудящихся =)
```
        ''')


client.run(DISCORD_BOT_TOKEN)
