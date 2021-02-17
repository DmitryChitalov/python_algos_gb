"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
from random import randint
from memory_profiler import memory_usage


# декоратор для одновременного замера памяти и времени
def mem_time_count(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = default_timer()
        res = func(args[0])
        stop = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = stop - start
        print(f"{func.__name__}: {time_diff} секунд, {mem_diff} MiB")
        return res

    return wrapper


def fact(n):
    fact = 1
    for el in range(1, n + 1):
        fact *= el
        return fact


def fact_optimized(n):
    fact = 1
    for el in range(1, n + 1):
        fact *= el
        yield fact


@mem_time_count
def call_fact(n):
    for el in range(n): a = fact(n)


@mem_time_count
def call_fact_yield(n):
    for el in fact_optimized(n): a = el


call_fact_yield(1000)
call_fact(1000)
'''
Задача последовательного вычисления факториалов от 1 до n.
Реализация через "yield" работает быстрее, но использует больше памяти: 
call_fact_yield: 0.0006026000000000087 секунд, 0.01171875 MiB
call_fact: 0.0010240999999999723 секунд, 0.0 MiB
'''


@mem_time_count
def list_init_append(length):
    my_list = []
    for idx in range(length):
        my_list.append(idx)
    return my_list


@mem_time_count
def list_init1(length):
    return list(el for el in range(length))


@mem_time_count
def list_init2(length):
    return [el for el in range(length)]


list_init_append(1000000)
list_init1(1000000)
list_init2(1000000)
'''
Три варианта инициализации списка натуральных чисел от 0 до n.
Все варианты дают схожие результаты по использованию памяти, но по скорости
результаты отличаются, самый быстрый - [], самый медленный - .append
list_init_append: 0.12512290000000004 секунд, 39.515625 MiB
list_init1: 0.11407429999999996 секунд, 38.64453125 MiB
list_init2: 0.07545819999999992 секунд, 38.640625 MiB
'''

number = randint(1000000000000000000000, 10000000000000000000000000)


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@mem_time_count
def call_recursive_reverse(number):
    return recursive_reverse(number)

@mem_time_count
def revers_str(number):
    return reversed(str(number))



revers_str(number)
call_recursive_reverse(number)
'''
Два варианта переворота числа:
рекурсивный, и reversed(str):

revers_str: 1.070000000003013e-05 секунд, 0.0 MiB
call_recursive_reverse: 0.00017040000000001498 секунд, 0.0 MiB

reversed(str) отрабатывает быстрее
По памяти проблем нет, но ожидается, что на больших данных рекурсивная функция
будет использовать больше памяти.
'''