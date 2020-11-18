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
from functools import lru_cache
import cProfile

num_10000 = randint(100, 10**50)


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


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@lru_cache()
def revers_4(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


@memoize
def revers_5(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


def main():
    foo = num_10000         #Для чистоты эксперемента возбмем одно число из random (а не генерировать разные 10*100 раз)
    for _ in range(100000):
        revers(foo)
        revers_2(foo)
        revers_3(foo)
        revers_4(foo)
        revers_5(foo)

cProfile.run('main()')

print(num_10000)
print("*"*100)
print(revers(num_10000))
print(revers_2(num_10000))
print(revers_3(num_10000))
print(revers_4(num_10000))
print(revers_4(num_10000))
print("*"*100)
print(timeit("revers(num_10000)", setup="from __main__ import revers, num_10000", number=100000))
print(timeit("revers_2(num_10000)", setup="from __main__ import revers_2, num_10000", number=100000))
print(timeit("revers_3(num_10000)", setup="from __main__ import revers_3, num_10000", number=100000))
print(timeit("revers_4(num_10000)", setup="from __main__ import revers_4, num_10000", number=100000))
print(timeit("revers_5(num_10000)", setup="from __main__ import revers_5, num_10000", number=100000))

'''
Для эксперимента добавил рекурсию с самонаписанной меморизацией и библиотечной 
На основе полученных данных можно сделать вывод что из предствленных функций и алгоритмов, быстрее всего рабоатет 
срез, и рекурсия с меморизацией. но возникает следующие вопросы:
Что за 5100100/100002 в ncalls что-то / число вызовов и почему вызовов на 2 больше ?
Почему рекурсия с меморизацией пишет число вызовов 1 и время 0?

Результаты работы: 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.796    7.796 <string>:1(<module>)
5100100/100002    4.818    0.000    4.818    0.000 task_3.py:20(revers)
   100000    2.548    0.000    2.548    0.000 task_3.py:30(revers_2)
   100000    0.179    0.000    0.179    0.000 task_3.py:38(revers_3)
   100000    0.044    0.000    0.044    0.000 task_3.py:47(decorate)
        1    0.000    0.000    0.000    0.000 task_3.py:57(revers_4)
        1    0.000    0.000    0.000    0.000 task_3.py:68(revers_5)
        1    0.208    0.208    7.796    7.796 task_3.py:79(main)
        1    0.000    0.000    7.796    7.796 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Рекурсия -                             3.6894048
Вычисления -                           2.4379986000000002
Срез -                                 0.12502489999999966
Рекурсия с библиотечной меморизацией - 0.013494100000000842
Рекурсия с самописной меморизацией -   0.0362486999999998
'''
