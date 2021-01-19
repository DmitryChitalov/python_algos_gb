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
Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    47     31.8 MiB     31.8 MiB           1   @time_memory_dec
    48                                         @profile
    49                                         # Вариант 1. Сложность O(N)
    50                                         def find_max1(com_dict):
    51     31.8 MiB      0.0 MiB           1       result = {}
    52     36.6 MiB      4.9 MiB           1       copy_dict = com_dict.copy()
    53     36.6 MiB      0.0 MiB           4       for i in range(3):
    54     36.6 MiB      0.0 MiB           3           max_val = max(copy_dict.values())
    55     36.6 MiB      0.0 MiB       40507           for key, val in copy_dict.items():
    56     36.6 MiB      0.0 MiB       40507               if val == max_val:
    57     36.6 MiB      0.0 MiB           3                   result[key] = copy_dict.pop(key)
    58     36.6 MiB      0.0 MiB           3                   break
    59     31.8 MiB     -4.9 MiB           1       del copy_dict
    60     31.8 MiB      0.0 MiB           1       return result


Время выполнения: 10.38108491897583
Расход памяти: 0.296875
{'com9770': 10000, 'com13570': 10000, 'com17167': 10000}
Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     31.8 MiB     31.8 MiB           1   @time_memory_dec
    64                                         @profile
    65                                         # Вариант 2. Сложность O(N).
    66                                         def find_max2(com_dict):
    67     31.8 MiB      0.0 MiB           1       lst_max = []
    68     31.8 MiB      0.0 MiB      100001       for key in com_dict:
    69     31.8 MiB      0.0 MiB      100000           if len(lst_max) < 3:
    70     31.8 MiB      0.0 MiB           3               lst_max.append([key, com_dict[key]])
    71                                                 else:
    72     31.8 MiB      0.0 MiB      399943               for i in range(3):
    73     31.8 MiB      0.0 MiB      299971                   if lst_max[i][1] < com_dict[key]:
    74     31.8 MiB      0.0 MiB          25                       lst_max[2] = [key, com_dict[key]]
    75     31.8 MiB      0.0 MiB          25                       break
    76     31.8 MiB      0.0 MiB      699994           lst_max.sort(key=lambda cm: cm[1], reverse=True)
    77     31.8 MiB      0.0 MiB           1       return lst_max


Время выполнения: 199.12100219726562
Расход памяти: 0.0
[['com9770', 10000], ['com13570', 10000], ['com17167', 10000]]
Filename: /home/katrin/Geekbrains/ALGO Python/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    80     31.8 MiB     31.8 MiB           1   @time_memory_dec
    81                                         @profile
    82                                         # Вариант 3. Сложность O(N). Попытка оптимизации Варианта 2: убираю сортировку.
    83                                         def find_max3(com_dict):
    84     31.8 MiB      0.0 MiB           1       lst_max = []
    85     31.8 MiB      0.0 MiB      100001       for key in com_dict:
    86     31.8 MiB      0.0 MiB      100000           if len(lst_max) < 3:
    87     31.8 MiB      0.0 MiB           3               lst_max.append((key, com_dict[key]))
    88                                                 else:
    89     31.8 MiB      0.0 MiB      699979               mn = min(lst_max, key=lambda cm: cm[1])
    90     31.8 MiB      0.0 MiB       99997               if com_dict[key] >= mn[1]:
    91     31.8 MiB      0.0 MiB          59                   for i in range(3):
    92     31.8 MiB      0.0 MiB          59                       if lst_max[i][1] == mn[1]:
    93     31.8 MiB      0.0 MiB          30                           lst_max[i] = (key, com_dict[key])
    94     31.8 MiB      0.0 MiB          30                           break
    95     31.8 MiB      0.0 MiB           1       return lst_max


Время выполнения: 123.8405122756958
Расход памяти: 0.0
[('com83576', 10000), ('com9770', 10000), ('com17167', 10000)]
'''
# Вывод: зачастую приходится выбирать между скоростью и расходом памяти.

