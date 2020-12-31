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
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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


def all(enter_num):
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


enter_num = randint(100000000000, 10000000000000)
cProfile.run(f'all({enter_num})')

statments = ('revers', 'revers_2', 'revers_3')

for elem in statments:
    print(timeit(f'{elem}(enter_num)', f'from __main__ import {elem}, enter_num', number=10000))

"""
           20 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     14/1    0.000    0.000    0.000    0.000 task_3.py:17(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:27(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:35(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:41(all)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


0.0341268
0.021737400000000004
0.003533500000000009

Это результаты произведенных замеров, как видно в данном случае cProfiler не дает нам полной картины скорости выполнения 
так как производится замер единичного вызова. Для более понятной интерпретации эффективнее timeit, так как дает картину
суммарного времени выполнения нескольких вызовов.
Что касается эффективности алгоритмов, то очевидно самый эффективный это revers_3 - используется 
стандартная функция (срез), менее эффективный revers_2 - так как используется цикл и сложность такого алгоритма 
равна O(n), самый не эффективный это revers - рекурсия так же имеет сложность O(n), но выполняется дольше.    
"""