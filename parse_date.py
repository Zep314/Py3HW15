import my_utils8 as mu8
import argparse
from datetime import datetime

@mu8.my_logger_decorator(level='info')
def my_str_to_date(text):
    return mu8.parse_date(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parsing dates')
    parser.add_argument('-amount', metavar='<amount of week>', type=str, help='enter amount of days', default='1')
    parser.add_argument('-dow', metavar='<day of week>', type=str, help='enter day of week', default=str(datetime.now().weekday() + 1))
    parser.add_argument('-month', metavar='<month>', type=str, help='enter day of week', default=str(datetime.now().month))
    args = parser.parse_args()
    param = f'{args.amount} {args.dow} {args.month}'
    print(f'{param} -> {my_str_to_date(param)}')
