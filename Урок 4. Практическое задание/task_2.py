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


@memoize
def my_func(number, my_new_numb=''):
    if number == '':
        return my_new_numb
    else:
        my_new_numb = my_new_numb + str(number)[-1]
        return my_func(str(number)[:-1], my_new_numb)


# print(f"проверка {my_func(num_100, my_new_numb = '')}")


print('Мой вариант рекурсии')
print(
    timeit(
        'my_func(num_100)',
        setup='from __main__ import my_func, num_100',
        number=10000))
print(
    timeit(
        'my_func(num_1000)',
        setup='from __main__ import my_func, num_1000',
        number=10000))
print(
    timeit(
        'my_func(num_10000)',
        setup='from __main__ import my_func, num_10000',
        number=10000))


def my_new_f(number):
    my_new_numb = ''
    for el in str(number):
        my_new_numb = el + my_new_numb
    return my_new_numb


print('Мой вариант с циклом')
print(
    timeit(
        'my_new_f(num_100)',
        setup='from __main__ import my_new_f, num_100',
        number=10000))
print(
    timeit(
        'my_new_f(num_1000)',
        setup='from __main__ import my_new_f, num_1000',
        number=10000))
print(
    timeit(
        'my_new_f(num_10000)',
        setup='from __main__ import my_new_f, num_10000',
        number=10000))


def my_func1(number):
    enter_num = str(number)
    revers_num = enter_num[::-1]
    return revers_num


print('Мой вариант с подсмотренной функцией')
print(my_func1(num_100))
print(
    timeit(
        'my_func1(num_100)',
        setup='from __main__ import my_func1, num_100',
        number=10000))
print(
    timeit(
        'my_func1(num_1000)',
        setup='from __main__ import my_func1, num_1000',
        number=10000))
print(
    timeit(
        'my_func1(num_10000)',
        setup='from __main__ import my_func1, num_10000',
        number=10000))


"""
Декоратор однозначно нужен так как с ним существенно быстрее работает рекурсия, потому что много одинаковых операций
Попробовал оптимизировать декоратор что бы кеш был не словарем а списком, так как список заполняется быстрее но 
запутался и не получилось
Сделал свой вариант рекурсии через строки и срезы, так получалось иногда быстрее, наверно операции деления
с большими числами медленнее чем срез в строке. Хотя ваше решение стильное и элегантное всего в 1 строчку.
Не оптимизированная функция recursive_reverse
0.03767780900000001
0.04303802400000001
0.062163724000000004
Оптимизированная функция recursive_reverse_mem
0.002196224999999996
0.0022269719999999937
0.002251596999999994
Мой вариант рекурсии
0.0021334880000000167
0.002132881000000003
0.0021822240000000104
Мой вариант с циклом
0.007067792999999989
0.007762734000000021
0.011639294999999994
Мой вариант с подсмотренной функцией
0.003939824000000008
0.0038577090000000147
0.0044003930000000024
Еще попробовал через цикл, получилось быстрее чем через рекурсию но медленнее чем рекурсия с декоратором.
Потом начал делать 3 задание и увидел там решение с перевернутой строкой думал будет быстрее рекурсии с декоратором
оказалось нет, но все равно быстрее чем с циклом.
"""