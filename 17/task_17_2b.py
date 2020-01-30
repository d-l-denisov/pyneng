#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


from sys import argv
from pprint import pprint
import yaml

from draw_network_graph import draw_topology


def transform_topology(yaml_file):
    with open(yaml_file) as f:
        data = yaml.load(f) 
    #pprint(data)
    result = {}
    for d in data:
        for e in data[d]:
            tmp = tuple(data[d][e].items())[0]
            if tmp not in tuple(result.keys()):
                result[(d, e)] = tmp

        #result[(d, e)] = tuple(data[d][e].items())[0] for e in data[d] \
        #                 if tuple(data[d][e].items())[0] not in tuple(result.keys())}
    return result


if __name__ == '__main__':
    pprint(transform_topology(argv[1]))
    #draw_topology(transform_topology(argv[1]), 'task_17_2b_topology_done')
