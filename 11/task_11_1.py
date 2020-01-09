#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


def parse_cdp_neighbors(command_output):
    """
    Function receives output of show cdp neighbor command as single line string,
    parses it and returns dictionary that describes devices interconnection

    Example:

    R4>show cdp neighbors
    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0

    Function return:

        {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
         ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

    """
    dev_a = command_output[:command_output.find('>')].strip()
    lines = [ l for l in command_output[command_output.find('Device ID'):].split('\n')[1:] if l ]
    d_res = {}
    for line in lines:
        dev_b, dev_a_intf_type, dev_a_intf_num, *_, dev_b_intf_type, dev_b_intf_num = line.split()
        d_res[(dev_a, dev_a_intf_type + dev_a_intf_num)] = (dev_b, dev_b_intf_type + dev_b_intf_num)
    return d_res


from sys import argv


if __name__ == "__main__":
    with open(argv[1]) as f:
        cdp_output = f.read()
    
        print(parse_cdp_neighbors(cdp_output))

