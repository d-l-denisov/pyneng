#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
    '''
    Function receives configuration filename (config_filename), parses it and returns
    tuple that contain 2 dictionaries (accsess port: vlan and trunk port: vlan list)
    '''
    
    with open(config_filename) as f:
        intf_list = []
        vlan_list = []
        for line in f:
            line = line.strip()
            if line.startswith('interface'):
                intf_list.append(line.split()[-1].rstrip())
                vlan_list.append(None)
            if 'switchport access vlan' in line:
                vlan_list[-1] = int(line.split()[-1])
            elif 'switchport trunk allowed vlan' in line:
                vlan_list[-1] = [int(vlan) for vlan in line.split()[-1].split(',')]

        return (dict(e for e in zip(intf_list, vlan_list) if e[1] and type(e[1]) == int),
                dict(e for e in zip(intf_list, vlan_list) if e[1] and type(e[1]) == list)) 
        

from sys import argv

print(get_int_vlan_map(argv[1]))

