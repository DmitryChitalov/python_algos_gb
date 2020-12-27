"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
def min(list):
	for i in list:
		min = True
		for n in list:
			if i > n:
				min = False
		if min:
			return i

def min_2(list):
	min = list[0]
	for i in list:
		if min > i:
			min = i
	return min

list = [3531, 20, 543, 33, 2, 942, 3333, 144, 6]

print(min(list))
print(min_2(list))
