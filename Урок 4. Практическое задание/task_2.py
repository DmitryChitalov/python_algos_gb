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
from random import randint

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

elem_1 = randint(10, 100000)
elem_2 = randint(1000000, 10000000)
elem_3 = randint(10000000, 100000000)

def memoized(func):
    memory = {}

    def memo(*args):
        if args in memory:
            return memory[args]
        else:
            memory[args] = func(*args)
            return memory[args]
    return memo

@memoized
def recursive_reverse_modified(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_modified(number // 10)}'

print(timeit.timeit("recursive_reverse(elem_1)", setup="from __main__ import recursive_reverse, elem_1", number=1000))
print(timeit.timeit("recursive_reverse(elem_2)", setup="from __main__ import recursive_reverse, elem_2", number=1000))
print(timeit.timeit("recursive_reverse(elem_3)", setup="from __main__ import recursive_reverse, elem_3", number=1000))
print(timeit.timeit("recursive_reverse_modified(elem_1)", setup="from __main__ import recursive_reverse_modified, elem_1", number=1000))
print(timeit.timeit("recursive_reverse_modified(elem_2)", setup="from __main__ import recursive_reverse_modified, elem_2", number=1000))
print(timeit.timeit("recursive_reverse_modified(elem_3)", setup="from __main__ import recursive_reverse_modified, elem_3", number=1000))

'''В данном случае имеем рекурсивную функцию. Использование мемоизации для рекурсии в десятки раз ускоряет работу 
функции за счет использования данных, сохраненных в кэше. В данном случае мемоизация - лучшее решение по скорости.'''