import logging


class MyLoggerDecorator:
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
        self.logging.basicConfig(filename=log_file_name, encoding='utf-8', level=log_lev)

    def __call__(self, *args, **kwargs):
        try:
            res = self.function(*args, **kwargs)  #self.function.__name__
            self.logging.info(f'Выполнена функция {self.function.__name__} с аргументами {list(args)}, {dict(**kwargs)} и с результатом {res}')
            return res
        except BaseException as e:
            self.logging.error(f'Ошибка! {e}')
