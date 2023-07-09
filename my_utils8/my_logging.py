# Задание №1
# - Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# - Например отлавливаем ошибку деления на ноль.

# Задание №2
# - На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и
# результат её работы в файл.
# - Напишите аналогичный декоратор, но внутри используйте модуль logging.

# Задание №3
# - Доработаем задачу 2.
# - Сохраняйте в лог файл раздельно:
#   - уровень логирования,
#   - дату события,
#   - имя функции (не декоратора),
#   - аргументы вызова,
#   - результат.

import logging


class _MyLoggerDecorator:
    """
    Класс - для работы с логгером
    """
    def __init__(self, function, log_file_name='homework_3_15.log', level='debug'):
        self.logging = logging
        match level.lower():
            case 'debug':
                log_lev = logging.DEBUG
            case 'info':
                log_lev = logging.INFO
            case 'warning':
                log_lev = logging.WARNING
            case 'error':
                log_lev = logging.ERROR
            case 'critical':
                log_lev = logging.CRITICAL
            case _:
                log_lev = logging.NOTSET
        self.function = function
        log_fmt = '{asctime} - {name} - {levelname:<8} {message}'
        self.logging.basicConfig(format=log_fmt,
                                 style='{',
                                 filename=log_file_name,
                                 encoding='utf-8',
                                 level=log_lev)

    def __call__(self, *args, **kwargs):
        try:
            res = self.function(*args, **kwargs)
            self.logging.info(f'Выполнена функция {self.function.__name__}{tuple(args) if args else ""}'
                              f'{dict(**kwargs) if kwargs else ""} = {res}')
            return res
        except BaseException as e:
            self.logging.error(f'Ошибка! {e}')


def my_logger_decorator(function=None, log_file_name='homework_3_15.log', level='debug'):
    """
    Функция - обертка - для вызова класса с требуемыми параметрами
    :param function:
    :param log_file_name:
    :param level:
    :return:
    """
    if function:
        return _MyLoggerDecorator(function)
    else:
        def wrapper(func):
            return _MyLoggerDecorator(func, log_file_name, level)
        return wrapper
