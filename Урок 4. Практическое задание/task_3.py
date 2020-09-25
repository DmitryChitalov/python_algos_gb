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


def rev_main(n):
    for i in range(100000):
        revers(n)
        revers_2(n)
        revers_3(n)

num = 123456
print('Функция revers():  ', end=' ')
print(
    timeit(
        'revers(num)',
        setup='from __main__ import revers, num',
        number=10000))
print('Функция revers_2():', end=' ')
print(
    timeit(
        'revers_2(num)',
        setup='from __main__ import revers_2, num',
        number=10000))
print('Функция revers_3():', end=' ')
print(
    timeit(
        'revers_3(num)',
        setup='from __main__ import revers_3, num',
        number=10000))

cProfile.run('rev_main(123456)')

"""
Функция revers():   0.022272200000000002
Функция revers_2(): 0.0145541
Функция revers_3(): 0.004674499999999998

Из результата видно что самый эфективный метотод в котором используютя средства pyhon срезы, при чем значительно быстрей
чем другии методы. Самый медленный метод с рекурсией, цикл немного быстрей (интересно почему?)

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.675    0.675 <string>:1(<module>)
700000/100000    0.375    0.000    0.375    0.000 task_3.py:16(revers)
   100000    0.160    0.000    0.160    0.000 task_3.py:26(revers_2)
   100000    0.054    0.000    0.054    0.000 task_3.py:34(revers_3)
        1    0.086    0.086    0.675    0.675 task_3.py:40(rev_main)
        1    0.000    0.000    0.675    0.675 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Судя по результатам профилировщика, метод с рекурсией совсем медлено работает, в два раза быстрей цикл, и самый быстрый
обратный срез.
"""