#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

net = argv[1]

net = net.split('.')
net.extend(net.pop().split('/'))

print('Network:')

s_net = '{:08b}'.format(int(net[0])) + \
        '{:08b}'.format(int(net[1])) + \
        '{:08b}'.format(int(net[2])) + \
        '{:08b}'.format(int(net[3]))

s_net = s_net[0:int(net[-1])] + '0' * (32 - int(net[-1]))

print('{:<10}'.format(int(s_net[0:8], 2)),
      '{:<10}'.format(int(s_net[8:16], 2)),
      '{:<10}'.format(int(s_net[16:24], 2)),
      '{:<10}'.format(int(s_net[24:], 2)),
      '\n',
      '{:8}'.format(s_net[0:8]), '  ',
      '{:8}'.format(s_net[8:16]), '  ',
      '{:8}'.format(s_net[16:24]), '  ',
      '{:8}'.format(s_net[24:]), '\n',
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

