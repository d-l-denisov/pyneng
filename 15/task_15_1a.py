#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''


import re
from sys import argv
from pprint import pprint


def get_ip_from_cfg(filename):
    with open(filename) as f:
        line = f.read()
    regex = r'interface (?P<intf>\S+)\n.+?ip address (?P<ip_addr>\S+) (?P<ip_mask>\S+)\n'
    match = re.finditer(regex, line, re.DOTALL)
    return {m.group('intf'): m.group('ip_addr', 'ip_mask') for m in match}



if __name__ == "__main__":
    pprint(get_ip_from_cfg(argv[1]))
