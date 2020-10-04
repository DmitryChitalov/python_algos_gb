"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
from timeit import timeit


def bubble_sort(lst_obj_in):
	lst_obj = lst_obj_in.copy()
	n = 1
	while n < len(lst_obj):
		for i in range(len(lst_obj) - n):
			if lst_obj[i] < lst_obj[i + 1]:
				lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
		n += 1
	return lst_obj


def bubble_sort_up(lst_obj_in):
	lst_obj = lst_obj_in.copy()
	n = 1
	sort_end = 0
	while n < len(lst_obj):
		for i in range(len(lst_obj) - n):
			if lst_obj[i] < lst_obj[i + 1]:
				lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
				if sort_end == 0:
					sort_end = 1
		if sort_end == 0:
			return lst_obj
		n += 1
		sort_end = 0
	return lst_obj


if __name__ == '__main__':
	orig_list = [random.randint(-100, 100) for _ in range(10)]
	print(f'Исходный масив:        {orig_list}')
	print(f'Отсортированный масив: {bubble_sort(orig_list)}')
	print()
	print(f'Исходный масив:        {orig_list}')
	print(f'Отсортированный масив: {bubble_sort_up(orig_list)}')
	
	print()
	print(f'Время сортировки функции bubble_sort:    ', end='')
	print(
		timeit(
			"bubble_sort(orig_list)",
			setup='from __main__ import bubble_sort, orig_list',
			number=1000000))
	print(f'Время сортировки функции bubble_sort_up: ', end='')
	print(
		timeit(
			"bubble_sort_up(orig_list)",
			setup='from __main__ import bubble_sort_up, orig_list',
			number=1000000))

'''
Исходный масив:        [-65, 61, 100, -23, 25, -49, 36, -8, -87, -56]
Отсортированный масив: [100, 61, 36, 25, -8, -23, -49, -56, -65, -87]

Время сортировки функции bubble_sort:    15.2973429
Время сортировки функции bubble_sort_up: 12.390383500000002

Оптимизыция функции немного ускорила время сортировки, но не значилельно, а иногда время почти не отличается
'''