"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def sum_sequence(count):
	if count == 0:
		return 0
	elif count == 1:
		return 1
	else:
		sign = 1 if count % 2 == 1 else -1
		return (1 / 2**(count-1)) * sign + sum_sequence(count - 1)


if __name__ == '__main__':
	print(sum_sequence(3))
