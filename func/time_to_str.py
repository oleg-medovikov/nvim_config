from random import choice


def time_to_str(num: int) -> str:
    "Функция переводит количество тиков, во время "
    if num == 0:
        return 'Это не заняло много времени'
    H = {
        0: '',
        1: 'один час',
        2: 'два часа',
        3: 'три часа',
        4: 'четыре часа',
        5: 'пять часов',
        6: 'шесть часов',
        7: 'семь часов',
    }.get(num // 60, f'{num // 60} часов ')

    M = {
        0: '',
        15: ' пятнадцать минут',
        30: ' тридать минут',
        45: ' сорок пять минут',
    }.get(num % 60, f' {num % 60} минут')

    return f'Вы потратили {H}{M}'.replace('  ', ' ')


def timedelta_to_str(num: int) -> str:
    return choice({
        0: [
            'Справились за пару минут.',
            'Это почти не отняло у времени.',
            'Справились очень быстро.',
        ],
        1: [
            'Это заняло четверть часа.',
            'Прошло 15 минут.',
        ],
        2: [
            'Прошло полчаса.',
            'Это заняло 30 минут.',
            'Прошло тридцать минут',
        ],
        3: [
            'Потратили три четверти часа.',
            'Прошло сорок пять минут.',
            'Прошло 45 минут.',
            'Ушёл без пятнадцати минут час.',
            ],
        4: [
            'Прошёл целый час.',
            'Прошло ровно час.',
            'Это заняло целый час.',
        ],
        5: [
            'Прошёл час с четвертью.',
            'Прошёл час и 15 минут.',
            'Прошло больше часа времени.'
        ],
        6: [
            'Это заняло полтора часа.',
        ],
        7: [
            'Потребовалось почти два часа времени.',
            'Это заняло без пятнадцати минут два часа.'
        ],
        8: [
            'Прошло два часа.',
            'Это заняло ровно два часа',
            'Это заняло ровно 2 часа',
        ],
    }.get(num, ['Это заняло много времени']))
