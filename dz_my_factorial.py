"""
Вычисление факториала с логированием и возможностью запуска из командной строки
"""
import my_utils8 as mu8
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving factorial')
    parser.add_argument('-n', metavar='<f!(n)>', type=int, help='enter argument for solving factorial', default=1)
    parser.add_argument('-log', metavar='<name of log file>', type=str, help='name of logfile', default='factorial.log')
    args = parser.parse_args()

    @mu8.my_logger_decorator(log_file_name=args.log, level='info')
    def my_log_factorial(n):
        return mu8.MyFactorial(n)

    print(my_log_factorial(args.n))

# Результат работы:
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_factorial.py -h
# usage: dz_my_factorial.py [-h] [-n <f!n>] [-log <name of log file>]
#
# Solving factorial
#
# options:
#   -h, --help            show this help message and exit
#   -n <f!(n)>            enter argument for solving factorial
#   -log <name of log file>
#                         name of logfile
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_factorial.py -n 5
# 120
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_factorial.py -n -5
# None
# (venv) PS C:\Work\python\dz3\Py3HW15>

# Файл factorial.log
# 2023-07-10 14:22:03,543 - root - INFO     Выполнена функция my_log_factorial(5) = 120
# 2023-07-10 14:22:30,202 - root - INFO     Выполнена функция my_log_factorial(-5) = None
# 2023-07-10 14:23:57,424 - root - ERROR    Ошибка! MyValueError, Факториал от отрицательного числа не считаем!
