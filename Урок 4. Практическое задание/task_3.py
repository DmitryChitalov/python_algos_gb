"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from timeit import timeit
import sys


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def bench_revers():
    action = "revers(test_num)"
    setup = "from __main__ import revers"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_revers_2():
    action = "revers_2(test_num)"
    setup = "from __main__ import revers"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_revers_3():
    action = "revers_3(test_num)"
    setup = "from __main__ import revers"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def main():
    pass
    try:
        global test_num
        test_num = 12345678901234567890
        time_revers = bench_revers()
        time_revers_2 = bench_revers_2()
        time_revers_3 = bench_revers_3()

        print("#" * 40)
        print(f"Время выполнения через timeit функции revers \t{time_revers}")
        print("Профилировние")
        cProfile.run(f"revers({test_num})")
        print("#" * 40)
        print(f"Время выполнения через timeit функции revers_2 \t{time_revers_2}")
        print("Профилировние")
        cProfile.run(f"revers_2({test_num})")
        print("#" * 40)
        print(f"Время выполнения через timeit функции revers_3 \t{time_revers_3}")
        print("Профилировние")
        cProfile.run(f"revers_3({test_num})")
        print("#" * 40)

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
########################################
Время выполнения через timeit функции revers 	0.04571147300157463
Профилировние
         24 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     21/1    0.000    0.000    0.000    0.000 task_3.py:18(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

########################################
Время выполнения через timeit функции revers_2 	0.02880726900184527
Профилировние
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:28(revers_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


########################################
Время выполнения через timeit функции revers_3 	0.002803299001243431
Профилировние
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_3.py:36(revers_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


########################################

Программа завершена!

Вывод по програмной сложности (количество вызовов функций и модулей) варианты revers_2 и revers_3 равны.
Но с точки зрения вычеслений revers_3 более эффективен, как показывает функция timeit.
 

"""
