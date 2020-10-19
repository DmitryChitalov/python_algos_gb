"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
"""
Судя по даным предоставленым из подсчета времени запусков timeit и cProfile
	мы видим что работа функции со срезами самая быстрая по времени и делает только 4 вызова базовых функцию,
	так как первая рекурсивная функция делает 20 вызовов и затрачивает огромное колличество времени,
	вторая функция, в принципе, показала средние результаты
"""
import timeit as t
import cProfile


def revers(enter_num, revers_num=0):
	if enter_num == 0:
		return revers_num
	else:
		num = enter_num % 10
		revers_num = (revers_num + num / 10) * 10
		enter_num //= 10
		return revers(enter_num, revers_num)


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


number = 2345543654635309

print("результат обработки данных: ", revers(number))
med_start_counter_revers = t.repeat(
	stmt='revers(number)',
	setup='from __main__ import revers, number',
	repeat=4,
	number=100000)
print(f"4 повторения 100000 запусков первой функции:\n{med_start_counter_revers}")
cProfile.run("revers(number)")

print("результат обработки данных: ", revers_2(number))
med_start_counter_revers_2 = t.repeat(
	stmt='revers_2(number)',
	setup='from __main__ import revers_2, number',
	repeat=4,
	number=100000)
print(f"4 повторения 100000 запусков второй функции:\n{med_start_counter_revers_2}")
cProfile.run("revers_2(number)")

print("результат обработки данных: ", revers_3(number))
med_start_counter_revers_3 = t.repeat(
	stmt='revers_3(number)',
	setup='from __main__ import revers_3, number',
	repeat=4,
	number=100000)
print(f"4 повторения 100000 запусков второй функции:\n{med_start_counter_revers_3}")
cProfile.run("revers_3(number)")

# print(timeit.timeit("x=sum(range(100))"))
