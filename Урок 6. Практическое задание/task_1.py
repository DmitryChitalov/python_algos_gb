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

from collections import OrderedDict
from timeit import default_timer

from memory_profiler import memory_usage


###################################################################

def decor_mem_time(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = default_timer()
        res = func(*args, **kwargs)
        stop = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = stop - start
        print(f"{func.__name__}: {time_diff} секунд, {mem_diff} MiB")
        return res

    return wrapper


###################################################################
num = 1000000
def_dict = dict()
def_o_dict = OrderedDict()


@decor_mem_time
def populate_dict(dict, num):
    for i in range(num):
        dict[-i] = i


@decor_mem_time
def populate_o_dict(o_dict, num):
    for i in range(num):
        o_dict[-i] = i


###################################################################

populate_dict(def_dict, num)
populate_o_dict(def_o_dict, num)
