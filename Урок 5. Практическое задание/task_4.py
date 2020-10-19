"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

string = "Выполните различные операции с каждым из объектов и сделайте замеры"
string = string.split(' ')


def norm_dict():
	dict1 = dict()
	for i in range(len(string)):
		dict1[i] = string[i]
	return dict1


def ordered_dict():
	dict2 = OrderedDict()
	for i in range(len(string)):
		dict2[i] = string[i]
	return dict2


print(norm_dict())
print(ordered_dict())

print("normal dict append numbers: ",
      timeit("norm_dict()",
             "from __main__ import norm_dict",
             number=10000))

print("OrderedDict append numbers: ",
      timeit("ordered_dict()",
             "from __main__ import ordered_dict",
             number=10000))


def del_from_dict(arr):
	x = arr.copy()
	# print(x)
	for el in arr:
		del x[el]

	return x, "пусто"


def del_from_ordereddict(arr):
	x = arr.copy()
	for el in arr:
		del x[el]

	return x, 'пусто'


del_from_dict(norm_dict())
del_from_ordereddict(ordered_dict())


print("normal dict deleted numbers: ",
      timeit("del_from_dict(norm_dict())",
             "from __main__ import del_from_dict, norm_dict",
             number=10000))

print("OrderedDict deleted numbers: ",
      timeit("del_from_ordereddict(ordered_dict())",
             "from __main__ import del_from_ordereddict, ordered_dict",
             number=10000))
