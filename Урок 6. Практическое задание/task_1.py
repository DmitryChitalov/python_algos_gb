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

from memory_profiler import profile
from copy import deepcopy
import sys


@profile(precision=4)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile(precision=4)
def get_even_index_list(nums):
    pass
    even_index_list = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return even_index_list


@profile(precision=4)
def get_even_index_list_insert(nums):
    pass
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.insert(0, i)
    return new_arr


class TestClass():
    def __init__(self):
        num_list = list(range(0, 1000))
        self.__res1 = func_1(num_list)
        self.__res2 = get_even_index_list(num_list)
        self.__res3 = get_even_index_list_insert(num_list)
        self.__res4 = "123asd123sdf12312dfkgsdn345u9qweuo jfsjksfdjksdfjk sadfakj324 jksajksadf"

    def sizes(self):
        print(f"len res1 {len(self.__res1)}")
        print(f"len res1 {len(self.__res2)}")
        print(f"len res1 {len(self.__res3)}")
        print(f"len res1 {len(self.__res4)}")
        print(f"sizeof res1 {sys.getsizeof(self.__res1)}")
        print(f"sizeof res2 {sys.getsizeof(self.__res2)}")
        print(f"sizeof res3 {sys.getsizeof(self.__res3)}")
        print(f"sizeof res4 {sys.getsizeof(self.__res4)}")


@profile(precision=4)
def do_test():
    num_list = list(range(0, 1000))
    res1 = func_1(deepcopy(num_list))
    res2 = get_even_index_list(num_list[:])
    res3 = get_even_index_list_insert(num_list[:])
    res4 = "123asd123sdf12312dfkgsdn345u9qweuo jfsjksfdjksdfjk sadfakj324 jksajksadf"
    res5 = ""
    for _ in range(10000):
        res5 = res5 + res4
    test_obj = TestClass()
    test_obj.sizes()
    print(f"size of res5 {sys.getsizeof(res5)} bytes")
    del res4
    del num_list

    res6 = deepcopy(res5)
    res6 += "1"
    res7 = res6
    res7 += "1"
    print(f"len res1 {len(res1)}")


@profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


@profile(precision=4)
def main():
    pass
    try:

        do_test()
        my_func()
        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
Python 3.8.6 (default, Sep 25 2020, 09:36:53) 
[GCC 10.2.0] on linux 
OS Linux Ubuntu 20.10 x64

По результам профилирования, видно что расход памяти очень маленький в большенстве участков кода. 
1 Mib равен 1 048 576 байт. Так же видно, что Increment считается не правильно в 99% случаев. Но его можно 
посчитать вручную отняв от текущей строки "mem usage" от предыдущей.

Сборщик мусора очищает память не полностью. 




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22  16.8555 MiB  16.8555 MiB           1   @profile(precision=4)
    23                                         def func_1(nums):
    24  16.8555 MiB   0.0000 MiB           1       new_arr = []
    25  16.8555 MiB   0.0000 MiB        1001       for i in range(len(nums)):
    26  16.8555 MiB   0.0000 MiB        1000           if nums[i] % 2 == 0:
    27  16.8555 MiB   0.0000 MiB         500               new_arr.append(i)
    28  16.8555 MiB   0.0000 MiB           1       return new_arr


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31  16.8555 MiB  16.8555 MiB           1   @profile(precision=4)
    32                                         def get_even_index_list(nums):
    33                                             pass
    34  16.8555 MiB   0.0000 MiB        1003       even_index_list = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    35  16.8555 MiB   0.0000 MiB           1       return even_index_list


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38  16.8555 MiB  16.8555 MiB           1   @profile(precision=4)
    39                                         def get_even_index_list_insert(nums):
    40                                             pass
    41  16.8555 MiB   0.0000 MiB           1       new_arr = []
    42  16.8555 MiB   0.0000 MiB        1001       for i in range(len(nums)):
    43  16.8555 MiB   0.0000 MiB        1000           if nums[i] % 2 == 0:
    44  16.8555 MiB   0.0000 MiB         500               new_arr.insert(0, i)
    45  16.8555 MiB   0.0000 MiB           1       return new_arr


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22  18.9531 MiB  18.9531 MiB           1   @profile(precision=4)
    23                                         def func_1(nums):
    24  18.9531 MiB   0.0000 MiB           1       new_arr = []
    25  18.9531 MiB   0.0000 MiB        1001       for i in range(len(nums)):
    26  18.9531 MiB   0.0000 MiB        1000           if nums[i] % 2 == 0:
    27  18.9531 MiB   0.0000 MiB         500               new_arr.append(i)
    28  18.9531 MiB   0.0000 MiB           1       return new_arr


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31  18.9531 MiB  18.9531 MiB           1   @profile(precision=4)
    32                                         def get_even_index_list(nums):
    33                                             pass
    34  19.2109 MiB   0.2578 MiB        1003       even_index_list = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    35  19.2109 MiB   0.0000 MiB           1       return even_index_list


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38  19.2109 MiB  19.2109 MiB           1   @profile(precision=4)
    39                                         def get_even_index_list_insert(nums):
    40                                             pass
    41  19.2109 MiB   0.0000 MiB           1       new_arr = []
    42  19.2109 MiB   0.0000 MiB        1001       for i in range(len(nums)):
    43  19.2109 MiB   0.0000 MiB        1000           if nums[i] % 2 == 0:
    44  19.2109 MiB   0.0000 MiB         500               new_arr.insert(0, i)
    45  19.2109 MiB   0.0000 MiB           1       return new_arr


