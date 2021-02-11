"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run
from random import randint


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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

def revers_4(enter_num):
    return reversed(str(enter_num))

def main():
    num_10000 = randint(100000000, 10000000000000)
    revers_1(num_10000)
    revers_2(num_10000)
    revers_3(num_10000)


run('main()')
num_10000 = randint(100000000, 10000000000000)
run('revers_1(num_10000)')
run('revers_2(num_10000)')
run('revers_3(num_10000)')

num_10000 = randint(100000000, 10000000000000)
print(f"revers_1", end=' ')
print(timeit("revers_1(num_10000)", number=10000, globals=globals()))
print(f"revers_2", end=' ')
print(timeit("revers_2(num_10000)", number=10000, globals=globals()))
print(f"revers_3", end=' ')
print(timeit("revers_3(num_10000)", number=10000, globals=globals()))
print(f"revers_4", end=' ')
print(timeit("revers_4(num_10000)", number=10000, globals=globals()))


#          26 function calls (13 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#         1    0.000    0.000    0.000    0.000 random.py:244(randint)
#         1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      14/1    0.001    0.000    0.001    0.001 task_3.py:20(revers_1)
#         1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
#         1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
#         1    0.000    0.000    0.001    0.001 task_3.py:44(main)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#          17 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      14/1    0.000    0.000    0.000    0.000 task_3.py:20(revers_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:30(revers_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# revers_1 0.05910449999999999
# revers_2 0.04301150000000001
# revers_3 0.004994300000000007
#
# revers_3 эффективнее т.к. работает со срезом/строкой, без арифметики и рекурсии
# Свое решение даже чуть быстрее отрабатывает:
# def revers_4(enter_num):
#     return reversed(str(enter_num))