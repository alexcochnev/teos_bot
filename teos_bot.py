import json
import discord
from datetime import datetime, timedelta, timezone
from os import path
import re
import random
import sqlalchemy

username = 'wcdvvvukjlgxrd'
password = '86fd2ee0085b777415f3d512446e7984b6e117003416d74d44278769b02c1623'
hostname = 'ec2-34-250-16-127.eu-west-1.compute.amazonaws.com'
database = 'davpb8kf8pb4up'
engine = sqlalchemy.create_engine('postgresql://' + username + ':' + password + '@' + hostname + '/' + database)

DISCORD_BOT_TOKEN = 'ODM5MDkyMzAzNjQ4OTE1NDc2.YJEnmg.o78O95FIlIJoI2HhG2u5lFcyXmg'
# DISCORD_BOT_TOKEN = 'ODM5NDYxODEzMjkyNjMwMDM4.YJJ_vA.IEnOxbcX6hkfRhcOAqFwbEQVBBw'  # тестовый бот

resp = {'ales': ['Алес', '🤷‍♀️', '🤷‍♀️', 0], 'lumen': ['Люма', '🤷‍♀️', '🤷‍♀️', 0],
        'tanya': ['Таня', '🤷‍♀️', '🤷‍♀️', 0], 'dent': ['Дент', '🤷‍♀️', '🤷‍♀️', 0],
        'cent': ['Цент', '🤷‍♀️', '🤷‍♀️', 0]}
rb_dict = {'алес': {'name': 'ales', 'name_rus': 'Алес', 'pic': '🌪', 'type': 'kanos'},
           'люма': {'name': 'lumen', 'name_rus': 'Люма', 'pic': '🔥', 'type': 'kanos'},
           'таня': {'name': 'tanya', 'name_rus': 'Таня', 'pic': '🌊', 'type': 'kanos'},
           'дент': {'name': 'dent', 'name_rus': 'Дент', 'pic': '🌿', 'type': 'kanos'},
           'цент': {'name': 'cent', 'name_rus': 'Цент', 'pic': '🐓', 'type': 'cent'}}
date_string = '%d.%m %H:%M'
time_string = '%H:%M'
ball = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
        'Мне кажется — «да»', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят — «да»', 'Да',
        'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
        'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»',
        'Перспективы не очень хорошие', 'Весьма сомнительно']


with engine.connect() as con:
    bd_resp = con.execute('select * from teos.resp')
    for row in bd_resp:
        resp[row['id']][1] = row['min']
        resp[row['id']][2] = row['max']
        resp[row['id']][3] = row['message_id']

client = discord.Client()


def save_to_db():
    with engine.connect() as con:
        for key in resp.keys():
            con.execution_options(autocommit=True).execute(
                f"update teos.resp set min = '{resp[key][1]}', max = '{resp[key][2]}', message_id = '{resp[key][3]}' where id = '{key}';")


def print_table():
    return f'''
🌪 {resp['ales'][0]}:    Мини {resp['ales'][1]} --- Макси {resp['ales'][2]}
🔥 {resp['lumen'][0]}:  Мини {resp['lumen'][1]} --- Макси {resp['lumen'][2]}
🌿 {resp['dent'][0]}:    Мини {resp['dent'][1]} --- Макси {resp['dent'][2]}
🌊 {resp['tanya'][0]}:    Мини {resp['tanya'][1]} --- Макси {resp['tanya'][2]}
🐓 {resp['cent'][0]}:    Мини {resp['cent'][1]} --- Макси {resp['cent'][2]}
        '''


def calc_resp(message):
    dt = re.search(r'\b[0-2]?\d[:][0-5]\d\b', message.replace('.', ':'))
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
    return {'die': dt.strftime(time_string),
            'min_kanos_date': min_kanos.strftime(date_string), 'min_kanos_time': min_kanos.strftime(time_string),
            'max_kanos': max_kanos.strftime(date_string), 'min_cent_date': min_cent.strftime(date_string),
            'min_cent_time': min_cent.strftime(time_string), 'max_cent': max_cent.strftime(date_string)}


