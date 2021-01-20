"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти..

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
"""
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
from pympler import asizeof
from memory_profiler import profile


class Road:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length
    @profile()
    def result(self):
        self.weigh = 12
        self.thickness = 5
        x = self.weigh * self.thickness * self.__width * self.__length
        print(x)

@profile()
def func():
    rslt = Road(width=10, length=7)
    rslt.result()
    print("func", asizeof.asizeof((rslt)))


class Broad:
    __slots__ = ['width', 'length']

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def result(self):
        self.weigh = 12
        self.thickness = 5
        x = self.weigh * self.thickness * self.width * self.length
        print(x)


def func2():
    rslt1 = Broad(width=10, length=7)
    print(rslt1.__slots__)

    print("func2", asizeof.asizeof((rslt1)))


func()
func2()
"""
здесь чтобы измерить память я использовала  функцию sizeof()  из библеотеки pympler
и унас есть 2 класса роад и броад
в класс роад выделяет 304 миб памяти и это обычный класс 
а в классе броад выделяется 56 миб памяти и это блогадаря слотам 

"""
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

from memory_profiler import profile

@profile()
def func1():
    my_list = [7, 5, 3, 3, 2]
    new_el = input("введите новый елемент рейтинга:")
    new_el = int(new_el)
    n = 0
    for i in range(len(my_list)):
        if new_el == my_list[i]:
            my_list.insert(i + 1, new_el)
            break


        elif new_el < my_list[i] and new_el > my_list[i + 1]:
            my_list.insert(i + 1, new_el)
            break
        elif new_el < my_list[-1]:
            my_list.insert(len(my_list), new_el)
            break

        elif new_el > my_list[0]:
            my_list.insert(0, new_el)
            break

    print(my_list)

@profile()
def func2():
    my_list = [7, 5, 3, 3, 2]
    new_el = input("введите новый елемент рейтинга:")
    new_el = int(new_el)
    a=list(range(10000000))
    n = 0
    for i in range(len(my_list)):
        if new_el == my_list[i]:
            my_list.insert(i + 1, new_el)
            break


        elif new_el < my_list[i] and new_el > my_list[i + 1]:
            my_list.insert(i + 1, new_el)
            break
        elif new_el < my_list[-1]:
            my_list.insert(len(my_list), new_el)
            break

        elif new_el > my_list[0]:
            my_list.insert(0, new_el)
            break

    print(my_list)

func1()
"""
func1
здесь в первом функции когда функция запускается используется 15.8 миб памяти 
а инкремент не растет
поэтому во втором списке создала список му_лист и этот список выделил   192.0 миб памяти

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    26     15.5 MiB     15.5 MiB           1   @profile()
    27                                         def func1():
    28     15.5 MiB      0.0 MiB           1       my_list = [7, 5, 3, 3, 2]
    29     15.5 MiB      0.0 MiB           1       new_el = input("введите новый елемент рейтинга:")
    30     15.5 MiB      0.0 MiB           1       new_el = int(new_el)
    31     15.5 MiB      0.0 MiB           1       n = 0
    32     15.5 MiB      0.0 MiB           5       for i in range(len(my_list)):
    33     15.5 MiB      0.0 MiB           5           if new_el == my_list[i]:
    34     15.5 MiB      0.0 MiB           1               my_list.insert(i + 1, new_el)
    35     15.5 MiB      0.0 MiB           1               break
    36                                         
    37                                         
    38     15.5 MiB      0.0 MiB           4           elif new_el < my_list[i] and new_el > my_list[i + 1]:
    39                                                     my_list.insert(i + 1, new_el)
    40                                                     break
    41     15.5 MiB      0.0 MiB           4           elif new_el < my_list[-1]:
    42                                                     my_list.insert(len(my_list), new_el)
    43                                                     break
    44                                         
    45     15.5 MiB      0.0 MiB           4           elif new_el > my_list[0]:
    46                                                     my_list.insert(0, new_el)
    47                                                     break
    48                                         
    49     15.5 MiB      0.0 MiB           1       print(my_list)


"""
func2()
"""
 func2


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    52     15.5 MiB     15.5 MiB           1   @profile()
    53                                         def func2():
    54     15.5 MiB      0.0 MiB           1       my_list = [7, 5, 3, 3, 2]
    55     15.5 MiB      0.0 MiB           1       new_el = input("введите новый елемент рейтинга:")
    56     15.5 MiB      0.0 MiB           1       new_el = int(new_el)
    57    207.5 MiB    192.0 MiB           1       a=list(range(10000000))
    58    207.5 MiB      0.0 MiB           1       n = 0
    59    207.5 MiB      0.0 MiB           1       for i in range(len(my_list)):
    60    207.5 MiB      0.0 MiB           1           if new_el == my_list[i]:
    61                                                     my_list.insert(i + 1, new_el)
    62                                                     break
    63                                         
    64                                         
    65    207.5 MiB      0.0 MiB           1           elif new_el < my_list[i] and new_el > my_list[i + 1]:
    66                                                     my_list.insert(i + 1, new_el)
    67                                                     break
    68    207.5 MiB      0.0 MiB           1           elif new_el < my_list[-1]:
    69    207.5 MiB      0.0 MiB           1               my_list.insert(len(my_list), new_el)
    70    207.5 MiB      0.0 MiB           1               break
    71                                         
    72                                                 elif new_el > my_list[0]:
    73                                                     my_list.insert(0, new_el)
    74                                                     break
    75                                         
    76    207.5 MiB      0.0 MiB           1       print(my_list).

"""



