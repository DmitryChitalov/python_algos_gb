"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time


def function_execution_time(fun):
	def time_dec(el):
		start_val = time.time()
		fun(el)
		end_val = time.time()
		print(f'Время выполнения функции {fun}:  {end_val - start_val}')
	return time_dec


@function_execution_time
def my_list(el):
	lst = [i for i in range(el)]
	return lst


@function_execution_time
def my_dict(el):
	dct = {f'key{i}': i for i in range(el)}
	return dct


if __name__ == '__main__':
	
	dict_1 = my_dict(100000)
	list_1 = my_list(100000)
