# Задание #4
# - Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# - Преобразуйте его в дату в текущем году.
# - Логируйте ошибки, если текст не соответсвует формату.

# Задание No5
# - Дорабатываем задачу 4.
# - Добавьте возможность запуска из командной строки.
# - При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели,
# текущий день недели и/или текущий месяц.
# - *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.
from datetime import datetime, timedelta


def parse_date(text):
    dict_months = {'января': 1,
                   'февраля': 2,
                   'марта': 3,
                   'апреля': 4,
                   'мая': 5,
                   'июня': 6,
                   'июля': 7,
                   'августа': 8,
                   'сентября': 9,
                   'октября': 10,
                   'ноября': 11,
                   'декабря': 12,
                   }
    dict_day_of_week = {'понедельник': 1,
                        'вторник': 2,
                        'среда': 3,
                        'четверг': 4,
                        'пятница': 5,
                        'суббота': 6,
                        'воскресенье': 7,
                        }

    current_year = datetime.now().year
    parts = text.split()

    if len(parts) != 3:
        return None

    # Обрабатываем не только строковые, но и числовые значения (задачка со *)
    number = int(parts[0][:parts[0].find("-") if parts[0].find("-") != -1 else len(parts[0])])
    day = int(parts[1]) if parts[1].isnumeric() else dict_day_of_week[parts[1]]
    month = int(parts[2]) if parts[2].isnumeric() else dict_months[parts[2]]

    date = datetime(current_year, month, 1)
    day_of_week = date.weekday()
    first_day_of_week = (day - day_of_week) % 7

    if first_day_of_week < 1:
        first_day_of_week += 7

    target_day = first_day_of_week + ((number - 1) * 7)

    res = date + timedelta(days=(target_day - 1))
    if date.month == res.month:
        return res
    else:
        raise ValueError('no request date')
