# Погружение в Python (семинары)
# Урок 15. Обзор стандартной библиотеки Python
#
import my_utils8 as mu8


@mu8.MyLoggerDecorator
def s_div(a, b):
    return a / b


if __name__ == '__main__':
    print('--== Задания семинара ==--')
    print(s_div(8, 4))
