import random
import re
import time
from datetime import datetime, timedelta, timezone

import discord
# import sqlalchemy
from config import (
    DISCORD_BOT_TOKEN,
    RESP_CHANNEL_ID,
    RESP_LOW_ZONE_ID,
    GUILD_ID,
    AOL_EMOJI_ID,
    UOF_EMOJI_ID,
    CHANGE_ROLE_MESSAGE_ID,
    ROLE_15_ID,
    ROLE_30_ID,
    ROLE_60_ID,
    ROLE_ARTI_ID,
    ROLE_VALHEIM_ID,
    ROLE_RB_ID,
    CHECK_RB_ID,
)

resp = {'ales': ['Алес', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'lumen': ['Люма', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'tanya': ['Таня', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'dent': ['Дент', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'cent': ['Цент', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'knight': ['Рыцарь', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'kima': ['Кима', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)]}
rb_dict = {'алес': {'name': 'ales', 'name_rus': 'Алес', 'pic': '🌪', 'type': 'kanos'},
           'люма': {'name': 'lumen', 'name_rus': 'Люма', 'pic': '🔥', 'type': 'kanos'},
           'таня': {'name': 'tanya', 'name_rus': 'Таня', 'pic': '🌊', 'type': 'kanos'},
           'дент': {'name': 'dent', 'name_rus': 'Дент', 'pic': '🌿', 'type': 'kanos'},
           'цент': {'name': 'cent', 'name_rus': 'Цент', 'pic': '🐓', 'type': 'cent'},
           'рыцарь': {'name': 'knight', 'name_rus': 'Рыцарь', 'pic': '🛡️', 'type': 'knight'},
           'кима': {'name': 'kima', 'name_rus': 'Кима', 'pic': '🐒', 'type': 'cent'}}
date_string = '%d.%m %H:%M'
time_string = '%H:%M'
ball = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
        'Мне кажется — «да»', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят — «да»', 'Да',
        'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
        'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»',
        'Перспективы не очень хорошие', 'Весьма сомнительно']


#with engine.connect() as con:
#    bd_resp = con.execute(f'select * from {DB_TABLE}')
#    for row in bd_resp:
#        resp[row['id']][1] = row['min']
#        resp[row['id']][2] = row['max']
#        resp[row['id']][3] = row['message_id']

client = discord.Client(intents=discord.Intents.all())


def save_to_db():
#    with engine.connect() as con:
#        for key in resp.keys():
#            con.execution_options(autocommit=True).execute(
#                f"update {DB_TABLE} set min = '{resp[key][1]}', max = '{resp[key][2]}', message_id = '{resp[key][3]}' where id = '{key}';")
    return


def print_table():
    return f'''
🌪 {resp['ales'][0]}:    Мини {resp['ales'][1]} --- Макси {resp['ales'][2]}   {resp['ales'][4]}
🔥 {resp['lumen'][0]}:  Мини {resp['lumen'][1]} --- Макси {resp['lumen'][2]}   {resp['lumen'][4]}
🌿 {resp['dent'][0]}:    Мини {resp['dent'][1]} --- Макси {resp['dent'][2]}   {resp['dent'][4]}
🌊 {resp['tanya'][0]}:    Мини {resp['tanya'][1]} --- Макси {resp['tanya'][2]}   {resp['tanya'][4]}
🐓 {resp['cent'][0]}:    Мини {resp['cent'][1]} --- Макси {resp['cent'][2]}   {resp['cent'][4]}
🛡️ {resp['knight'][0]}:    Мини {resp['knight'][1]} --- Макси {resp['knight'][2]}   {resp['knight'][4]}
🐒 {resp['kima'][0]}:    Мини {resp['kima'][1]} --- Макси {resp['kima'][2]}   {resp['kima'][4]}
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
    min_knight = dt + timedelta(hours=17)
    max_knight = dt + timedelta(hours=19)
    return {'die': dt.strftime(time_string),
            'min_kanos_date': min_kanos.strftime(date_string),
            'min_kanos_time': min_kanos.strftime(time_string),
            'max_kanos': max_kanos.strftime(date_string),
            'min_cent_date': min_cent.strftime(date_string),
            'min_cent_time': min_cent.strftime(time_string),
            'max_cent': max_cent.strftime(date_string),
            'min_knight_date': min_knight.strftime(date_string),
            'min_knight_time': min_knight.strftime(time_string),
            'max_knight': max_knight.strftime(date_string)
            }


async def send_resp(message, rb):
    content = message.content.lower()
    if datetime.now(tz=timezone(timedelta(hours=3))) < (resp[rb_dict[rb]['name']][5] + timedelta(minutes=1)):
        sent_message = await message.channel.send('Воу-воу, полегче, не все сразу! Этого босса уже записали.')
        try:
            await message.delete()
        except discord.errors.NotFound:
            pass
        time.sleep(6)
        await sent_message.delete()
        return

    resp[rb_dict[rb]['name']][5] = datetime.now(tz=timezone(timedelta(hours=3)))
    cr = calc_resp(content)
    min_date = f"min_{rb_dict[rb]['type']}_date"
    min_time = f"min_{rb_dict[rb]['type']}_time"
    max = f"max_{rb_dict[rb]['type']}"
    resp[rb_dict[rb]['name']][1] = cr[min_date]
    resp[rb_dict[rb]['name']][2] = cr[max]
    approx = 'примерно ' if content.find('примерно') != -1 else ''
    if content.find('тест') == -1:
        if rb == 'кима':
            sent_message = await resp_low_zone.send(f"{rb_dict[rb]['pic']} {rb_dict[rb]['name_rus']} {cr['die']} --- {cr[min_time]} {approx}  (записал {message.author.display_name})")
        else:
            sent_message = await resp_channel.send(f"{rb_dict[rb]['pic']} {rb_dict[rb]['name_rus']} {cr['die']} --- {cr[min_time]} {approx}  (записал {message.author.display_name})")
        resp[rb_dict[rb]['name']][3] = sent_message.id
        if content.find('уши') != -1 or content.find('ас') != -1:
            await sent_message.add_reaction(client.get_emoji(AOL_EMOJI_ID))
        elif content.find('негры') != -1 or content.find('ся') != -1:
            await sent_message.add_reaction(client.get_emoji(UOF_EMOJI_ID))
    await message.delete()
    save_to_db()


async def permission_alert(message):
    await message.channel.send('Недостаточно прав для использования данной команды.')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game("!хелп"))
    global resp_channel
    global resp_low_zone

    resp_channel = client.get_channel(RESP_CHANNEL_ID)
    resp_low_zone = client.get_channel(RESP_LOW_ZONE_ID)

    global guild
    global role_15
    global role_30
    global role_60
    global role_arti
    global role_valheim
    global role_rb

    guild = client.get_guild(GUILD_ID)
    role_15 = guild.get_role(ROLE_15_ID)
    role_30 = guild.get_role(ROLE_30_ID)
    role_60 = guild.get_role(ROLE_60_ID)
    role_arti = guild.get_role(ROLE_ARTI_ID)
    role_valheim = guild.get_role(ROLE_VALHEIM_ID)
    role_rb = guild.get_role(ROLE_RB_ID)


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == CHANGE_ROLE_MESSAGE_ID:
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == '🤡':
            await member.add_roles(role_arti, reason='Роль добавлена пользователем')
        elif payload.emoji.name == '15':
            await member.add_roles(role_15, reason='Роль добавлена пользователем')
        elif payload.emoji.name == '30':
            await member.add_roles(role_30, reason='Роль добавлена пользователем')
        elif payload.emoji.name == '60':
            await member.add_roles(role_60, reason='Роль добавлена пользователем')
        elif payload.emoji.name == '🪓':
            await member.add_roles(role_valheim, reason='Роль добавлена пользователем')


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == CHANGE_ROLE_MESSAGE_ID:
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == '🤡':
            await member.remove_roles(role_arti, reason='Роль удалена пользователем')
        elif payload.emoji.name == '15':
            await member.remove_roles(role_15, reason='Роль удалена пользователем')
        elif payload.emoji.name == '30':
            await member.remove_roles(role_30, reason='Роль удалена пользователем')
        elif payload.emoji.name == '60':
            await member.remove_roles(role_60, reason='Роль удалена пользователем')
        elif payload.emoji.name == '🪓':
            await member.remove_roles(role_valheim, reason='Роль удалена пользователем')


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

    # Аватар
    elif message.content.lower().startswith('!аватар'):
        if len(message.mentions):
            for mention in message.mentions:
                # await message.channel.send(mention.avatar_url)
                await message.channel.send(mention.avatar.replace(static_format='png', size=4096))
        else:
            # await message.channel.send(message.author.avatar_url)
            await message.channel.send(message.author.avatar.replace(static_format='png', size=4096))

    # Алес
    elif message.content.lower().startswith(('!алес', '!fktc')):
        if message.author in role_rb.members:
            await send_resp(message, 'алес')
        else:
            await permission_alert(message)

    # Люма
    elif message.content.lower().startswith(('!люма', '!люмен', '!k.vf')):
        if message.author in role_rb.members:
            await send_resp(message, 'люма')
        else:
            await permission_alert(message)

    # Дент
    elif message.content.lower().startswith(('!дент', '!ltyn')):
        if message.author in role_rb.members:
            await send_resp(message, 'дент')
        else:
            await permission_alert(message)

    # Таня
    elif message.content.lower().startswith(('!таня', '!тайнор', '!nfyz')):
        if message.author in role_rb.members:
            await send_resp(message, 'таня')
        else:
            await permission_alert(message)

    # Цент
    elif message.content.lower().startswith(('!цент', '!wtyn')):
        if message.author in role_rb.members:
            await send_resp(message, 'цент')
        else:
            await permission_alert(message)

    # Рыцарь
    elif message.content.lower().startswith(('!рыц', '!рыцарь', '!hsw')):
        if message.author in role_rb.members:
            await send_resp(message, 'рыцарь')
        else:
            await permission_alert(message)

    # Кима
    elif message.content.lower().startswith(('!кима', '!rbvf')):
        await send_resp(message, 'кима')

    # Инфо о рб
    elif message.content.lower().startswith('!рб'):
        if message.channel.id != CHECK_RB_ID:
            sent_message = await message.channel.send(f'Для данной команды существует отдельный канал <#{CHECK_RB_ID}>. Повторите запрос там')
            try:
                await message.delete()
            except discord.errors.NotFound:
                pass
            time.sleep(20)
            await sent_message.delete()
            return

        if message.author in role_rb.members:
            date_now = datetime.strptime(datetime.now(tz=timezone(timedelta(hours=3))).strftime(date_string), date_string)
            for key in resp.keys():
                try:
                    date_min = datetime.strptime(resp[key][1], date_string)
                    if date_min < date_now:
                        resp[key][4] = '(может встать ✅)'
                    else:
                        resp[key][4] = '(ещё рано ❌)'
                    date_max = datetime.strptime(resp[key][2], date_string)
                    if date_max < date_now:
                        resp[key][1] = resp[key][2] = '🤷‍♀️'
                except:
                    resp[key][4] = '(может встать ✅)'
            await message.channel.send(print_table())
            save_to_db()
        else:
            await permission_alert(message)

    # Релог
    elif message.content.lower().startswith('!релог'):
        if message.author in role_rb.members:
            cr = calc_resp(message.content)
            for key in resp.keys():
                resp[key][1] = cr['min_kanos_date']
                resp[key][2] = cr['max_kanos']
                resp[key][4] = ''
            resp['cent'][1] = resp['cent'][2] = '🤷‍♀️'
            resp['knight'][1] = resp['knight'][2] = '🤷‍♀️'
            resp['kima'][1] = resp['kima'][2] = '🤷‍♀️'
            await resp_channel.send(f"Релог {cr['die']}   (записал {message.author.display_name})")
            await resp_channel.send(print_table())
            await message.delete()
            save_to_db()
        else:
            await permission_alert(message)

    # Очистка
    elif message.content.lower().startswith('!очистка'):
        if message.author in role_rb.members:
            if message.content.find('все') != -1:
                for key in resp.keys():
                    resp[key][1] = resp[key][2] = '🤷‍♀️'
                await message.channel.send('Респы очищены')

            for key in rb_dict.keys():
                if message.content.find(key) != -1:
                    resp[rb_dict[key]['name']][1] = resp[rb_dict[key]['name']][2] = '🤷‍♀️'
                    if resp[rb_dict[key]['name']][3] != 0:
                        try:
                            if key == 'кима':
                                found_message = await resp_low_zone.fetch_message(resp[rb_dict[key]['name']][3])
                            else:
                                found_message = await resp_channel.fetch_message(resp[rb_dict[key]['name']][3])
                            await found_message.delete()
                        except:
                            pass
                        resp[rb_dict[key]['name']][3] = 0
                    await message.channel.send(f"{rb_dict[key]['name_rus']} удалён")
            save_to_db()
        else:
            await permission_alert(message)

    # Автор
    elif message.content.startswith('!автор'):
        await message.channel.send('Данный бот является собственностью Кочевника')

    # Хелп
    elif message.content.startswith('!хелп'):
        await message.channel.send('''
```
!алес (люма/дент/таня/цент) - записывает респ босса, которого слили только что (по МСК).
!алес уши/негры/ас/ся - записывает респ босса и ставит смайлик кто его слил.
!алес 12:50 - записывает респ босса, которого слили в определенное время (по МСК).
!алес 12:50 примерно - записывает примерный респ босса. Тоже самое, только с пометкой "примерно" (по МСК).
!алес 23:55 вчера - записывает респ босса, которого слили до 00 часов текущего дня (по МСК).
!рыц или !рыцарь - записывает респ нового босса.
!кима - записывает респ кимы в респы малых зон
!рб - Работает только в канале #проверить-рб. Выводит актуальную информацию обо всех записанных респах. Если макси прошло - респ удаляется.
!очистка алес - удаляет респ босса (в базе и последнюю запись о нём в канале "респы").
!релог - устанавливает респы всех боссов в соответствии с поведением после релога сервера.
!релог 12:50 - устанавливает респы всех боссов после релога сервера в определённое время.
!ракета @адресат - для души...
!какашка @адресат - по просьбам трудящихся =)
!шар "вопрос" - шар предсказаний, знает ответ на любые вопросы.
!аватар @пользователь - показывает аватарку пользователя (или нескольких). Без упоминания - аватарка автора.
```
        ''')


client.run(DISCORD_BOT_TOKEN, reconnect=True)
