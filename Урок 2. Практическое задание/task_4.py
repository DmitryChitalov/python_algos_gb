"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def rec_method(i, numb, n_count, common_sum):
	"""Переписал из примера, сам не смог, не понял как это можно сделать"""
	if i == n_count:
		print(f"Кол-во элементов - {n_count}, их сумма - {common_sum}")
	elif i < n_count:
		return rec_method(i + 1, numb / 2 * -1, n_count, common_sum + numb)


try:
	N_COUNT = int(input("Enter the numbers of items: "))
	rec_method(0, 1, N_COUNT, 0)
except ValueError:
	print("Error!! You try to enter letters but need the numbers!!")