"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

from memory_profiler import profile
import sys
import time


@profile(precision=8)
def get_next_val():
    for _ in range(1000):
        s = "#" * 1024000
        yield s


@profile(precision=8)
def my_func():
    reslist = []

    for i in get_next_val():
        reslist.append(i)

    print("check memory")
    time.sleep(10)
    reslist2 = [("!" * 1024000) for _ in range(1000)]

    print(f"size of reslist = {sys.getsizeof(reslist)}")
    print(f"size of reslist2 = {sys.getsizeof(reslist2)}")
    print("check memory 2")
    time.sleep(10)
    del reslist
    del reslist2


@profile(precision=8)
def main():
    my_func()


if __name__ == "__main__":
    main()

"""
Python 3.8.6 (default, Sep 25 2020, 09:36:53) 
[GCC 10.2.0] on linux 
OS Linux Ubuntu 20.10 x64

При работе с генератором, удобно получать значения по 1 за раз. Так можно перебрать список 
не накапливая выделеную память, но постепенно генериря значения функцией. 
Пример указанный выше складывает результат в список и накапливает память - так память не сэкономить. 
При работе с генераторными выражениями память выделяется для этих же целей но сразу на весь ожидаемый объем. 
Даже если захочешь, не съкономишь, лучшее что можно делать, после обработки по 1 удалять элементы списка. 

По итогам работы sys.getsizeof выдает одинаковые значения по выделению памяти для тестовых list'ов.

п.с. пример кода выше кушает примерно 2 Гб оперативной памяти.

######################################################
check memory
size of reslist = 9016
size of reslist2 = 9016
check memory 2
Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21  16.81250000 MiB  16.81250000 MiB           1   @profile(precision=8)
    22                                         def my_func():
    23  16.81250000 MiB   0.00000000 MiB           1       reslist = []
    24                                         
    25 997.27343750 MiB 980.46093750 MiB        1001       for i in get_next_val():
    26 997.27343750 MiB   0.00000000 MiB        1000           reslist.append(i)
    27                                         
    28 997.27343750 MiB   0.00000000 MiB           1       print("check memory")
    29 997.27343750 MiB   0.00000000 MiB           1       time.sleep(10)
    30 1977.73437500 MiB 980.46093750 MiB        1003       reslist2 = [("!" * 1024000) for _ in range(1000)]
    31                                         
    32 1977.73437500 MiB   0.00000000 MiB           1       print(f"size of reslist = {sys.getsizeof(reslist)}")
    33 1977.73437500 MiB   0.00000000 MiB           1       print(f"size of reslist2 = {sys.getsizeof(reslist2)}")
    34 1977.73437500 MiB   0.00000000 MiB           1       print("check memory 2")
    35 1977.73437500 MiB   0.00000000 MiB           1       time.sleep(10)
    36 998.55468750 MiB -979.17968750 MiB           1       del reslist
    37  18.08593750 MiB -980.46875000 MiB           1       del reslist2


Filename: /home/nek/projects/GeekBrains/python_algos_gb/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40  16.81250000 MiB  16.81250000 MiB           1   @profile(precision=8)
    41                                         def main():
    42  17.10546875 MiB   0.29296875 MiB           1       my_func()
"""
