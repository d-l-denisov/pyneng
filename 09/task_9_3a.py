#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
- добавить поддержку конфигурации, когда настройка access-порта выглядит так:
    interface FastEthernet0/20
     switchport mode access
     duplex auto
  То есть, порт находится в VLAN 1

  В таком случае, в словарь портов должна добавляться информация,
  что порт в VLAN 1
  Пример словаря: {
                   'FastEthernet0/12': 10,
                   'FastEthernet0/14': 11,
                   'FastEthernet0/20': 1
                   }

У функции  должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного
файла. Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def get_int_vlan_map(config_filename):
    '''
    Function receives configuration filename (config_filename), parses it and returns
    2 dictionaries (accsess port: vlan and trunk port: vlan list)
    '''
    
    with open(config_filename) as f:
        intf_list = []
        vlan_list = []
        for line in f:
            if line.startswith('interface') and 'Ethernet' in line:
                intf_list.append(line.split()[-1].rstrip())
                vlan_list.append(1)
            if 'switchport access vlan' in line:
                vlan_list[-1] = int(line.split()[-1])
            elif 'switchport trunk allowed vlan' in line:
                vlan_list[-1] = [int(vlan) for vlan in line.split()[-1].split(',')]

        return (dict(e for e in zip(intf_list, vlan_list) if type(e[1]) == int),
                dict(e for e in zip(intf_list, vlan_list) if type(e[1]) == list)) 
        

from sys import argv

print(get_int_vlan_map(argv[1]))

