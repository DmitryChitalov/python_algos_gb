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


def start():
    revers(n)
    revers_2(n)
    revers_3(n)


n = randint(1000000,10000000)


cProfile.run('start()')

print ('Измерения с помощью timeit')
print (timeit('revers(n)',setup='from __main__ import revers,n', number=10000))
print (timeit('revers_2(n)',setup='from __main__ import revers_2,n', number=10000))
print (timeit('revers_3(n)',setup='from __main__ import revers_3,n', number=10000))

"""
Выводы: первая функция не работала ( в ней была ошибка)

С помощью модуля timeIt можно определить какая из реализаций быстрее
3-я реализация самая быстрая

С помощью cProfile можно увидеть количество вызовов рекурсивно функции ( в данном случае 8)

Результаты профилировки:
        14 function calls (7 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      8/1    0.000    0.000    0.000    0.000 task_3.py:15(revers)
        1    0.000    0.000    0.000    0.000 task_3.py:26(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:34(revers_3)
        1    0.000    0.000    0.000    0.000 task_3.py:40(start)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    Измерения с помощью timeit
        0.026461556999999997
        0.010902398000000008
        0.0035092050000000014

"""