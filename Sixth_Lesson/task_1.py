"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile, memory_usage
from timeit import timeit, default_timer
from pympler import asizeof

"""Python 3.7.2, 64-разрядная Windows 7"""

"""Скрипт 1"""

"""Нептимизированная версия через цикл"""
@profile
def list_1():
    l = list()
    for i in range(60000):
        l += [i]
    return l

def my_generator():
    for i in range(60000):
        yield i
"""Оптимизированная версия через генератор"""
@profile
def list_2():
    l = []
    for i in my_generator():
        l += [i]
    return l

list_1()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     30.3 MiB     30.3 MiB           1   @profile
    35                                         def list_1():
    36     30.3 MiB      0.0 MiB           1       l = list()
    37     33.3 MiB      0.0 MiB       60001       for i in range(60000):
    38     33.3 MiB      2.9 MiB       60000           l += [i]
    39     33.3 MiB      0.0 MiB           1       return l
"""
list_2()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     30.4 MiB     30.4 MiB           1   @profile
    46                                         def list_2():
    47     30.4 MiB      0.0 MiB           1       l = []
    48     33.0 MiB      0.0 MiB       60001       for i in my_generator():
    49     33.0 MiB      2.6 MiB       60000           l += [i]
    50     33.0 MiB      0.0 MiB           1       return l

"""
"""Вывод: функция с циклом показала в значении Increment: 2.9 MiB,
 , а функция, использующая генератор 2.6 MiB, что подтверждает преимущество 
  использования генератора, но всё же пример не очень удачный, так как мы в обоих случаях возвращаем
  список, который хранится в памяти.
 """

"""Скрипт 2"""
#Декоратор для замеров памяти и времени
def my_decorator(function):
    def wrapper():
        m0 = memory_usage()
        t0 = default_timer()
        my_list = function()
        t1 = default_timer()
        m1 = memory_usage()
        return f'Инкремент памяти: {m1[0] - m0[0]}\nВремени затрачено: {t1 - t0}'
    return wrapper

class NotOptimized():
    def __init__(self, host = "127.0.0.1", port = 8000):
        self.host = host
        self.port = port

@my_decorator
def func_1():
    l = []
    for i in range(1000000):
        l.append(NotOptimized())
    return l

class Optimized():
    __slots__ = ("host", "port")
    def __init__(self, host = "127.0.0.1", port = 8000):
        self.host = host
        self.port = port

@my_decorator
def func_2():
    l = []
    for i in range(1000000):
        l.append(Optimized())
    return l

l = func_1()
print('Без слотов: ',asizeof.asizeof(l))
l = func_2()
print('Используя слоты: ',asizeof.asizeof(l))
""" Вывод без декоратора:

Без слотов:  176697672
Используя слоты:  64697560

Вывод: в некоторых случаях переопределения метода __slots__()
помогает в несколько раз уменьшить объём используемой памяти,
(в данном примере приблизительно в 3 раза).
"""
print(func_1())
print(func_2())
"""Вывод с декоратором:

Инкремент памяти: 170.75390625
Времени затрачено: 1.0536649699999998
Инкремент памяти: 61.828125
Времени затрачено: 0.8856505809999999

Вывод: Использование переопределённого метода __slots__
даёт выйгрыш не только в экономии памяти, но и во времени выполнения,
о чем свидетельствует написанный мной декоратор, вычисляющий дельту памяти
и дельту времени.
"""