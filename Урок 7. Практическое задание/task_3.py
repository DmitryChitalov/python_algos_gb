"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from random import randint
from timeit import timeit, Timer
from statistics import median


def gnome(data):
	i, size = 1, len(data)
	while i < size:
		if data[i - 1] <= data[i]:
			i += 1
		else:
			data[i - 1], data[i] = data[i], data[i - 1]
			if i > 1:
				i -= 1
	return data


arr1 = [randint(0, 1000) for _ in range(100)]
print(arr1)
arr1 = gnome(arr1)
print('### :', arr1)

print('функция гномьей сортировки 1 варриант: ', timeit('gnome(arr1[:])',
                                                        'from __main__ import gnome, arr1',
                                                        number=100000), 'seconds')

def with_sort(lst_obj):
	temp = lst_obj
	left_list = []
	right_list = []

	for i in range(len(temp)):

		for j in range(len(temp)):
			if temp[i] > temp[j]:
				left_list.append(temp[j])
			if temp[i] < temp[j]:
				right_list.append(temp[j])
			if temp[i] == temp[j] and i > j:
				left_list.append(temp[j])
			if temp[i] == temp[j] and i < j:
				right_list.append(temp[j])
		if len(left_list) == len(right_list):
			return temp[i]

	left_list.clear()
	right_list.clear()


arr1 = [randint(0, 100) for _ in range(10)]
print(arr1[:])
print('медиана списка: ', median(arr1[:]))
arr1 = with_sort(arr1[:])
print('Медиана: ', arr1)

















