"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import timeit

enter_num = 123456789
revers_num = 0


def revers(enter_num, revers_num=0):
    num = 0
    if enter_num == 0:
        return int(revers_num + num / 10)
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
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def main():
    revers(enter_num, revers_num=0)
    revers_2(enter_num, revers_num=0)
    revers_3(enter_num)


print(revers(123456789, 0))
print(revers_2(123456789, 0))
print(revers_3(123456789))

print(timeit.timeit("revers(enter_num, revers_num=0)", setup="from __main__ import revers, enter_num"))
print(timeit.timeit("revers_2(enter_num, revers_num=0)", setup="from __main__ import revers_2, enter_num, revers_num"))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num"))

cProfile.run('main()')

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      10/1    0.000    0.000    0.000    0.000 hW_4_task_3.py:19(revers)
#         1    0.000    0.000    0.000    0.000 hW_4_task_3.py:30(revers_2)
#         1    0.000    0.000    0.000    0.000 hW_4_task_3.py:38(revers_3)
#         1    0.000    0.000    0.000    0.000 hW_4_task_3.py:43(main)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}