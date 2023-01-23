
from clas import Person
from conf import emoji

I_def = {
    'head':     'Непокрытая голова',
    'onehand':  'Пустые руки',
    'twohands': 'Пустые руки',
    'body':     'Голое тело',
    'legs':     'Голые ноги',
    'shoes':    'Босые ноги',
    'bag':      'Сумка пустая, не тянет плечо',
    }

I_zero = {
    'head':     '',
    'onehand':  '',
    'twohands': '',
    'body':     '',
    'legs':     '',
    'shoes':    '',
    'bag':      '',
    }

def inventory_mess(PERS: 'Person', INV: list) -> str:
    "Генерируем сообщение для списка инвентаря"

    for item in INV:
        I_zero[item.slot] += ' ' + emoji(item.emoji) + ' ' + item.name

    I_zero['hands'] = {
            I_zero['onehand'] == '' and I_zero['twohands'] == '': I_def['onehand'],
            I_zero['onehand'] != '':  I_def['onehand'],
            I_zero['twohands'] != '': I_def['twohands'],
            }[True]

    for key, value in I_zero.items():
        if key == 'hands':
            continue
        if value == '':
            I_zero[key] = I_def[key]


    MESS = f"""```
Ваш инвентарь, {PERSON.gamename}
__________________________
Голова: {HEAD}
{RUKI}
Тело: {BODY}
Ноги: {LEGS}
В вашей сумке:
```
"""
