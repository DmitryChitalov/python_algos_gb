"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit
text = 'C:/Users/egor/GeekBrains/python_algos_gb/Урок5'
list_ = text.split('/')
print(text)
mydict = {val:num for num, val in enumerate(list_)}
d= OrderedDict(mydict)
setup ='from __main__ import d, mydict'
print(d['Users'])
print(mydict)
print(timeit('d["Users"]',setup))
print(timeit('mydict["Users"]',setup))
print(timeit('d["Users2"]= 12',setup))
print(timeit('mydict["Users2"] = 12',setup))
print(timeit('d["Users3"]= 1252',setup))
print(timeit('mydict["Users3"] = 1252',setup))
print(d)
print(mydict)
"""Анализ чтение в случае обычного словаря и OrderedDict
Добавление нового элемента в случае обычного словаря быстрее"""