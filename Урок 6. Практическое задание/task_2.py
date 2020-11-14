"""
Задание 2.
Предложить еще какие-гибудь варианты (механизмы, библиотеки) оптимизации и
доказать (наглядно, кодом) их эффективность
"""

from functools import reduce
from memory_profiler import profile
from pympler import tracker


@profile
def function_2(max_value):
    # возвращаем сумму квадратов четных чисел от 0 до max_value
    gen = (x ** 2 for x in range(1, max_value) if x % 2 == 0)
    print(type(gen))
    value = reduce(lambda x, y: x + y, gen)
    return value


# print(function_2(9999))
tr = tracker.SummaryTracker()
function_2(9999)
tr.print_diff()

"""
Результат:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     18.7 MiB     18.7 MiB           1   @profile
    12                                         def function_1(max_value):
    13                                             # возвращаем сумму квадратов четных чисел от 0 до max_value
    14     18.7 MiB      0.0 MiB       15000       gen = (x ** 2 for x in range(1, max_value) if x % 2 == 0)
    15     18.7 MiB      0.0 MiB           1       print (type(gen))
    16     18.7 MiB      0.0 MiB        9997       value = reduce(lambda x, y: x + y, gen)
    17     18.7 MiB      0.0 MiB           1       return value


166616670000

                types |   # objects |   total size
======================= | =========== | ============
                   list |        4999 |    432.52 KB
                    str |        4997 |    348.87 KB
                    int |        1206 |     32.98 KB
                   dict |           3 |    400     B
                   code |           1 |    246     B
                  tuple |           4 |    224     B
  function (store_info) |           1 |    136     B
                   cell |           2 |     80     B
                weakref |           1 |     72     B
                 method |           1 |     64     B


Здесь наглядно видно, что генераторы более рациональны чем списки, в плане использования памяти
Также можем видет сколько присутствует типов данных и сколко потребляет памяти каждый из них
"""
