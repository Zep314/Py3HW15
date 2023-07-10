"""
Вычисление факториалов в указанном промежутке, с логированием и возможностью запуска из командной строки
"""
import my_utils8 as mu8
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return range of factorials')
    parser.add_argument('-start', metavar='<a>', type=int, help='enter argument for start solving of factorials',
                        default=1)
    parser.add_argument('-stop', metavar='<b>', type=int, help='enter argument for stop solving of factorials',
                        default=1)
    parser.add_argument('-step', metavar='<step>', type=int, help='enter argument for stop solving of factorials',
                        default=1)
    parser.add_argument('-log', metavar='<name of log file>', type=str, help='name of logfile', default='factorial.log')
    args = parser.parse_args()

    @mu8.my_logger_decorator(log_file_name=args.log, level='info')
    def my_log_range_factorial(start, stop, step):
        try:
            return [i for i in mu8.MyRangeFactorial(start, stop + 1, step)]
        except BaseException as e:
            print(f'Error! {e}')

    print(my_log_range_factorial(args.start, args.stop, args.step))

# Результат работы:
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_range_factorial.py -h
# usage: dz_my_range_factorial.py [-h] [-start <a>] [-stop <b>] [-step <step>] [-log <name of log file>]
#
# Return range of factorials
#
# options:
#   -h, --help            show this help message and exit
#   -start <a>            enter argument for start solving of factorials
#   -stop <b>             enter argument for stop solving of factorials
#   -step <step>          enter argument for stop solving of factorials
#   -log <name of log file>
#                         name of logfile
# (venv) PS C:\Work\python\dz3\Py3HW15> python .\dz_my_range_factorial.py -start 1 -stop 20 -step 3
# [1, 24, 5040, 3628800, 6227020800, 20922789888000, 121645100408832000]
# (venv) PS C:\Work\python\dz3\Py3HW15>

# Файл factorial.log
# 2023-07-10 14:27:09,298 - root - INFO     Выполнена функция my_log_range_factorial(1, 20, 3) = [1, 24, 5040, 3628800,
# 6227020800, 20922789888000, 121645100408832000]
