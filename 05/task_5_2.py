#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

net = input("Enter IP network (net/mask): ")

net = net.split('.')
net.extend(net.pop().split('/'))

print('Network:')

print('{:10}'.format(net[0]),
      '{:10}'.format(net[1]),
      '{:10}'.format(net[2]),
      '{:10}'.format(net[3]),
      '\n',
      '{:08b}'.format(int(net[0])), '  ',
      '{:08b}'.format(int(net[1])), '  ',
      '{:08b}'.format(int(net[2])), '  ',
      '{:08b}'.format(int(net[3])), '\n',
     sep='')

print('Mask:')

print('/', net[4], sep = '')

mask = '1' * int(net[4]) + '0' * (32 - int(net[4]))
print('{:<10}'.format(int(mask[0:8], 2)),
      '{:<10}'.format(int(mask[8:16], 2)),
      '{:<10}'.format(int(mask[16:24], 2)),
      '{:<10}'.format(int(mask[24:], 2)),
      sep = '')

print('{:08b}'.format(int(mask[0:8], 2)), '  ',
      '{:08b}'.format(int(mask[8:16], 2)), '  ',
      '{:08b}'.format(int(mask[16:24], 2)), '  ',
      '{:08b}'.format(int(mask[24:], 2)), '  ',
      sep = '')

