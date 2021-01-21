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
import time
from memory_profiler import memory_usage

extend_list = [el for el in range(100000)]


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        m_start = memory_usage()
        res = func(*args, **kwargs)
        m_end = memory_usage()
        end = time.time()
        print(f'method => {func.__name__}\n\ttime => {end - start} sec, memory => {m_end[0] - m_start[0]}')
        return res

    return wrapper

@benchmark
def init_list():
    lst = []
    for i in range(200000):
        lst.append(i)
    return lst


@benchmark
def init_list_gen():
    return [el for el in range(20000)]


@benchmark
def init_dict():
    dict = {}
    for i in range(200000):
        dict[i] = i
    return dict


@benchmark
def add_to_list(lst):
    for i in range(200000, 300000):
        lst.append(i)


@benchmark
def add_to_list_extend(lst, ext_lst):
    lst.extend(ext_lst)


@benchmark
def add_to_dict(dict):
    for i in range(200000, 300000):
        dict[i] = i


list = init_list()
list2 = init_list_gen()
dict = init_dict()
add_to_list(list)
add_to_list_extend(list2, extend_list)
add_to_dict(dict)

"""
Для начала посмотрим на варианты заполнения списка через метод append или через генератор

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     56.7 MiB     56.7 MiB           1   @profile
    23                                         def init_list():
    24     56.7 MiB      0.0 MiB           1       lst = []
    25     64.4 MiB      0.0 MiB      200001       for i in range(200000):
    26     64.4 MiB      7.7 MiB      200000           lst.append(i)
    27     64.4 MiB      0.0 MiB           1       return lst

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     64.4 MiB     64.4 MiB           1   @profile
    31                                         def init_list_gen():
    32     72.2 MiB      7.7 MiB      200003       return [el for el in range(200000)]
    
Видим что потребление примерно на одном и том же уровне

Инициализация словаря такого же размера требует значительно больше памяти, т.к. требуется место для хранения хешей

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     72.2 MiB     72.2 MiB           1   @profile
    36                                         def init_dict():
    37     72.2 MiB      0.0 MiB           1       dict = {}
    38     97.2 MiB      0.0 MiB      200001       for i in range(200000):
    39     97.2 MiB     25.0 MiB      200000           dict[i] = i
    40     97.2 MiB      0.0 MiB           1       return dict

Далее посмотрим на расширение списка двумя способами - добавление элементов в цикле или использование метода extend

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43     97.2 MiB     97.2 MiB           1   @profile
    44                                         def add_to_list(lst):
    45    100.3 MiB      0.0 MiB      100001       for i in range(200000, 300000):
    46    100.3 MiB      3.1 MiB      100000           lst.append(i)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    49    100.3 MiB    100.3 MiB           1   @profile
    50                                         def add_to_list_extend(lst, ext_lst):
    51    102.6 MiB      2.3 MiB           1       lst.extend(ext_lst)
    
Видим, что метод extend потребляет меньше памяти

Напоследок, расширение словаря элементами

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54    102.6 MiB    102.6 MiB           1   @profile
    55                                         def add_to_dict(dict):
    56    105.7 MiB      0.0 MiB      100001       for i in range(200000, 300000):
    57    105.7 MiB      3.1 MiB      100000           dict[i] = i
    
Общие данные полученные с помощью декоратора, 
по которым видна разница по использованию памяти при создании массива обычным способом(for + append) и генератором
method => init_list
	time => 0.2327899932861328 sec, memory => 7.78125
method => init_list_gen
	time => 0.21004915237426758 sec, memory => 0.796875
method => init_dict
	time => 0.23703384399414062 sec, memory => 25.03515625
method => add_to_list
	time => 0.22006011009216309 sec, memory => 3.12109375
method => add_to_list_extend
	time => 0.20840668678283691 sec, memory => 0.01171875
method => add_to_dict
	time => 0.22244501113891602 sec, memory => 3.1015625
"""
