#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''



ip = input('Enter IP address: ')
ip_ok = True
try:
    ip = ip.split('.')
    if len(ip) == 4:
        for indx in range(4):
            ip[indx] = int(ip[indx])
            if ip[indx] < 0 or ip[indx] > 255:
                ip_ok = False
    else:
        ip_ok = False
except (IndexError, ValueError):
    ip_ok = false

if ip_ok:
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
else:
    print('Wrong IP addess')