len res1 500
len res1 500
len res1 500
len res1 72
sizeof res1 4264
sizeof res2 4264
sizeof res3 4264
sizeof res4 121
size of res5 720049 bytes
len res1 500
Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    67  16.8555 MiB  16.8555 MiB           1   @profile(precision=4)
    68                                         def do_test():
    69  16.8555 MiB   0.0000 MiB           1       num_list = list(range(0, 1000))
    70  16.8555 MiB   0.0000 MiB           1       res1 = func_1(deepcopy(num_list))
    71  16.8555 MiB   0.0000 MiB           1       res2 = get_even_index_list(num_list[:])
    72  16.8555 MiB   0.0000 MiB           1       res3 = get_even_index_list_insert(num_list[:])
    73  16.8555 MiB   0.0000 MiB           1       res4 = "123asd123sdf12312dfkgsdn345u9qweuo jfsjksfdjksdfjk sadfakj324 jksajksadf"
    74  16.8555 MiB   0.0000 MiB           1       res5 = ""
    75  19.0781 MiB -3136.6797 MiB       10001       for _ in range(10000):
    76  19.0781 MiB -3134.4570 MiB       10000           res5 = res5 + res4
    77  19.2109 MiB   0.1328 MiB           1       test_obj = TestClass()
    78  19.2109 MiB   0.0000 MiB           1       test_obj.sizes()
    79  19.2109 MiB   0.0000 MiB           1       print(f"size of res5 {sys.getsizeof(res5)} bytes")
    80  19.2109 MiB   0.0000 MiB           1       del res4
    81  19.2109 MiB   0.0000 MiB           1       del num_list
    82                                         
    83  19.2109 MiB   0.0000 MiB           1       res6 = deepcopy(res5)
    84  19.2109 MiB   0.0000 MiB           1       res6 += "1"
    85  19.2109 MiB   0.0000 MiB           1       res7 = res6
    86  19.8516 MiB   0.6406 MiB           1       res7 += "1"
    87  19.8516 MiB   0.0000 MiB           1       print(f"len res1 {len(res1)}")


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    90  17.4336 MiB  17.4336 MiB           1   @profile(precision=4)
    91                                         def my_func():
    92  24.9062 MiB   7.4727 MiB           1       a = [1] * (10 ** 6)
    93 177.5312 MiB 152.6250 MiB           1       b = [2] * (2 * 10 ** 7)
    94  25.0664 MiB -152.4648 MiB           1       del b
    95  25.0664 MiB   0.0000 MiB           1       return a



Программа завершена!
Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    98  16.8555 MiB  16.8555 MiB           1   @profile(precision=4)
    99                                         def main():
   100                                             pass
   101  16.8555 MiB   0.0000 MiB           1       try:
   102                                         
   103  17.4336 MiB   0.5781 MiB           1           do_test()
   104  17.4336 MiB   0.0000 MiB           1           my_func()
   105  17.4336 MiB   0.0000 MiB           1           print("\nПрограмма завершена!")
   106                                             except Exception as ex:
   107                                                 print(f"Fatal error: {ex}")



Process finished with exit code 0

"""
