# Задание №3
# - Создайте класс с базовым исключением и дочерние классы-исключения:
#  - ошибка уровня,
#  - ошибка доступа.

# Задание №6
# - Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# - Передавайте необходимые данные из основного кода проекта.

class MyBaseException(BaseException):
    """
    Базовый класс для работы с моими персональными исключениями
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.__class__.__name__}, {self.message}'
        else:
            return '{self.__class__.__name__} has been raised!'


class MyLevelException(MyBaseException):
    """
    Мой класс для обработки исключений ошибок уровня
    """
    def __init__(self, *args):
        super().__init__(*args)


class MyAccessException(MyBaseException):
    """
    Мой класс для обработки исключений ошибок по доступу
    """
    def __init__(self, *args):
        super().__init__(*args)


class MyValueError(MyBaseException):
    """
    Мой класс для обработки исключений ошибок по значению переменных
    """
    def __init__(self, *args):
        super().__init__(*args)
