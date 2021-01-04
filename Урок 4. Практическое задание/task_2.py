"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memorize(func):
	def wrapper(number, memory={}):
		r = memory.get(number)
		if r is None:
			r = func(number)
			memory[number] = r
		return r

	return wrapper


@memorize
def recursive_reverse(number):
	if number == 0:
		return str(number % 10)
	return f'{str(number % 10)}{recursive_reverse(number // 10)}'


a = 123456789

print(
	timeit.timeit(
		'recursive_reverse(a)',
		'from __main__ import recursive_reverse, a',
		number=1000))
'''
Время выполнения функции до оптимизации: 0.0044835840235464275
Время выполнения задачи послеоптимизации: 0.0001692090299911797. Использование мемоизации позволило сократить время выполненяи за счет сохранения результатов работы функции
'''

