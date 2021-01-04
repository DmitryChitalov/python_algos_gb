"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
import timeit


def revers(enter_num, revers_num=0):
	if enter_num == 0:
		return
	else:
		num = enter_num % 10
		revers_num = (revers_num + num / 10) * 10
		enter_num //= 10
		revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
	while enter_num != 0:
		num = enter_num % 10
		revers_num = (revers_num + num / 10) * 10
		enter_num //= 10
	return revers_num


def revers_3(enter_num):
	enter_num = str(enter_num)
	revers_num = enter_num[::-1]
	return revers_num


a = 123456789


def main():
	revers(a)
	revers_2(a)
	revers_3(a)


cProfile.run('main()')

print(
	timeit.timeit('revers(a)', 'from __main__ import revers, a', number=1000))
print(
	timeit.timeit('revers_2(a)', 'from __main__ import revers_2, a', number=1000))
print(
	timeit.timeit('revers_3(a)', 'from __main__ import revers_3, a', number=1000))
'''
Время работы reverse: 0.003436166967730969
Время работы reverse_2: 0.002174832974560559
Время работы reverse_3: 0.0004098339704796672
Данные получение с помощью cProfile не позволяют выделить какой то алгоритм из 3х, т.к. время выполнения в целом не большое.
По данным модуля timeit, можно сделать вывод:
Эффективнее использовать функцию reverse_3 - самая быстрая по времени. 
Выполняются всего 2 операции: преобразование в строку(встроенная функция) и вывод строки в обратном порядке через slice.
'''

