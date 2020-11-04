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


input_num = 12345354849653548978952343216310608459840201601749

print(
    timeit(
        'revers(input_num)',
        setup='from __main__ import revers, input_num',
        number=10000))

print(
    timeit(
        'revers_2(input_num)',
        setup='from __main__ import revers_2, input_num',
        number=10000))

print(
    timeit(
        'revers_3(input_num)',
        setup='from __main__ import revers_3, input_num',
        number=10000))


def main():
    print()
    print(revers(input_num), revers_2(input_num), revers_3(input_num))
    print()


cProfile.run('main()')

"""
0.6843466620048275
0.39150333699944895
0.01699999099946581

None 9.471061020489546e+49 94710610204895480601361234325987984535694845354321

         60 function calls (10 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     51/1    0.000    0.000    0.000    0.000 task_3.py:16(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:63(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

timeit четко показывает, что каждая последующая реализации более эффективна.
revers_3() самая быстрая, так как без всяких причуд выполняется двумя встроенными функциями
cProfile показал отсутствие проблемных по времени для всех функций
P.S. revers() выдаёт None
"""
