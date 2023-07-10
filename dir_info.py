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
    """
    Класс для сканирования содержимого каталога со всеми вложениями
    """
    DirItem = namedtuple("DirItem", "name ext is_dir root")
    files = []
    logging = logging

    def __init__(self, root):
        self.root = root
        self.scan(self.root)  # При создании объекта - сразу выполняем сканирования указанного каталога

    def scan(self, path):
        """
        Рекурсивное сканирование каталога с сохранением результатов в списке
        :param path:
        :return:
        """
        filename, ext = os.path.splitext(path)
        self.files.append(self.DirItem(name=filename, ext="", is_dir=True, root=path))
        for dr in os.listdir(path):
            obj_path = os.path.join(path, dr)
            if not os.path.isdir(obj_path):
                filename, ext = os.path.splitext(dr)
                self.files.append(self.DirItem(name=filename, ext=ext[1:], is_dir=False, root=path))
            else:
                self.files.append(self.DirItem(name=dr, ext="", is_dir=True, root=path))
                self.scan(obj_path)

    def __str__(self):
        return str(self.files)

    def save_to_txt(self, filename):
        """
        Сохранение результатов в текстовом файле с помощью logging
        :param filename:
        :return:
        """
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
    parser.add_argument('-indir',
                        metavar='<Initial directory>',
                        type=str,
                        help='Initial dir for parsing',
                        default='C:\\VIDEO')
    parser.add_argument('-outfile',
                        metavar='<Output file>',
                        type=str,
                        help='Text file for store result',
                        default='dir_info.txt')
    args = parser.parse_args()

    my_dir_info = MyDirInfo(args.indir)
    my_dir_info.save_to_txt(args.outfile)

# Результат работы:
# C:\Work\python\dz3\Py3HW15\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW15/dir_info.py
#
# Process finished with exit code 0

