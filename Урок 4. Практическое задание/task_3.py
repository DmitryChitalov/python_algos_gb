"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile
from random import randint

number = randint(10000, 10000000000)


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


print(timeit('revers(number, revers_num=0)', setup='from __main__ import revers, number', number=100000))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


print(timeit('revers_2(number, revers_num=0)', setup='from __main__ import revers_2, number', number=100000))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    revers(number)
    revers_2(number)
    revers_3(number)


print(timeit('revers_3(number)', setup='from __main__ import revers_3, number', number=100000))
cProfile.run('main()')
"""
Как видно ниже, рекурсивная функция самая медленная. Так как в ней содержится 11 вызовов самой себя.
Эфективнее всего функция номер 3 так как в ней нет рекурсии и нет цикла, ее сложность константная.
P.S. первая функция не рабочая была, в if не хватало что возвращать int(revers_num), в else не хватало команды return.
0.305877604
0.19486031399999998
0.043144406999999996
         17 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     11/1    0.000    0.000    0.000    0.000 task_3.py:19(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:32(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:43(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:49(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""