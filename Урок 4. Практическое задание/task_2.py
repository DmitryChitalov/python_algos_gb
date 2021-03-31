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
from textwrap import dedent


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


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


# Сначала сделаем числа разной длины, чтобы они порождали
# разное число рекурсивных вызовов
num_1 = 1
num_5 = 12345
num_10 = 1234567890


N = 1
print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_1)",
        setup='from __main__ import recursive_reverse, num_1',
        number=N))
print(
    timeit(
        "recursive_reverse(num_5)",
        setup='from __main__ import recursive_reverse, num_5',
        number=N))
print(
    timeit(
        "recursive_reverse(num_10)",
        setup='from __main__ import recursive_reverse, num_10',
        number=N))
# ---
# Не оптимизированная функция recursive_reverse
# 0.5288310369942337
# 1.658883001015056
# 3.1454150729696266
# ---
# Видно, что время зависит от длины числа, то есть рекурсия происходит


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_1)',
        setup='from __main__ import recursive_reverse_mem, num_1',
        number=N))
print(
    timeit(
        'recursive_reverse_mem(num_5)',
        setup='from __main__ import recursive_reverse_mem, num_5',
        number=N))
print(
    timeit(
        'recursive_reverse_mem(num_10)',
        setup='from __main__ import recursive_reverse_mem, num_10',
        number=N))
# ---
# Оптимизированная функция recursive_reverse_mem
# 0.17349300003843382
# 0.169658282015007
# 0.1851398529834114
# ---
# Странные результаты, совершенно не зависят от длины числа
# Можно предположить, что функция отрабатывает только
# в первый раз, а дальше мы имеем 999999 чтений из словаря.
# Сделаем аргументы случайными:

N = 1000000
print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        dedent('''
            n = randint(10**8, 10**9)
            recursive_reverse(n)'''),
        setup=dedent('''
            from random import randint
            from __main__ import recursive_reverse'''),
        number=N))

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        dedent('''
            n = randint(10**8, 10**9)
            recursive_reverse_mem(n)'''),
        setup=dedent('''
            from random import randint
            from __main__ import recursive_reverse_mem'''),
        number=N))

# ---
# Не оптимизированная функция recursive_reverse
# 3.585237400024198
# Оптимизированная функция recursive_reverse_mem
# 4.854937668016646
# ---

# Что и требовалось доказать, мемоизация в данном случае
# делает только хуже
