"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile, memory_usage
import time
from random import randint


def time_memory_dec(fn):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        m1 = memory_usage()
        res = fn(*args, **kwargs)
        print(f'Время выполнения: {time.time() - time_start}')
        m2 = memory_usage()
        print(f'Расход памяти: {m2[0]-m1[0]}')
        return res
    return wrapper


# Пример 1. Задача №3 из домашнего задания 1: Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
com = {'com' + str(i): randint(0, 10000) for i in range(100000)}


@time_memory_dec
@profile
# Вариант 1. Сложность O(N). Расходует память, потому как создает копию исходного словаря.
# Для оптимизации использования памяти - освобождаю принудительно память перед завершением работы функции.
def find_max1(com_dict):
    result = {}
    copy_dict = com_dict.copy()
    for i in range(3):
        max_val = max(copy_dict.values())
        for key, val in copy_dict.items():
            if val == max_val:
                result[key] = copy_dict.pop(key)
                break
    del copy_dict
    return result


@time_memory_dec
@profile
# Вариант 2. Сложность O(N). Не использует дополнительную память, но работает медленно, полагаю из-за того,
# что последовательный перебор элементов словаря - не самое оптимальное его использование.
def find_max2(com_dict):
    lst_max = []
    for key in com_dict:
        if len(lst_max) < 3:
            lst_max.append([key, com_dict[key]])
        else:
            for i in range(3):
                if lst_max[i][1] < com_dict[key]:
                    lst_max[2] = [key, com_dict[key]]
                    break
        lst_max.sort(key=lambda cm: cm[1], reverse=True)
    return lst_max


@time_memory_dec
@profile
# Вариант 3. Сложность O(N). Попытка оптимизации Варианта 2: убираю сортировку. Алгоритм стал быстрее, чем вариант 2,
# но все ещё медленнее варианта 1
def find_max3(com_dict):
    lst_max = []
    for key in com_dict:
        if len(lst_max) < 3:
            lst_max.append((key, com_dict[key]))
        else:
            mn = min(lst_max, key=lambda cm: cm[1])
            if com_dict[key] >= mn[1]:
                for i in range(3):
                    if lst_max[i][1] == mn[1]:
                        lst_max[i] = (key, com_dict[key])
                        break
    return lst_max


print(find_max1(com))
print(find_max2(com))
print(find_max3(com))

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    41     33.4 MiB     33.4 MiB           1   @time_memory_dec
    42                                         @profile
    43                                         # Вариант 1. Сложность O(N). Расходует память, потому как создает копию исходного словаря.
    44                                         # Для оптимизации использования памяти - освобождаю принудительно память перед завершением работы функции.
    45                                         def find_max1(com_dict):
    46     33.4 MiB      0.0 MiB           1       result = {}
    47     38.4 MiB      5.0 MiB           1       copy_dict = com_dict.copy()
    48     38.4 MiB      0.0 MiB           4       for i in range(3):
    49     38.4 MiB      0.0 MiB           3           max_val = max(copy_dict.values())
    50     38.4 MiB      0.0 MiB       44882           for key, val in copy_dict.items():
    51     38.4 MiB      0.0 MiB       44882               if val == max_val:
    52     38.4 MiB      0.0 MiB           3                   result[key] = copy_dict.pop(key)
    53     38.4 MiB      0.0 MiB           3                   break
    54     33.4 MiB     -5.0 MiB           1       del copy_dict
    55     33.4 MiB      0.0 MiB           1       return result


Время выполнения: 1.7209665775299072
Расход памяти: 0.37890625
{'com5932': 10000, 'com18510': 10000, 'com20440': 10000}


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    58     33.4 MiB     33.4 MiB           1   @time_memory_dec
    59                                         @profile
    60                                         # Вариант 2. Сложность O(N). Не использует дополнительную память, но работает медленно, полагаю из-за того,
    61                                         # что последовательный перебор элементов словаря - не самое оптимальное его использование.
    62                                         def find_max2(com_dict):
    63     33.4 MiB      0.0 MiB           1       lst_max = []
    64     33.4 MiB      0.0 MiB      100001       for key in com_dict:
    65     33.4 MiB      0.0 MiB      100000           if len(lst_max) < 3:
    66     33.4 MiB      0.0 MiB           3               lst_max.append([key, com_dict[key]])
    67                                                 else:
    68     33.4 MiB      0.0 MiB      399956               for i in range(3):
    69     33.4 MiB      0.0 MiB      299979                   if lst_max[i][1] < com_dict[key]:
    70     33.4 MiB      0.0 MiB          20                       lst_max[2] = [key, com_dict[key]]
    71     33.4 MiB      0.0 MiB          20                       break
    72     33.4 MiB      0.0 MiB      699994           lst_max.sort(key=lambda cm: cm[1], reverse=True)
    73     33.4 MiB      0.0 MiB           1       return lst_max


Время выполнения: 28.87936305999756
Расход памяти: 0.03125
[['com5932', 10000], ['com18510', 10000], ['com20440', 10000]]


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    76     33.4 MiB     33.4 MiB           1   @time_memory_dec
    77                                         @profile
    78                                         # Вариант 3. Сложность O(N). Попытка оптимизации Варианта 2: убираю сортировку. Алгоритм стал быстрее, чем вариант 2,
    79                                         # но все ещё медленнее варианта 1
    80                                         def find_max3(com_dict):
    81     33.4 MiB      0.0 MiB           1       lst_max = []
    82     33.4 MiB      0.0 MiB      100001       for key in com_dict:
    83     33.4 MiB      0.0 MiB      100000           if len(lst_max) < 3:
    84     33.4 MiB      0.0 MiB           3               lst_max.append((key, com_dict[key]))
    85                                                 else:
    86     33.4 MiB      0.0 MiB      699979               mn = min(lst_max, key=lambda cm: cm[1])
    87     33.4 MiB      0.0 MiB       99997               if com_dict[key] >= mn[1]:
    88     33.4 MiB      0.0 MiB          44                   for i in range(3):
    89     33.4 MiB      0.0 MiB          44                       if lst_max[i][1] == mn[1]:
    90     33.4 MiB      0.0 MiB          28                           lst_max[i] = (key, com_dict[key])
    91     33.4 MiB      0.0 MiB          28                           break
    92     33.4 MiB      0.0 MiB           1       return lst_max


Время выполнения: 18.134470224380493
Расход памяти: 0.0
[('com98018', 10000), ('com18510', 10000), ('com20440', 10000)]
'''
# Вывод: зачастую приходится выбирать между скоростью и расходом памяти.
