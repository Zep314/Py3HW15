"""
Вычисление корней квадратного уравнения (включая комплексные), с логированием и возможностью запуска из командной строки
"""
import my_utils8 as mu8
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving a quadratic equation')
    parser.add_argument('-a', metavar='<a>', type=float, help='enter argument a for a * x ** 2 + b * x + c = 0',
                        default=1)
    parser.add_argument('-b', metavar='<b>', type=float, help='enter argument b for a * x ** 2 + b * x + c = 0',
                        default=0)
    parser.add_argument('-c', metavar='<c>', type=float, help='enter argument c for a * x ** 2 + b * x + c = 0',
                        default=0)
    parser.add_argument('-log', metavar='<name of log file>', type=str, help='name of logfile', default='quad.log')
    args = parser.parse_args()

    @mu8.my_logger_decorator(log_file_name=args.log, level='info')
    def my_log_quad_equat(a, b, c):
        return mu8.find_roots(a, b, c)

    print(my_log_quad_equat(args.a, args.b, args.c))

# Результат работы:
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -h
# usage: dz_my_quad_equat.py [-h] [-a <a>] [-b <b>] [-c <c>] [-log <name of log file>]
#
# Solving a quadratic equation
#
# options:
#   -h, --help            show this help message and exit
#   -a <a>                enter argument a for a * x ** 2 + b * x + c = 0
#   -b <b>                enter argument b for a * x ** 2 + b * x + c = 0
#   -c <c>                enter argument c for a * x ** 2 + b * x + c = 0
#   -log <name of log file>
#                         name of logfile
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -a 1 -b 10 -c 2
# (-9.79583152331272, -0.2041684766872809)
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -a 1 -b 0 -c -0
# 0.0
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_quad_equat.py -a 1 -b 2 -c 20
# ((-1.0, -4.358898943540674), (-1.0, 4.358898943540674))
# (venv) PS C:\Work\python\dz3\Py3HW15>

# Файл quad.log
# 2023-07-10 14:28:32,583 - root - INFO     Выполнена функция my_log_quad_equat(1.0, 10.0, 2.0) =
# (-9.79583152331272, -0.2041684766872809)
# 2023-07-10 14:28:45,383 - root - INFO     Выполнена функция my_log_quad_equat(1.0, 0.0, -0.0) = 0.0
# 2023-07-10 14:28:54,194 - root - INFO     Выполнена функция my_log_quad_equat(1.0, 2.0, 20.0) =
# ((-1.0, -4.358898943540674), (-1.0, 4.358898943540674))