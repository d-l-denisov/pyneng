#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

while True:
    ip = input('Enter IP address: ')
    try:
        ip = ip.split('.')
        if len(ip) == 4:
            for indx in range(4):
                ip[indx] = int(ip[indx])
                if ip[indx] < 0 or ip[indx] > 255:
                    int('nan')
            break

    except ValueError:
        pass
    print('Wrong IP address')

if 1 <= ip[0] <= 223:
    print('unicast')
elif 224 <= ip[0] <= 239:
    print('multicast')
elif ip.count(255) == 4:
    print('local broadcast')
elif ip.count(0) == 4:
    print('unassigned')
else:
    print('unused')