async def send_resp(message, rb):
    cr = calc_resp(message.content)
    min_date = f"min_{rb_dict[rb]['type']}_date"
    min_time = f"min_{rb_dict[rb]['type']}_time"
    max = f"max_{rb_dict[rb]['type']}"
    resp[rb_dict[rb]['name']][1] = cr[min_date]
    resp[rb_dict[rb]['name']][2] = cr[max]
    approx = 'примерно ' if message.content.find('примерно') != -1 else ''
    if message.content.find('тест') == -1:
        send_message = await resp_channel.send(f"{rb_dict[rb]['pic']} {rb_dict[rb]['name_rus']} {cr['die']} --- {cr[min_time]} {approx}  (записал {message.author.display_name})")
        resp[rb_dict[rb]['name']][3] = send_message.id
    await message.delete()
    save_to_db()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    global resp_channel
    resp_channel = client.get_channel(542043903356829706)  # основной сервер теоса
    # resp_channel = client.get_channel(839090077396107314)  # 1й тестовый сервер (прод бот)
    # resp_channel = client.get_channel(839939523341189140)  # 2й тестовый сервер (тест бот)

    # for channel in client.get_all_channels():  # получить id канала
    #     print(channel.name, channel.id)


@client.event
async def on_message(message):
    # if not message.content.startswith('!'):
    #     return
    if message.author == client.user:
        return

    # Шар предсказаний
    elif message.content.lower().startswith('!шар'):
        await message.channel.send(random.choice(ball))

    # Какашка
    elif message.content.lower().startswith('!какашка'):
        await message.channel.send(f"{message.content.lower().replace('!какашка ', '').replace('!какашка', '')} поймал 💩")

    # Ракета
    elif message.content.lower().startswith('!ракета'):
        await message.channel.send(f"{message.content.lower().replace('!ракета ', '').replace('!ракета', '')} получает 🚀")

    # Алес
    elif message.content.lower().startswith(('!алес', '!fktc')):
        await send_resp(message, 'алес')

    # Люма
    elif message.content.lower().startswith(('!люма', '!люмен', '!k.vf')):
        await send_resp(message, 'люма')

    # Дент
    elif message.content.lower().startswith(('!дент', '!ltyn')):
        await send_resp(message, 'дент')

    # Таня
    elif message.content.lower().startswith(('!таня', '!тайнор', '!nfyz')):
        await send_resp(message, 'таня')

    # Цент
    elif message.content.lower().startswith(('!цент', '!wtyn')):
        await send_resp(message, 'цент')

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
        await message.channel.send(print_table())
        save_to_db()

    # Релог
    elif message.content.lower().startswith('!релог'):
        cr = calc_resp(message.content)
        for key in resp.keys():
            resp[key][1] = cr['min_kanos_date']
            resp[key][2] = cr['max_kanos']
        resp['cent'][1] = resp['cent'][2] = '🤷‍♀️'
        await resp_channel.send(f"Релог {cr['die']}")
        await resp_channel.send(print_table())
        save_to_db()

    # Очистка
    elif message.content.lower().startswith('!очистка'):
        if message.content.find('все') != -1:
            for key in resp.keys():
                resp[key][1] = resp[key][2] = '🤷‍♀️'
            await message.channel.send('Респы очищены')

        for key in rb_dict.keys():
            if message.content.find(key) != -1:
                resp[rb_dict[key]['name']][1] = resp[rb_dict[key]['name']][2] = '🤷‍♀️'
                if resp[rb_dict[key]['name']][3] != 0:
                    try:
                        found_message = await resp_channel.fetch_message(resp[rb_dict[key]['name']][3])
                        await found_message.delete()
                    except:
                        pass
                    resp[rb_dict[key]['name']][3] = 0
                await message.channel.send(f"{rb_dict[key]['name_rus']} удалён")
        save_to_db()

    # Автор
    elif message.content.startswith('!автор'):
        await message.channel.send('Данный бот является собственностью Кочевника')

    # Хелп
    elif message.content.startswith('!хелп'):
        await message.channel.send('''
```
!алес (люма/дент/таня/цент) - записывает респ босса, которого слили только что (по МСК).
!алес 12:50 - записывает респ босса, которого слили в определенное время (по МСК).
!алес 12:50 примерно - записывает примерный респ босса. Тоже самое, только с пометкой "примерно" (по МСК).
!алес 23:55 вчера - записывает респ босса, которого слили до 00 часов текущего дня (по МСК).
!рб - выводит актуальную информацию обо всех записанных респах. Если макси прошло - респ удаляется.
!очистка алес - удаляет респ босса (в базе и последнюю запись о нём в канале "респы").
!релог - устанавливает респы всех боссов в соответствии с поведением после релога сервера.
!релог 12:50 - устанавливает респы всех боссов после релога сервера в определённое время.
!ракета @адресат - для души...
!какашка @адресат - по просьбам трудящихся =)
!шар "вопрос" - шар предсказаний, знает ответ на любые вопросы.
```
        ''')


client.run(DISCORD_BOT_TOKEN)
