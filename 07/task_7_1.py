#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('./ospf.txt') as f:
    for line in f:
        line = line.split()
        print('{:24}{:20}\n'.format('Protocol:', 'OSPF' if line[0] == 'O' else 'Unknown'),
              '{:24}{:20}\n'.format('Prefix:', line[1]),
              '{:24}{:20}\n'.format('AD/Metric:', line[2].strip('[]')),
              '{:24}{:20}\n'.format('Next Hop:', line[4].rstrip(',')),
              '{:24}{:20}\n'.format('Last Update:', line[5].rstrip(',')),
              '{:24}{:20}\n'.format('Outbound Interface:', line[6]),
              sep = ''
             )

