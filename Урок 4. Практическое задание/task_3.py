"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

"""
время работы каждой функции через timeit

0.0971826
0.0628178
0.0593071

D:\python3\python.exe "D:/python3/python_algos_gb/Урок 4. Практическое задание/task_3.py"
         12 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      6/1    0.000    0.000    0.000    0.000 task_3.py:23(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:43(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:48(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

по cProfile не видно, какая функция реализованна лучше...
по замерам timeit видно, что 3-тья функция работает быстрееб т.к. она использует встроенные функции, которые
работают быстрее
"""
from timeit import timeit
import cProfile

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

def main():
    revers(99999)
    revers_2(99999)
    revers_3(99999)

cProfile.run('main()')