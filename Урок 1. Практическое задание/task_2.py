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

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(0, 100))

print(numbers)		

#Алгоритм 1

def check1(numbers):
	min_ = numbers[0]
	for n in numbers:
		for m in numbers:
			if min_>m:
				min_ = m
	return(min_)

print(check1(numbers))


#Алгоритм 2
def check_2(numbers):
	numbers_copy = list(numbers)
	numbers_copy.sort()
	return(numbers_copy[0])

print(check_2(numbers))


#Алгоритм 2, второй вариант
def check_2_v2(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers[i]


print(check_2_v2(numbers))