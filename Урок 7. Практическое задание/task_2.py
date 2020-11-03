"""
2. Отсортируйте по возрастанию 'методом слияния' одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random


def sort_lst(lst):
	len_lst = len(lst)
	if len_lst < 2:
		return lst
	left_part = sort_lst(lst[:len_lst // 2])
	right_part = sort_lst(lst[len_lst // 2:len_lst])

	i = j = 0
	res = []
	while i < len(left_part) or j < len(right_part):
		if not i < len(left_part):
			res.append(right_part[j])
			j += 1
		elif not j < len(right_part):
			res.append(left_part[i])
			i += 1
		elif left_part[i] < right_part[j]:
			res.append(left_part[i])
			i += 1
		else:
			res.append(right_part[j])
			j += 1
	return res


if __name__ == '__main__':
	arr1 = [(random() * 50) for _ in range(5)]

	print(arr1)
	arr1 = sort_lst(arr1)
	print(arr1)


