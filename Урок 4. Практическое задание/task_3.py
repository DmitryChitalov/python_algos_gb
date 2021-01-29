"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from random import randint
import cProfile
import sys


sys.setrecursionlimit(10000)


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


enter_num = 13579551  # определим входное значение числа, которое будем преворачивать


print(timeit("revers(enter_num)", globals=globals()))
print(timeit("revers_2(enter_num)", globals=globals()))
print(timeit("revers_3(enter_num)", globals=globals()))


"""
3.5822159 - 1 метод решается рекурсивно, самое низкое быстродействие
2.7327783 - 2 метод решение через цикл. Лучше чем рекурсия, но всё равно не самый удачный
0.5752480000000002 - 3 метод, решение через встроенную функцию среза ( самый быстрый и эффективный метод )
"""


def cProfile_func():
    enter_num = randint(99998**1000, 99999**1000)  # хотим большое число для наглядных замеров
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


cProfile_func()
cProfile.run('cProfile_func()')

"""

  5012 function calls (12 primitive calls) in 0.128 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.128    0.128 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:200(randrange)
        1    0.000    0.000    0.000    0.000 random.py:244(randint)
        1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
   5001/1    0.068!!! 0.000    0.068    0.068 task_3.py:21(revers)  # 1 метод 
        1    0.058!!! 0.058    0.058    0.058 task_3.py:31(revers_2)  # 2 метод 
        1    0.002!!! 0.002    0.002    0.002 task_3.py:39(revers_3)  #  3 метод 
        1    0.000    0.000    0.128    0.128 task_3.py:59(cProfile_func)
        1    0.000    0.000    0.128    0.128 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
  4015 function calls (15 primitive calls) in 0.084 seconds

При решении через cProfile можно сделать такие же выводы, как и при решении через timeit, 
однако  через timeit лаконичнее, удобнее, нагляднее, особенно при небольших значениях количества вызовов
"""
