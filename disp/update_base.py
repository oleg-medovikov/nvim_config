from .dispetcher import dp, bot
from aiogram import types
import os
import pandas as pd

from clas import User, PersonDefaults
from func import delete_message

FILES = {
    'PersonDefaults.xlsx':     'update_person_defaults',
    'Karta.xlsx':              'update_location',
    'KartaDescriptions.xlsx':  'update_location_description',
    'Manual.xlsx':             'update_manual',
    'Items.xlsx':              'update_item',
    'Events.xlsx':             'update_event',
    'Monsters.xlsx':           'update_monster',
        }

NAMES = {
    'PersonDefaults.xlsx': [
        'date_update', 'profession', 'start_location_id', 'money_min',
        'money_max', 'start_list_items', 'max_health_min', 'max_health_max',
        'max_mind_min', 'max_mind_max', 'speed_min', 'speed_max',
        'stealth_min', 'stealth_max', 'strength_min', 'strength_max',
        'knowledge_min', 'knowledge_max', 'godliness_min', 'godliness_max',
        'luck_min', 'luck_max'
        ],
    'Karta.xlsx': [
        'node_id', 'name_node', 'declension', 'contact_list_id', 'district',
        'district_id', 'street', 'dist', 'date_update'
        ],
    'KartaDescriptions.xlsx': [
        'node_id', 'stage', 'description', 'date_update'
        ],
    'Manual.xlsx': [
        'm_id', 'm_name', 'order', 'text', 'date_update'
        ],
    'Items.xlsx': [
        'i_id', 'name', 'description', 'equip_mess', 'fail_mess',
        'remove_mess', 'drop_mess', 'i_type', 'slot', 'effect', 'demand',
        'emoji', 'cost', 'single_use', 'achievement', 'date_update'
        ],
    'Events.xlsx': [
        'e_id', 'e_name', 'single', 'active', 'stage', 'node_id',
        'profession', 'demand', 'description', 'mess_prize',
        'mess_punishment', 'check', 'choice', 'prize', 'punishment',
        'username', 'date_update'
        ],
    'Monsters.xlsx': [
        'm_id', 'name', 'description', 'mess_win', 'mess_lose',
        'check_of_stels', 'nigthmare', 'crush', 'phisical_resist',
        'magic_resist', 'check_mind', 'check_fight', 'mind_damage',
        'body_damage', 'health', 'price', 'item', 'experience', 'date_update'
        ],
        }


@dp.message_handler(content_types='document')
async def update_base(message: types.Message):
    """Работа с файлами которые посылает пользователь"""
    await delete_message(message)

    USER = await User.get(message['from']['id'])
    if USER is None or not USER.admin:
        return await message.answer('Зачем вы шлёте мне файлы?')

    FILE = message['document']

    if not FILE['file_name'] in FILES.keys():
        return await message.answer('У файла неправильное имя')

    DESTINATION = 'temp/' + FILE.file_unique_id + 'xlsx'

    await bot.download_file_by_id(
        file_id=FILE.file_id,
        destination=DESTINATION
        )

    COLUMNS = NAMES.get(FILE['file_name'])
    try:
        df = pd.read_excel(DESTINATION, usecols=COLUMNS)
    except Exception as e:
        os.remove(DESTINATION)
        return await message.answer(str(e))

    list_ = df.to_dict('records')

    MESS = {
        'PersonDefaults.xlsx': await PersonDefaults.update_all(list_),
        }.get(FILE['file_name'], 'не знаю, как это обновить')

    await message.answer(MESS)
    os.remove(DESTINATION)