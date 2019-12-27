#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan = input('Enter VLAN number: ')

with open('./CAM_table.txt') as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit():
            line[0] = int(line[0])
            if line[0] == int(vlan):
                print('{:<9}'.format(line[0]),
                     '{:17}'.format(line[1]),
                     '{:5}'.format(line[3]),
                     sep = ''
                     )

