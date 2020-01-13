#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv
import subprocess


def ping_ip_addresses(ip_list):
    """
    Function receives list of IP addresses and returns tuple with 2 list-elements: pingable IP
    and non-pingable IP addresses
    """

    t_res = ([], [])
    for ip in ip_list:
        sp_res= subprocess.run(['ping', '-c1', '-n', ip],
                       stdout = subprocess.DEVNULL,
                       stderr = subprocess.DEVNULL)
        if sp_res.returncode == 0:
            t_res[0].append(ip)
        else:
            t_res[1].append(ip)
    return t_res


if __name__ == '__main__':
    print('\n',ping_ip_addresses(argv[1:]))
