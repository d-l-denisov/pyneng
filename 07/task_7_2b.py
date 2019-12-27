#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

filename = argv[1]

with open(filename) as src_f, open('./config_sw1_cleared.txt', 'w') as dst_f:
    for line in src_f:
        if not set(line.split()).intersection(set(ignore)):
            dst_f.write(line)

