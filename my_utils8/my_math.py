"""
Класс для работы с математикой
"""

import json
from my_utils8.my_exceptions import MyValueError


class MyFactorial:
    """
    Класс - факториал, для демонстрации продвинутой работы с ООП
    """
    _cache = {}

    def __init__(self, k, file_name='output.json'):
        if k < 0:
            raise MyValueError('Факториал от отрицательного числа не считаем!')
        self.k = k
        self.file_name = file_name
        self._cache = {}  # Кэш для вычисленных ранее значений

    def _factorial(self, k: int) -> int:
        """
        Рекурсивное вычисление факториала с сохранением значений в кэше
        :param k:
        :return: f!(k)
        """
        if k in self._cache.keys():
            return self._cache[k]
        else:
            if k < 0:
                raise MyValueError('Факториал от отрицательного числа не считаем!')
            elif k < 2:
                self._cache[k] = 1
                return 1
            else:
                self._cache[k] = k * self._factorial(k - 1)
                return self._cache[k]

    def get_factorial(self):
        """
        Обертка для метода вычисления
        :return:
        """
        return self._factorial(self.k)

    def __repr__(self):
        """
        Выводим текущий кэш вычисленных значений факториала
        :return:
        """
        return f'{self._cache}'

    def __str__(self):
        return str(self.get_factorial())

    def __enter__(self):
        """
        Задаем менеджер контекста
        :return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        При выходе из менеджера контекста - пишем кэш в json-файл
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        try:
            with open(self.file_name, 'w') as f:
                json.dump(self._cache, f, indent=4)
        except FileNotFoundError:
            print(f'Файл {self.file_name} не найден!')


class MyRangeFactorial(MyFactorial):
    """
    Итеративный класс для вычисления факториала
    :param args: start, stop, step
    """

    def __init__(self, *args):
        """
        Инициализация с различным количеством аргументов
        :param args:
        """
        self._start = 1
        self._step = 1
        match len(args):
            case 1:
                self._stop = args[0]
            case 2:
                self._start = args[0]
                self._stop = args[1]
            case 3:
                self._start = args[0]
                self._stop = args[1]
                self._step = args[2]
            case _:
                raise MyValueError('Ошибка в параметрах')
        if self._start > self._stop:
            raise MyValueError('Начальное значение больше конечного')
        self._current = self._start
        super().__init__(self._stop)  # Сразу же вычисляем все значения факториала (они сохранятся в кэше)

    def __str__(self):
        """
        Возвращаем значение факториала последнего члена в итерациях
        :return:
        """
        return f'{super()._factorial(self._stop)}'

    def __iter__(self):
        """
        Необходимо для итерируемого класса
        :return:
        """
        return self

    def __next__(self):
        """
        Один шаг итерации. Последовательно вычисляем значения факториала,
        и контролируем шаг текущей переменной
        :return:
        """
        if self._current < self._stop:
            tmp = super()._factorial(self._current)
            self._current += self._step
            return tmp
        else:
            raise StopIteration


def find_roots(a, b, c):
    """
    Вычисление корней квадратного уравнения ax^2+bx+c=0
    :param a:
    :param b:
    :param c:
    :return: Корни уравнения, даже мнимые
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:  # мнимые корни
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        return (real_part, -imaginary_part), (real_part, imaginary_part)
    elif discriminant == 0:  # один действительный корень
        return -b / (2 * a)
    else:  # два действительных корня
        return ((-b - discriminant ** 0.5) / 2 * a,
                (-b + discriminant ** 0.5) / 2 * a,
                )
