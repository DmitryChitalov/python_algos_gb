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
        return ''#str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
print(num_100, num_1000, num_10000)
print(recursive_reverse(55770))

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):
        #print(cache)
        if args in cache:
            #print(f'get from cash: {args}, {cache[args]}.')
            return cache[args]
        else:
            cache[args] = f(*args)
            #print(f'set to cash: {args}, {cache[args]}.')
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))


# Сначала хотелось бы сказать, что функция recursive_reverse
# содержит ошибку в строке, содержащей первый return.
# Например, число 55770 преобразуется в 077550.
# Код я поправил.
# Первоначально, судя по замерам, мемоизация ускоряет исходную функцию
# примерно в 10-20 раз.
# Но судя по анализу самой задачи, вероятность появления
# повторяющихся последовательностей цифр внутри числа крайне мала.
# Это показывает запуск данной функции с повтором в несколько раз
# с дебажными принтами: в первом запуске из кэша данные взялись один раз,
# при последующих, исходное число бралось из кэша сразу.
# Вывод 1: здесь предыдущие запуски влияют на последующие, поэтому
#          использовать timeit для этого некорректно.
# Вывод 2: кэширование имеет смысл, если будут повторяться исходные числа.
