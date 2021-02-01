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
from timeit import default_timer
from math import factorial


def dec(func):
    """
    Декоратор для проверки использования памяти и времени работы
    """
    def wrap(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args, **kwargs)
        return res, memory_usage()[0] - m1[0], default_timer() - t1
    return wrap


# 1. Удалить из первого списка все вхождения элементов во второй список

my_list_1 = list(range(100000))
my_list_2 = [2, 7, 12, 3]


@profile
def check_and_del1(lst1, lst2):
    j = len(lst1)
    i = 0

    for elem1 in lst1:
        i = 0
        if elem1 in lst2:
            while i < j:
                if lst1[i] == elem1:
                    del lst1[i]
                    j -= 1
                    i -= 1
                i += 1
    return lst1


@profile
def check_and_del2(lst1, lst2):
    return [elem for elem in lst1 if elem not in lst2]


@profile
def check_and_del3(lst1, lst2):
    for elem1 in lst1.copy():
        if elem1 in lst2:
            lst1.remove(elem1)
    return lst1


check_and_del1(my_list_1, my_list_2)
check_and_del2(my_list_1, my_list_2)
check_and_del3(my_list_1, my_list_2)

"""
check_and_del1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     17.9 MiB     17.9 MiB           1   @profile
    26                                         def check_and_del1(lst1, lst2):
    27     17.9 MiB      0.0 MiB           1       j=len(lst1)
    28     17.9 MiB      0.0 MiB           1       i=0
    29                                         
    30     17.9 MiB  -2205.5 MiB       99998       for elem1 in lst1:
    31     17.9 MiB  -2205.5 MiB       99997           i=0
    32     17.9 MiB  -2205.5 MiB       99997           if elem1 in lst2:
    33     17.9 MiB    -37.6 MiB      300000               while i<j:
    34     17.9 MiB    -37.6 MiB      299997                   if lst1[i]==elem1:
    35     17.9 MiB      0.0 MiB           3                       del lst1[i]
    36     17.9 MiB      0.0 MiB           3                       j-=1
    37     17.9 MiB      0.0 MiB           3                       i-=1
    38     17.9 MiB    -37.6 MiB      299997                   i+=1
    39     17.9 MiB     -0.0 MiB           1       return lst1

check_and_del2

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     17.9 MiB     17.9 MiB           1   @profile
    43                                         def check_and_del2(lst1, lst2):
    44     18.6 MiB      0.6 MiB      100000       return [elem for elem in lst1 if elem not in lst2]


check_and_del3

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     17.9 MiB     17.9 MiB           1   @profile
    47                                         def check_and_del3(lst1, lst2):
    48     18.3 MiB      0.4 MiB       99998       for elem1 in lst1.copy():
    49     18.3 MiB      0.0 MiB       99997           if elem1 in lst2:
    50     18.3 MiB      0.0 MiB           1               lst1.remove(elem1)
    51     18.3 MiB      0.0 MiB           1       return lst1


check_and_del1 использует память оптимальнее всего, так как в ней реализована логика прохода по изменяемому списку,
которая позволяет не делать никаких дополнительных копий. Однако работает она намного медленнее, так как не используются
встроенные мехнизмы интерпретатора.
В check_and_del2 создается копия списка из-за применения спискового включения, 
из-за чего добавляется использование памяти.
В check_and_del3 создается копия списка для того, чтобы проходить по старому списка, не учитывая изменения. 
Из-за этого добавляется использование памяти на хранение этой копии. Размеры используемой памяти в check_and_del2 и
check_and_del3 примерно равны.
"""


# 2 Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
# Выведите результат.

@dec
@profile
def resolve_1(storage):
    """
    Сложность: N + 3 + N + N*5 + N + 1 + N*(1 + N + 3) + 1 = N^2 + 11*N + 5 или O(N^2)
    """
    cnt = 0  # O(1)
    res = []  # O(1)
    val_par = list(storage.values())  # O(N)
    while cnt < 3 and len(val_par) != 0:  # O(3)
        max_el = max(val_par)  # O(N) ищем максимальный капитал из имеющихся
        for name, price in storage.items():  # O(N)
            if price == max_el:  # O(1) ищем имена компаний с максимальным капиталом
                res.append(name)  # O(1)
                cnt += 1  # O(1) увеличиваем счетчик компаний
            if cnt == 3:  # O(1) если нашли 3 компании
                break  # O(1)
        cp = val_par.copy()  # O(N)
        i, k = 0, 0  # O(1)
        while i < len(cp) - k:  # O(N) удаляем уже найденные компании из списка для дальнейшего поиска
            if val_par[i] == max_el:  # O(1)
                del val_par[i]  # O(N)
                i -= 1  # O(1)
                k += 1  # O(1)
            i += 1  # O(1)
    return res  # O(1)


@dec
@profile
def resolve_2(storage):
    """
    Сложность: 3*(N + N + N*(4 + 2) + 3*N) + 2 = 33*N + 3 или O(N)
    """
    cnt = 0  # O(1)
    res = []  # O(1)
    while cnt < 3 and len(storage) > 0:   # O(3)
        val_par = list(storage.values())  # O(N)
        max_el = max(val_par)             # O(N) ищем максимальный капитал из имеющихся
        for name, elem in storage.items():  # O(N)
            if elem == max_el and name not in res:  # O(4) ищем ранее не встречавшиеся компании с максимальным капиталом
                res.append(name)   # O(1)
                cnt += 1  # O(1)
        for name in res:  # O(3) удаляем из общего исписка найденные компании для дальнейшего поиска
            if name in storage:  # O(N)
                del storage[name]  # O(1)
    return res  # O(1)


print(resolve_1(dict(tuple(zip(list(range(1000000)), list(range(100000)))))))
print(resolve_2(dict(tuple(zip(list(range(1000000)), list(range(100000)))))))


