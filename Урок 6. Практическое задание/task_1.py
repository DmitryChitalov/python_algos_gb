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


from memory_profiler import profile, memory_usage
import timeit
import random
import gc


def time_memory_profile(func):
    def wrapper_func(*args, **kwargs):
        current_memory_1 = memory_usage()
        current_time_1 = timeit.default_timer()
        func(*args, **kwargs)
        current_time_2 = timeit.default_timer()
        current_memory_2 = memory_usage()
        print(f"Function {func.__name__} memory difference: {current_memory_2[0] - current_memory_1[0]}, "
              f"elapsed time: {current_time_2 - current_time_1}")
    return wrapper_func


@profile
# @time_memory_profile
def script_1_implementation_1(count: int):
    new_list = list()
    for index in range(count):
        if index % 2 == 0:
            new_list.append(index)
    return new_list


@profile
#@time_memory_profile
def script_1_implementation_2(count: int):
    return list(el for el in range(count) if not el % 2)


@profile
# @time_memory_profile
def script_2_implementation_1(count: int):
    def enumerator1():
        yield random.randint(0, 100)
    list1 = list()
    for element in enumerator1():
        list1.append(element)
        if len(list1) == count:
            break


@profile
@time_memory_profile
def script_2_implementation_2(count: int):
    list(random.randint(0, 100) for _ in range(count))


@profile
@time_memory_profile
def script_3_implementation_1(count: int):
    dict1 = {el: el for el in range(count)}


@profile
@time_memory_profile
def script_3_implementation_2(count: int):
    list1 = [el for el in range(count)]


# gc.disable()
script_1_implementation_1(100000)
script_1_implementation_2(100000)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     46     18.9 MiB     18.9 MiB           1   @profile
#     47                                         # @time_memory_profile
#     48                                         def script_1_implementation_1(count: int):
#     49     18.9 MiB      0.0 MiB           1       new_list = list()
#     50     21.5 MiB      0.0 MiB      100001       for index in range(count):
#     51     21.5 MiB      1.5 MiB      100000           if index % 2 == 0:
#     52     21.5 MiB      1.1 MiB       50000               new_list.append(index)
#     53     21.5 MiB      0.0 MiB           1       return new_list

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     56     19.1 MiB     19.1 MiB           1   @profile
#     57                                         # @time_memory_profile
#     58                                         def script_1_implementation_2(count: int):
#     59     21.4 MiB      2.3 MiB      150003       return list(el for el in range(count) if not el % 2)

# Function script_1_implementation_1 memory difference: 0.21484375, elapsed time: 0.03602179999999999
# Function script_1_implementation_2 memory difference: 0.484375, elapsed time: 0.018971300000000024

script_2_implementation_1(100000)
script_2_implementation_2(100000)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     62     19.0 MiB     19.0 MiB           1   @profile
#     63                                         # @time_memory_profile
#     64                                         def script_2_implementation_1(count: int):
#     65     19.0 MiB      0.0 MiB           2       def enumerator1():
#     66     19.0 MiB      0.0 MiB           2           yield random.randint(0, 100)
#     67     19.0 MiB      0.0 MiB           1       list1 = list()
#     68     19.0 MiB      0.0 MiB           2       for element in enumerator1():
#     69     19.0 MiB      0.0 MiB           1           list1.append(element)
#     70     19.0 MiB      0.0 MiB           1           if len(list1) == count:
#     71                                                     break

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     74     19.1 MiB     19.1 MiB           1   @profile
#     75                                         # @time_memory_profile
#     76                                         def script_2_implementation_2(count: int):
#     77     20.5 MiB      0.0 MiB      200003       list(random.randint(0, 100) for _ in range(count))

# Function script_2_implementation_1 memory difference: 0.0078125, elapsed time: 7.150000000000212e-05
# Function script_2_implementation_2 memory difference: -0.0859375, elapsed time: 0.19693680000000002

script_3_implementation_1(100000)
script_3_implementation_2(100000)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     80     19.2 MiB     19.2 MiB           1   @profile
#     81                                         # @time_memory_profile
#     82                                         def script_3_implementation_1(count: int):
#     83     27.2 MiB      8.1 MiB      100003       dict1 = {el: el for el in range(count)}

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     86     19.0 MiB     19.0 MiB           1   @profile
#     87                                         # @time_memory_profile
#     88                                         def script_3_implementation_2(count: int):
#     89     23.6 MiB      4.6 MiB      100003       list1 = [el for el in range(count)]

# Function script_3_implementation_1 memory difference: 0.25390625, elapsed time: 0.038227299999999964
# Function script_3_implementation_2 memory difference: 0.0078125, elapsed time: 0.025683200000000017

'''
Вывод:
Если говорить о первой функции результаты показывают болший расход памяти примерно одинаковый в случае с profile
В случае второй функции также примерно одинаковый ввиду того, что enumerator1 и range также генераторы,
в случае с третьей функцией очевидно словарь занимает почти в два раза больше меньше места.
На результаты декоратора time_memory_profile лучше не ориентироваться, т.к. он даёт только разницу памяти между
моментами завершения и начала функции, а за этот момент сборщик мусора может выполнить очистку несколько раз, более того
сборщик может вызваться только на второй функции почистив тем самым данные, выделенные функции, которая вызвалась до
этого метода, что создаст абсолютно неверную картину, выход из этой ситуации состоит в отключении сборщика мусора 
'''
