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
import my_utils8 as mu8
import argparse
from datetime import datetime


@mu8.my_logger_decorator(level='info')
def my_str_to_date(text):
    return mu8.parse_date(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parsing dates')
    parser.add_argument('-amount', metavar='<amount of week>', type=str, help='enter amount of days', default='1')
    parser.add_argument('-dow', metavar='<day of week>', type=str, help='enter day of week',
                        default=str(datetime.now().weekday() + 1))
    parser.add_argument('-month', metavar='<month>', type=str, help='enter day of week',
                        default=str(datetime.now().month))
    args = parser.parse_args()
    param = f'{args.amount} {args.dow} {args.month}'
    print(f'{param} -> {my_str_to_date(param)}')
