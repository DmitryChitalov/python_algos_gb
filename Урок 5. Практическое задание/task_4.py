"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit

setup = '''
from collections import OrderedDict

with open("presidents.txt", "r", encoding="utf-8") as presidents:
    text = presidents.read().split("\\n")

dict1 = {}
od_dict = OrderedDict()


def dict_add(text_list):
    for note in text_list:
        note_list = note.replace(")", "").split(" (")
        dict1.update({note_list[0]: note_list[1]})
        od_dict.update({note_list[0]: note_list[1]})
    return


def get_d_named(dict):
    res = {}
    for key in dict:
        if key.split()[1][0] == "Д":
            res.update({key: dict[key]})
    return res

dict_add(text)
'''

start = 'get_d_named(dict1.copy())'
start_od = 'get_d_named(od_dict.copy())'

print(f'Время словаря - {timeit(start, setup, number=1000)}')
print(f'Время OD - {timeit(start_od, setup, number=1000)}')

'''
Выводы: OrderedDict работает медленнее, чем dict. 
'''