# Файл dir_info.txt:
# INFO: [file.name='C:\\VIDEO', file.ext='', file.is_dir=True, file.root='C:\\VIDEO']
# INFO: [file.name='100 дней на жизнь.2019.1080p.AMZN.WEB-DL.ELEKTRI4KA.UNIONGANG', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='21.2008.BDRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Army_of_Thieves_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Beshenstvo.2023.WEB-DL.1080p', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Besprincipnye.v.derevne.2023.WEB-DL.1080p', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='FILE20210419-173754-000011', file.ext='MP4', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='FILE20210419-173824-000012', file.ext='MP4', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Glass.Onion.A.Knives.Out.Mystery.(2022).WEB-DL.1080p.Theseus', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Gorko.2.2014.RUS.BDRip.XviD.AC3.-HQCLUB', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich', file.ext='', file.is_dir=True, file.root='C:\\VIDEO']
# INFO: [file.name='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e01.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e02.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e03.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e04.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e05.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e06.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e07.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e08.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e09.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.e10.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.2022.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich', file.ext='', file.is_dir=True, file.root='C:\\VIDEO']
# INFO: [file.name='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e01.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e01.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e02.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e02.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e03.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e03.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e04.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e04.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e05.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e05.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e06.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e06.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e07.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e07.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e08.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e08.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e09.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e09.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e10.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='I.snova.zdravstvuyte.s02e10.WEB-DLRip.25Kuzmich', file.ext='srt', file.is_dir=False, file.root='C:\\VIDEO\\I.snova.zdravstvuyte.S02.WEB-DLRip.25Kuzmich']
# INFO: [file.name='NO20210508-210743-000021F', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Nyurnberg.2023.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='PICT0285', file.ext='AVI', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='PICT0285.AVI', file.ext='sfk', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Poslednij.klient.2022.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Record', file.ext='', file.is_dir=True, file.root='C:\\VIDEO']
# INFO: [file.name='C:\\VIDEO\\Record', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Record']
# INFO: [file.name='2022-10-06 13-05-08', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO\\Record']
# INFO: [file.name='2022-10-06 13-05-08', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO\\Record']
# INFO: [file.name='2022-10-06 13-05-08.mp4', file.ext='sfk', file.is_dir=False, file.root='C:\\VIDEO\\Record']
# INFO: [file.name='out', file.ext='gif', file.is_dir=False, file.root='C:\\VIDEO\\Record']
# INFO: [file.name='Untitled', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO\\Record']
# INFO: [file.name='ssonya', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Turist.2010.HDRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Untitled', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='[Anf].Avatar.The.Way.of.Water.(2022).DUB.TC. [1080p-LQ]', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='[PB.wtf].1286204', file.ext='torrent', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='ГИС РСО онлайн 29 .11.2022', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='Прочь (2017) BDRip-AVC_ivanes20031987', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO']
# INFO: [file.name='регистратор', file.ext='', file.is_dir=True, file.root='C:\\VIDEO']
# INFO: [file.name='C:\\VIDEO\\регистратор', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\регистратор']
# INFO: [file.name='FILE20210529-175622-001381', file.ext='MP4', file.is_dir=False, file.root='C:\\VIDEO\\регистратор']
# INFO: [file.name='NO20210621-202406-001724F', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO\\регистратор']
# INFO: [file.name='NO20210621-202706-001725F', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO\\регистратор']
# INFO: [file.name='NO20210827-140448-001872F', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO\\регистратор']
# INFO: [file.name='_NO20210627-130907-000530F', file.ext='mp4', file.is_dir=False, file.root='C:\\VIDEO\\регистратор']
# INFO: [file.name='Сериалы', file.ext='', file.is_dir=True, file.root='C:\\VIDEO']
# INFO: [file.name='C:\\VIDEO\\Сериалы', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='Fisher.S01.WEB-DLRip.25Kuzmich', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e01.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e02.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e03.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e04.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e05.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e06.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e07.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Fisher.s01e08.WEB-DLRip.25Kuzmich', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Fisher.S01.WEB-DLRip.25Kuzmich']
# INFO: [file.name='Maigret.HDRip-AVC', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Maigret', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC']
# INFO: [file.name='Maigret.s01.HDRip-AVC', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s01', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s01.HDRip-AVC']
# INFO: [file.name='Maigret.s01e01.Maigret.Sets.a.Trap.HDRip-AVC', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s01.HDRip-AVC']
# INFO: [file.name='Maigret.s01e02.Maigrets.Dead.Man.HDRip-AVC', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s01.HDRip-AVC']
# INFO: [file.name='Maigret.s02.HDRip-AVC', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s02', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s02.HDRip-AVC']
# INFO: [file.name='Maigret.s02e01.Maigret.Night.at.the.Crossroads.HDRip-AVC', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s02.HDRip-AVC']
# INFO: [file.name='Maigret.s02e02.Maigret.in.Montmartre.HDRip-AVC', file.ext='mkv', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Maigret.HDRip-AVC\\Maigret.s02.HDRip-AVC']
# INFO: [file.name='Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E01_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E02_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E03_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E04_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E05_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E06_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Mare_of_Easttown_S01_E07_2021_WEB-DLRip_NM_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Mare_of_Easttown_S01_2021_WEB-DLRip_NM_by_Dalemake']
# INFO: [file.name='Ordeal by Innocence', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Ordeal by Innocence', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Ordeal by Innocence']
# INFO: [file.name='Ordeal.by.Innocence.s01e01.LostFilm', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Ordeal by Innocence']
# INFO: [file.name='Ordeal.by.Innocence.s01e02.LostFilm', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Ordeal by Innocence']
# INFO: [file.name='Ordeal.by.Innocence.s01e03.LostFilm', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Ordeal by Innocence']
# INFO: [file.name='Perry.Mason.S01.WEB-DL.NewStudio', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e01.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e02.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e03.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e04.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e05.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e06.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e07.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='Perry.Mason.s01e08.WEB-DL.Rus.Eng.NewStudio.RGzsRutracker', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Perry.Mason.S01.WEB-DL.NewStudio']
# INFO: [file.name='The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S01.MVO.SDI.Media.WEB-DLRip', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S01.MVO.SDI.Media', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S01.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S01E01.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S01.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S01E02.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S01.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S01E03.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S01.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S02.MVO.SDI.Media.WEB-DLRip', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S02.MVO.SDI.Media', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S02.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S02E01.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S02.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S02E02.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S02.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S02E03.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S02.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The.Bletchley.Circle.S02E04.MVO.SDI.Media.WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The.Bletchley.Circle.MVO.SDI.Media.WEB-DLRip\\The.Bletchley.Circle.S02.MVO.SDI.Media.WEB-DLRip']
# INFO: [file.name='The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='The_Chestnut_Man_S01_E01_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='The_Chestnut_Man_S01_E02_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='The_Chestnut_Man_S01_E03_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='The_Chestnut_Man_S01_E04_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='The_Chestnut_Man_S01_E05_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='The_Chestnut_Man_S01_E06_2021_WEB-DLRip_by_Dalemake', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\The_Chestnut_Man_S01_2021_WEB-DLRip_by_Dalemake']
# INFO: [file.name='Дублинские убийства. Сезон 1', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы']
# INFO: [file.name='C:\\VIDEO\\Сериалы\\Дублинские убийства', file.ext='', file.is_dir=True, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E01.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E02.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E03.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E04.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E05.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E06.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E07.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Dublin.Murders.S01E08.WEB-DLRip.Rus.Eng', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO\\Сериалы\\Дублинские убийства. Сезон 1']
# INFO: [file.name='Убийство в Париже_2023_WEB-DLRip', file.ext='avi', file.is_dir=False, file.root='C:\\VIDEO']