'''
resolve_1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   127     22.7 MiB     22.7 MiB           1   @dec
   128                                         @profile
   129                                         def resolve_1(storage):
   130                                             """
   131                                             Сложность: N + 3 + N + N*5 + N + 1 + N*(1 + N + 3) + 1 = N^2 + 11*N + 5 или O(N^2)
   132                                             """
   133     22.7 MiB      0.0 MiB           1       cnt = 0  # O(1)
   134     22.7 MiB      0.0 MiB           1       res = []  # O(1)
   135     23.0 MiB      0.4 MiB           1       val_par = list(storage.values())  # O(N)
   136     23.4 MiB     -0.1 MiB           4       while cnt < 3 and len(val_par) != 0:  # O(3)
   137     23.4 MiB     -0.0 MiB           3           max_el = max(val_par)  # O(N) ищем максимальный капитал из имеющихся
   138     23.4 MiB  -2722.4 MiB      300000           for name, price in storage.items():  # O(N)
   139     23.4 MiB  -2722.4 MiB      299998               if price == max_el:  # O(1) ищем имена компаний с максимальным капиталом
   140     23.4 MiB     -0.0 MiB           3                   res.append(name)  # O(1)
   141     23.4 MiB     -0.0 MiB           3                   cnt += 1  # O(1) увеличиваем счетчик компаний
   142     23.4 MiB  -2722.4 MiB      299998               if cnt == 3:  # O(1) если нашли 3 компании
   143     23.4 MiB     -0.0 MiB           1                   break  # O(1)
   144     23.4 MiB      0.4 MiB           3           cp = val_par.copy()  # O(N)
   145     23.4 MiB     -0.0 MiB           3           i, k = 0, 0  # O(1)
   146     23.5 MiB -11125.2 MiB      300000           while i < len(cp) - k:  # O(N) удаляем уже найденные компании из списка для дальнейшего поиска
   147     23.5 MiB -11125.1 MiB      299997               if val_par[i] == max_el:  # O(1)
   148     23.4 MiB     -0.1 MiB           3                   del val_par[i]  # O(N)
   149     23.4 MiB     -0.1 MiB           3                   i -= 1  # O(1)
   150     23.4 MiB     -0.1 MiB           3                   k += 1  # O(1)
   151     23.5 MiB -11125.1 MiB      299997               i += 1  # O(1)
   152     23.4 MiB     -0.0 MiB           1       return res  # O(1)


([99999, 99998, 99997], 0.09765625, 122.615543597)

resolve_2

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   155     22.9 MiB     22.9 MiB           1   @dec
   156                                         @profile
   157                                         def resolve_2(storage):
   158                                             """
   159                                             Сложность: 3*(N + N + N*(4 + 2) + 3*N) + 2 = 33*N + 3 или O(N)
   160                                             """
   161     22.9 MiB      0.0 MiB           1       cnt = 0  # O(1)
   162     22.9 MiB      0.0 MiB           1       res = []  # O(1)
   163     23.3 MiB     -0.0 MiB           4       while cnt < 3 and len(storage) > 0:   # O(3)
   164     23.3 MiB      0.4 MiB           3           val_par = list(storage.values())  # O(N)
   165     23.3 MiB     -0.0 MiB           3           max_el = max(val_par)             # O(N) ищем максимальный капитал из имеющихся
   166     23.3 MiB   -390.6 MiB      300000           for name, elem in storage.items():  # O(N)
   167     23.3 MiB   -390.6 MiB      299997               if elem == max_el and name not in res:  # O(4) ищем ранее не встречавшиеся компании с максимальным капиталом
   168     23.3 MiB     -0.0 MiB           3                   res.append(name)   # O(1)
   169     23.3 MiB     -0.0 MiB           3                   cnt += 1  # O(1)
   170     23.3 MiB     -0.0 MiB           9           for name in res:  # O(3) удаляем из общего исписка найденные компании для дальнейшего поиска
   171     23.3 MiB     -0.0 MiB           6               if name in storage:  # O(N)
   172     23.3 MiB     -0.0 MiB           3                   del storage[name]  # O(1)
   173     23.3 MiB     -0.0 MiB           1       return res  # O(1)


([99999, 99998, 99997], 0.0, 27.39928559100001)


resolve_2 более оптимальна по использованию памяти, так как алгоритм в ней не требует создания копий больших списков,
в то время как в resolve_1 создается копия списка названия компаний для дальнейшего обхода по нему
В некоторых случаях при вычислении длины списка выделялась допонлительная память - предполагаю, что в этом случае 
создавался дополнительный объект этой длины и на него помещалась ссылка.
'''


# 3 Вычисление факториала

@profile
def fact(n):
    for i in range(1, n+1):
        yield factorial(i)


@profile
def fact1(n):
    return [factorial(i) for i in range(1, n+1)]

@dec
@profile
def print_fact(n, f):
    for elem in f(n):
        el = elem


print(print_fact(500, fact))
print(print_fact(500, fact1))


'''
fact

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   263     16.1 MiB     16.1 MiB           1   @dec
   264                                         @profile
   265                                         def print_fact(n, f):
   266     16.1 MiB      0.0 MiB         501       for elem in f(n):
   267     16.1 MiB      0.0 MiB         500           el = elem

   
fact1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   263     16.1 MiB     16.1 MiB           1   @dec
   264                                         @profile
   265                                         def print_fact(n, f):
   266     16.2 MiB      0.1 MiB         501       for elem in f(n):
   267     16.2 MiB      0.0 MiB         500           el = elem




По использованию памяти fact оптимальнее fact1, так как использует ленивые вычисления (генератор), 
таким образом не храня весь список результатов, а рассчитывая результат "на ходу".
'''