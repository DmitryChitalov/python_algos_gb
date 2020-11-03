"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
	if number == 0:
		return str(number % 10)
	return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
	timeit(
		"recursive_reverse(num_100)",
		setup='from __main__ import recursive_reverse, num_100',
		number=100000))
print(
	timeit(
		"recursive_reverse(num_1000)",
		setup='from __main__ import recursive_reverse, num_1000',
		number=100000))
print(
	timeit(
		"recursive_reverse(num_10000)",
		setup='from __main__ import recursive_reverse, num_10000',
		number=100000))


def memoize(f):
	cache = {}

	def decorate(*args):

		if args in cache:
			return cache[args]
		else:
			cache[args] = f(*args)
			return cache[args]

	return decorate


# так то,в этой ф-ции, идет выборка последнего числа с последующим уменьшением "number" списка(удалением
# выведеного числа), мемоизация не нужна, по идее, но по замерам почему то код быстрее....
#
# я так понимаю, оптимизация выражается в том, что при нулевом значении просто возвращается null, а не идет анализ
# последнего значения с его подальшим выводом? И из-за этого так сильно экономим время? если это так, то я в шоке,
# из-за такой мелкой части так возрастает производительность...
#
# с мемоизацией:
# 0.008068604991422035, 0.009427, 0.0111101
# без мемоизации:
# 0.055013220099574514, 0.0793041270080721, 0.3963181330036605
# #######################
# 100 000 без мемоизации:
# 0.5235821180103812
# 0.6129620029969374
# 1.2494449180085212
#
# 100 000 с мемоизацией:
# 0.06475572499039117
# 0.06462229999306146
# 0.06748099099786486
@memoize
def recursive_reverse_mem(number):
	if number == 0:
		return ''
	return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
	timeit(
		stmt='recursive_reverse_mem(num_100)',
		setup='from __main__ import recursive_reverse_mem, num_100',
		number=100000))
print(
	timeit(
		'recursive_reverse_mem(num_1000)',
		setup='from __main__ import recursive_reverse_mem, num_1000',
		number=100000))
print(
	timeit(
		'recursive_reverse_mem(num_10000)',
		setup='from __main__ import recursive_reverse_mem, num_10000',
		number=100000))
