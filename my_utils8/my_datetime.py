# Задание #4
# - Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# - Преобразуйте его в дату в текущем году.
# - Логируйте ошибки, если текст не соответсвует формату.

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

    s = parts[0][:parts[0].find("-")]
    number = int(s)
    day = dict_day_of_week[parts[1]]
    month = dict_months[parts[2]]

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



# # Пример использования функции
# text = "1-й четверг ноября"
# result = parse_date(text)
#
# if result:
#     print(f"Полученная дата: {result.strftime('%d.%m.%Y')}")
# else:
#     print("Некорректный формат текста")
