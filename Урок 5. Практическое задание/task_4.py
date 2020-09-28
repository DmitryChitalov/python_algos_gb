"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import collections
from timeit import timeit


def filling_dict(n=0):
	return {i: i for i in range(n)}


def filling_OrderedDict(n=0):
	NEW_DICT = collections.OrderedDict([(i, i) for i in range(n)])
	return NEW_DICT


def dict_add_one(dct):
	dct_copy = dct.copy()
	for k, v in dct_copy.items():
		dct_copy[k] += 1
	return dct_copy


def odict_add_one(odct):
	odct_copy = odct.copy()
	for k, v in odct_copy.items():
		odct_copy[k] += 1
	return odct_copy


if __name__ == '__main__':
	dct = filling_dict(100)
	odct = filling_OrderedDict(100)
	# print(odct)
	# print(dct)
	# print(dict_add_one(dct))
	# print(odict_add_one(odct))
	
	print('Функция filling_dict: ', end='')
	print(
		timeit(
			'filling_dict(100)',
			setup='from __main__ import filling_dict',
			number=10000))
	print('Функция filling_OrderedDict:  ', end='')
	print(
		timeit(
			'filling_OrderedDict(100)',
			setup='from __main__ import filling_OrderedDict',
			number=10000))
	print()
	print('Функция dict_add_one: ', end='')
	print(
		timeit(
			'dict_add_one(dct)',
			setup='from __main__ import dict_add_one, dct',
			number=10000))
	print('Функция odict_add_one:  ', end='')
	print(
		timeit(
			'odict_add_one(odct)',
			setup='from __main__ import odict_add_one, odct',
			number=10000))

"""
Функция filling_dict: 0.0714106
Функция filling_OrderedDict:  0.3884862

Функция dict_add_one: 0.1354646
Функция odict_add_one:  0.37659260000000006

Судя поп полученным измерниям обычный словарь быстрей OrderedDict
"""
