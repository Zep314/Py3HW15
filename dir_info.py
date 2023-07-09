# Задание No6
# - Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# - Соберите информацию о содержимом в виде объектов namedtuple.
# - Каждый объект хранит:
#   - имя файла без расширения или название каталога,
#   - расширение, если это файл,
#   - флаг каталога,
#   - название родительского каталога.
#   - В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
import argparse
import os
from collections import namedtuple

class MyDirInfo:
    DirItem = namedtuple("DirItem", "name ext is_dir root")
    files = []
    logging = logging

    def __init__(self, root):

        self.root = root
        self.scan(self.root)

    def scan(self, path):
        filename, ext = os.path.splitext(path)
        self.files.append(self.DirItem(name=filename, ext="", is_dir=True, root=path))
        for dr in os.listdir(path):
            obj_path = os.path.join(path, dr)
            if not os.path.isdir(obj_path):
                filename, ext = os.path.splitext(dr)
                self.files.append(self.DirItem(name=filename, ext=ext, is_dir=False, root=path))
            else:
                self.files.append(self.DirItem(name=dr, ext="", is_dir=True, root=path))
                self.scan(obj_path)

    def __str__(self):
        return str(self.files)

    def save_to_txt(self, filename):
        log_fmt = '{levelname:<4}: {message}'
        self.logging.basicConfig(format=log_fmt,
                                 filemode='w',
                                 style='{',
                                 filename=filename,
                                 encoding='utf-8',
                                 level=self.logging.INFO)
        for file in self.files:
            self.logging.info(f'[{file.name=}, {file.ext=}, {file.is_dir=}, {file.root=}]')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parsing directories')
    parser.add_argument('-indir', metavar='<Initial directory>', type=str, help='Initial dir for parsing', default='/home/dima/Видео')
    args = parser.parse_args()

    my_dir_info = MyDirInfo(args.indir)
    print(my_dir_info)
    my_dir_info.save_to_txt('dir_info.txt')