# Погружение в Python (семинары)
# Урок 15. Обзор стандартной библиотеки Python
#
import my_utils8 as mu8


@mu8.my_logger_decorator(level='info')
def s_div(a=1, b=1):
    return a / b


@mu8.my_logger_decorator(level='info')
def my_str_to_date(text):
    return mu8.parse_date(text)


if __name__ == '__main__':
    print('--== Задания семинара ==--')
    print('--== Работа с logger ==--')
    print(s_div(8, 4))
    print(s_div(8, 0))

    print('\n--== Работа с модулем datetime ==--')
    print(my_str_to_date('1-й четверг ноября'))
    print(my_str_to_date('3-я среда мая'))
    print(my_str_to_date('7-я пятница декабря'))
