#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
from sys import argv
from pprint import pprint


def get_ip_from_cfg_v1(filename):
    result = []
    with open(filename) as f:
        for line in f:
            match = re.search(r'ip address (\S+) (\S+)', line)
            if match:
                result.append(match.groups())
    return result

def get_ip_from_cfg_v2(filename):
    result = []
    with open(filename) as f:
        lines = f.read()
        match = re.finditer(r'ip address (\S+) (\S+)', lines)
        result = [(m.groups()) for m in match]
    return result


if __name__ == "__main__":
    pprint(get_ip_from_cfg_v2(argv[1]))
