from datetime import datetime, timedelta, timezone

RESP = {'ales': ['Алес', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3))) - timedelta(minutes=1)],
        'lumen': ['Люма', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'tanya': ['Таня', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'dent': ['Дент', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'cent': ['Цент', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'knight': ['Рыцарь', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)],
        'kima': ['Кима', '🤷‍♀️', '🤷‍♀️', 0, '', datetime.now(tz=timezone(timedelta(hours=3)))-timedelta(minutes=1)]}
RB_DICT = {'алес': {'name': 'ales', 'name_rus': 'Алес', 'pic': '🌪', 'type': 'kanos'},
           'люма': {'name': 'lumen', 'name_rus': 'Люма', 'pic': '🔥', 'type': 'kanos'},
           'таня': {'name': 'tanya', 'name_rus': 'Таня', 'pic': '🌊', 'type': 'kanos'},
           'дент': {'name': 'dent', 'name_rus': 'Дент', 'pic': '🌿', 'type': 'kanos'},
           'цент': {'name': 'cent', 'name_rus': 'Цент', 'pic': '🐓', 'type': 'cent'},
           'рыцарь': {'name': 'knight', 'name_rus': 'Рыцарь', 'pic': '🛡️', 'type': 'knight'},
           'кима': {'name': 'kima', 'name_rus': 'Кима', 'pic': '🐒', 'type': 'kima'}}
DATE_STRING = '%d.%m %H:%M'
TIME_STRING = '%H:%M'
BALL = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
        'Мне кажется — «да»', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят — «да»', 'Да',
        'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
        'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ — «нет»', 'По моим данным — «нет»',
        'Перспективы не очень хорошие', 'Весьма сомнительно']