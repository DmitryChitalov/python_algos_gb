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
        return ''               # здесь был косяк, добавляющий лишний символ "0" в результат
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def mine_reverse(number):
    return str(number)[::-1]

# даже такой неудачный метод, работающий с reversed оказывается в 2 раза быстрее рекурсии
def mine_reverse_v2(number):
    result = list(reversed(str(number)))
    num_rev = ''
    for i in result:
        num_rev += f"{i}"
    return num_rev


def start_timeit(func_name):
    print(f'Не оптимизированная функция {func_name}')
    print(
        timeit(
            f"{func_name}(num_100)",
            setup=f'from __main__ import {func_name}, num_100',
            number=10000))
    print(
        timeit(
            f"{func_name}(num_1000)",
            setup=f'from __main__ import {func_name}, num_1000',
            number=10000))
    print(
        timeit(
            f"{func_name}(num_10000)",
            setup=f'from __main__ import {func_name}, num_10000',
            number=10000))


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

# print(num_100)
# print(recursive_reverse(num_100))
# print(mine_reverse(num_100))
# print(mine_reverse_v2(num_100))

start_timeit('recursive_reverse')


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

start_timeit('mine_reverse')
start_timeit('mine_reverse_v2')
"""
Мемоизация безусловно нужна, т.к. она позволяет сократить количество повторных вычислений
Что даёт значительное сокращение затрачиваемого времени.
Однако отказ от рекурсии мог бы дать прирост производительности без введения мемоизации
Грубые методы типа reversed или среза, позволят сразу работать со строкой и производить разворот без вычислений
"""