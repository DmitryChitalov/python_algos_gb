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
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('\nНе оптимизированная функция recursive_reverse')
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


print('\nОптимизированная функция recursive_reverse_mem')
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

# Не смотря на то, что замеры показывают, что оптимизированная через мемоизацию функция работает быстрее,
# на самом деле это не так. Мемоизация помогает ускорить работу рекурсивной функции, если в нескольких вызовах
# в качестве аргумента передаётся одно и то же значение. Здесь же значения каждый раз разные и мемоизация никак
# не должна повлиять на скорость работы функции (если только ещё её замедлить за счёт дополнительных манипуляций).
# Почему же получились такие результаты замеров?
# Всё дело в декораторе. Что происходит, когда мы вызываем функцию recursive_reverse_mem? Мы сперва вызываем функцию
# memoize. Функция memoize создаёт словарь cache. И затем мы вызываем функцию decorate, в которую передаём наши
# аргументы. Проблема в том, что memoize вызывается только один раз - первый. Все последующие вызовы относятся только
# к функции decorate (это легко увидеть через профилирование cProfile):
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 30024/30000    0.003    0.000    0.003    0.000 task_2.py:50(decorate)
#      25/3    0.000    0.000    0.000    0.000 task_2.py:60(recursive_reverse_mem)
#
# Профилировались три замера из кода выше функции recursive_reverse_mem. Видно, что функция recursive_reverse_mem
# со строки 60 (там как раз наш декаратор memoize) запускалась три раза,
# а вот функция decorate со строки 50 запускалась 30 000 раз.
#
# Таким образом, созданный и заполненный при первом вызове функции словарь cache не пересоздаётся при повторных вызовах.
# А так как при замерах мы вызываем функцию 10 000 раз для одного и того же значения, уже после первого вызова декоратор
# просто использует этот словарь и в результате мы получаем сбивающие с толку результаты замеров.
# Схожая ситуация может возникнуть при замере скорости сортировки массива - при повторных вызовах будет сортироваться
# уже отсортированный массив и мы тоже получим искажённые результаты замеров.

# Какая функция будет работать быстрее, чем рекурсивная? Практически любая, потому что рекурсивная функция
# имеет факториальную сложность.
# Например, можно написать функцию, которая будет преобразовывать введённое число в строку и
# использовать реверс среза:


def slice_reverse_num(num):
    return str(num)[::-1]


print('\nФункция slice_reverse_num')
print(
    timeit(
        'slice_reverse_num(num_100)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'slice_reverse_num(num_1000)',
        globals=globals(),
        number=10000))
print(
    timeit(
        'slice_reverse_num(num_10000)',
        globals=globals(),
        number=10000))

# Замеры показывают неплохой результат: на моей машине примерно 0.0022, 0.0023, 0.0024 для строк разной длины против
# 0.015, 0.017, 0.034 для рекурсивной функции.
