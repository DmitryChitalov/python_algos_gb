"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from random import randint
from collections import deque
from timeit import timeit


def remove_left_deque(deq, count=0):
	deq_fun = deq.copy()
	for i in range(count):
		deq_fun.popleft()
	return deq_fun


def remove_left_list(lst, count=0):
	lst_fun = lst.copy()
	for i in range(count):
		lst_fun.pop(0)
	return lst_fun


if __name__ == '__main__':
	# simple_lst = [randint(0, 100) for i in range(100)]
	simple_lst = [i for i in range(100)]
	deq_obj = deque(simple_lst)
	
	# print(remove_left_deque(deq_obj, 50))
	# print(remove_left_list(simple_lst, 50))
	
	print('Функция remove_left_deque: ', end='')
	print(
		timeit(
			'remove_left_deque(deq_obj, 50)',
			setup='from __main__ import remove_left_deque, deq_obj',
			number=100000))
	print('Функция remove_left_list:  ', end='')
	print(
		timeit(
			'remove_left_list(simple_lst, 50)',
			setup='from __main__ import remove_left_list, simple_lst',
			number=100000))
