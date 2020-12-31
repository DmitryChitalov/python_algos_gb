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


number = 352352352

print(
    timeit(
        "revers(number)",
        setup='from __main__ import revers, number',
        number=10000))
print(
    timeit(
        "revers_2(number)",
        setup='from __main__ import revers_2, number',
        number=10000))
print(
    timeit(
        "revers_3(number)",
        setup='from __main__ import revers_3, number',
        number=10000))


def main():
    number = 352352352
    revers(number)
    revers_2(number)
    revers_3(number)


cProfile.run('main()')

"""
Результаты timeit:
0.030475350000000012
0.018989254999999983
0.004533014000000002

Результаты cProfile:
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 task_3.py:16(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:58(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Выводы:
первый метод медленный, т.к. использует рекурсию
второй вариант быстрее первого, т.к. работает через цикл
третий вариант быстрее, т.к. работает с переворотом строки вместо арифметических операций
"""
