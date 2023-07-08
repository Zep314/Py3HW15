import my_utils8 as mu8
import argparse


@mu8.my_logger_decorator(level='info')
def my_str_to_date(text):
    return mu8.parse_date(text)


if __name__ == '__main__':
    pass
