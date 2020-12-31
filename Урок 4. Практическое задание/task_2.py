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
    def memory_cache(func_arg, memory={}):
        res = memory.get(func_arg)
        if res is None:
            res = func(func_arg)
            memory[func_arg] = res
        return res
    return memory_cache


def recursive_reverse(number):
    if number == 0:
        return ''  # str(number % 10) дописывает лишний "0" в конце числа
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@memorize
def recursive_reverse_mem(number):
    if number == 0:
        return ''  # str(number % 10) дописывает лишний "0" в конце числа
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(recursive_reverse(12345678901))
print('recursive_reverse ', timeit.timeit("recursive_reverse(1234567890)", "from __main__ import recursive_reverse", number=1000))
print(recursive_reverse_mem(12345678901))
print('recursive_reverse_mem ', timeit.timeit("recursive_reverse_mem(1234567890)", "from __main__ import recursive_reverse_mem", number=1000))

# Применена мемоизация, время снизилось в десятки раз.
