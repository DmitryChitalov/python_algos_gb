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


res = 0
num = 1234567898765432112345678998765432112345678987654321123456789987654321


def main():
    revers(num, res)
    revers_2(num, res)
    revers_3(num)


cProfile.run('main()')

"""
         77 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     71/1    0.000    0.000    0.000    0.000 task_3.py:17(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:27(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:35(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:44(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Все значения по нулям.
Через cProfile не получилось понять какой вариант лучше.
"""

print(timeit("revers(num, res)", setup="from __main__ import revers, num, res", number=100000))
"""3.5326546999999997"""
print(timeit("revers_2(num, res)", setup="from __main__ import revers_2, num, res", number=100000))
"""2.5164704"""
print(timeit("revers_3(num)", setup="from __main__ import revers_3, num", number=100000))
"""0.0963118999999999"""


"""
По результатам timeit делаю вывод что revers_3 самый оптимальный вариант.
"""