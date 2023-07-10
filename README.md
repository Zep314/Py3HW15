# Погружение в Python (семинары)
## Урок 15. Обзор стандартной библиотеки Python

### Задание 1

Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

### Решение
**Задание 1**

Взял работы с предыдущих семинаров:
1. Вычисление факториала (файл *dz_my_factorial.py*)
2. Вычисление диапазона факториалов (файл *dz_my_range_factorial.py*)
3. Решение квадратного уравнения (файл *dz_my_quad_equat.py*)

Все задачи решены с использованием логирования и возможностью запуска из командной строки 

### Результат работы:
#### 1. Вычисление факториала

    Результат работы:
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_factorial.py -h
    usage: dz_my_factorial.py [-h] [-n <f!n>] [-log <name of log file>]
   
    Solving factorial
   
    options:
      -h, --help            show this help message and exit
      -n <f!(n)>            enter argument for solving factorial
      -log <name of log file>
                            name of logfile
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_factorial.py -n 5
    120
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_factorial.py -n -5
    None
    (venv) PS C:\Work\python\dz3\Py3HW15>

    Файл factorial.log
    2023-07-10 14:22:03,543 - root - INFO     Выполнена функция my_log_factorial(5) = 120
    2023-07-10 14:22:30,202 - root - INFO     Выполнена функция my_log_factorial(-5) = None
    2023-07-10 14:23:57,424 - root - ERROR    Ошибка! MyValueError, Факториал от отрицательного числа не считаем!

#### 2. Вычисление диапазона факториалов

    Результат работы:
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_range_factorial.py -h
    usage: dz_my_range_factorial.py [-h] [-start <a>] [-stop <b>] [-step <step>] [-log <name of log file>]
   
    Return range of factorials
   
    options:
      -h, --help            show this help message and exit
      -start <a>            enter argument for start solving of factorials
      -stop <b>             enter argument for stop solving of factorials
      -step <step>          enter argument for stop solving of factorials
      -log <name of log file>
                            name of logfile
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_range_factorial.py -start 1 -stop 20 -step 3
    [1, 24, 5040, 3628800, 6227020800, 20922789888000, 121645100408832000]
    (venv) PS C:\Work\python\dz3\Py3HW15>

    Файл factorial.log
    2023-07-10 14:27:09,298 - root - INFO     Выполнена функция my_log_range_factorial(1, 20, 3) = [1, 24, 5040, 3628800, 6227020800, 20922789888000, 121645100408832000]

#### 3. Решение квадратного уравнения

    Результат работы:
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -h
    usage: dz_my_quad_equat.py [-h] [-a <a>] [-b <b>] [-c <c>] [-log <name of log file>]
   
    Solving a quadratic equation
   
    options:
      -h, --help            show this help message and exit
      -a <a>                enter argument a for a * x ** 2 + b * x + c = 0
      -b <b>                enter argument b for a * x ** 2 + b * x + c = 0
      -c <c>                enter argument c for a * x ** 2 + b * x + c = 0
      -log <name of log file>
                            name of logfile
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -a 1 -b 10 -c 2
    (-9.79583152331272, -0.2041684766872809)
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -a 1 -b 0 -c -0
    0.0
    (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -a 1 -b 2 -c 20
    ((-1.0, -4.358898943540674), (-1.0, 4.358898943540674))
    (venv) PS C:\Work\python\dz3\Py3HW15>

    Файл quad.log
    2023-07-10 14:28:32,583 - root - INFO     Выполнена функция my_log_quad_equat(1.0, 10.0, 2.0) = (-9.79583152331272, -0.2041684766872809)
    2023-07-10 14:28:45,383 - root - INFO     Выполнена функция my_log_quad_equat(1.0, 0.0, -0.0) = 0.0
    2023-07-10 14:28:54,194 - root - INFO     Выполнена функция my_log_quad_equat(1.0, 2.0, 20.0) = ((-1.0, -4.358898943540674), (-1.0, 4.358898943540674))