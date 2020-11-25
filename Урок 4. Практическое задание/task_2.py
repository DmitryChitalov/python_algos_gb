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
print(timeit("recursive_reverse(num_100)", setup='from __main__ import recursive_reverse, num_100', number=10000))
print(timeit("recursive_reverse(num_1000)", setup='from __main__ import recursive_reverse, num_1000', number=10000))
print(timeit("recursive_reverse(num_10000)", setup='from __main__ import recursive_reverse, num_10000', number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(timeit('recursive_reverse_mem(num_100)', setup='from __main__ import recursive_reverse_mem, num_100', number=10000))
print(timeit('recursive_reverse_mem(num_1000)', setup='from __main__ import recursive_reverse_mem, num_1000', number=10000))
print(timeit('recursive_reverse_mem(num_10000)', setup='from __main__ import recursive_reverse_mem, num_10000', number=10000))


def test(num):
    rev_num = str(num)[::-1]
    return rev_num


print('test')
print(timeit('test(num_100)', setup='from __main__ import test, num_100', number=10000))
print(timeit('test(num_1000)', setup='from __main__ import test, num_1000', number=10000))
print(timeit('test(num_10000)', setup='from __main__ import test, num_10000', number=10000))


def test_2(num):
    return ''.join(str(list(str(num)).reverse()))


print('test_2')
print(timeit('test_2(num_100)', setup='from __main__ import test_2, num_100', number=10000))
print(timeit('test_2(num_1000)', setup='from __main__ import test_2, num_1000', number=10000))
print(timeit('test_2(num_10000)', setup='from __main__ import test_2, num_10000', number=10000))

"""
Решение данной задачи через алгоритм мемоизации является очень эффективным решением и ускоряет исходныю рекурсивную 
функцию во много раз. Решения через срез и встроенную функцию reverse ускоряют исходную ф-ю, но алгоритму мемоизации
они уступают в скорости. С уверенностью можно сказать, что мемоизация является очень эффективным решением!
"""

