#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''

from sys import argv
from pprint import pprint
import re

def parse_sh_ip_int_br(filename):
    result = []
    with open(filename) as f:
        lines = f.read()
        match = re.finditer(r'(\S+) +(\S+) .+ (up|down|aministratively down) +(up|down)', lines)
        result = [m.groups() for m in match]
    return result

if __name__ == '__main__':
    pprint(parse_sh_ip_int_br(argv[1]))
