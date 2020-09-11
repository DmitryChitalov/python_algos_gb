"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile
from functools import reduce


@profile
def func():
    my_list = [el for el in range(20, 242121) if el % 20 == 0 or el % 21 == 0]


func()

'''
Для запуска программы было выделено 16.3 MiB.
При создании списка "my_list" было выделено еще 0.4 MiB.
После выполнения программы удалил список "my_list", тем самым
освободил память на 0.4 MiB.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11     16.3 MiB     16.3 MiB           1   @profile
    12                                         def func():
    13     16.7 MiB      0.4 MiB      242104       my_list = [el for el in range(20, 242121) if el % 20 == 0 or el % 21 == 0]

'''


@profile
def func():
    my_list = list(range(100000))
    print(my_list)
    new_2 = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
    print(new_2)
    del my_list
    del new_2


func()

'''
Для запуска программы было выделено 16.3 MiB.
При создании списка "my_list" было выделено еще 1.9 MiB.
При создании списка "new_2" память увеличилась еще 1.0 MiB.
не могу внятно объяснить цифру -97.1 MiB Increment
после создания списка "new_2" занимаемая память уменьшилась на 0,4 MiB
это связано с тем что из исходного списка были удалены элементы, 
значения которых больше предыдущего элемента.
После выполнения программы удалил списки "my_list" и "new_2" , тем самым
освободил память на 0,6 + 1,2 = 1,8 MiB.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     16.3 MiB     16.3 MiB           1   @profile
    22                                         def func():
    23     18.1 MiB      1.9 MiB           1       my_list = list(range(100000))
    24     18.1 MiB      0.0 MiB           1       print(my_list)
    25     19.1 MiB    -97.1 MiB      100002       new_2 = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
    26     18.7 MiB     -0.4 MiB           1       print(new_2)
    27     18.1 MiB     -0.6 MiB           1       del my_list
    28     16.9 MiB     -1.2 MiB           1       del new_2

'''


@profile
def func():
    def my_list(el_1, el_2):
        return el_1 * el_2

    uniq_list = [el for el in range(10000, 100001, 2)]
    print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(my_list, uniq_list)}")
    del uniq_list


func()

'''
Для запуска программы было выделено 16.3 MiB.
Для работы функции при создании списка "my_list" было выделено еще 0.6 MiB.
Создание списка uniq_list при помои генерации дало выделение 1,1 MiB
Не могу вянтно обяснить очиещение памяти на 0,9 MiB при выполнении печати
После выполнения программы удалил список "my_list", тем самым
освободил память на 0.7 MiB.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     16.3 MiB     16.3 MiB           1   @profile
    13                                         def func():
    14     18.1 MiB      0.6 MiB       45001       def my_list(el_1, el_2):
    15     18.1 MiB      0.1 MiB       45000           return el_1 * el_2
    16                                         
    17     17.4 MiB      1.1 MiB       45004       uniq_list = [el for el in range(10000, 100001, 2)]
    18     17.3 MiB     -0.9 MiB           1       print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(my_list, uniq_list)}")
    19     16.6 MiB     -0.7 MiB           1       del uniq_list


'''


@profile
def func():
    class Matrix:
        def __init__(self, matrix):
            self.matrix = matrix
            # self.matrix2 = matrix2

        def __add__(self, other):
            return Matrix(self.matrix + other.matrix)

        def __str__(self):
            return f"Объект с параметрами ({self.matrix})"

    matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
    matrix_2 = Matrix([[31, 22, 37], [43, 51, 86], [3, -8, -15]])

    a = matrix_1
    b = matrix_2
    print(a)
    print(b)
    print(matrix_1 + matrix_2)


func()

'''
Для запуска программы было выделено 16.3 MiB.
Работа программы не занимает много памяти
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     16.3 MiB     16.3 MiB           1   @profile
    13                                         def func():
    14     16.3 MiB      0.0 MiB           3       class Matrix:
    15     16.3 MiB      0.0 MiB           4           def __init__(self, matrix):
    16     16.3 MiB      0.0 MiB           3               self.matrix = matrix
    17                                                     # self.matrix2 = matrix2
    18                                         
    19     16.3 MiB      0.0 MiB           2           def __add__(self, other):
    20     16.3 MiB      0.0 MiB           1               return Matrix(self.matrix + other.matrix)
    21                                         
    22     16.3 MiB      0.0 MiB           4           def __str__(self):
    23     16.3 MiB      0.0 MiB           3               return f"Объект с параметрами ({self.matrix})"
    24                                         
    25     16.3 MiB      0.0 MiB           1       matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
    26     16.3 MiB      0.0 MiB           1       matrix_2 = Matrix([[31, 22, 37], [43, 51, 86], [3, -8, -15]])
    27                                         
    28     16.3 MiB      0.0 MiB           1       a = matrix_1
    29     16.3 MiB      0.0 MiB           1       b = matrix_2
    30     16.3 MiB      0.0 MiB           1       print(a)
    31     16.3 MiB      0.0 MiB           1       print(b)
    32     16.3 MiB      0.0 MiB           1       print(matrix_1 + matrix_2)

'''
