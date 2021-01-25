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
from cProfile import run
from time import sleep

num_10000 = randint(1000, 10000)


def revers(enter_num, revers_num=0):
    # sleep(0.5)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


print('Первое решение')
# run('revers(num_10000, revers_num=0)')
print(
    timeit(
        'revers(num_10000)',
        setup='from __main__ import revers, num_10000',
        number=100000))


def revers_2(enter_num, revers_num=0):
    # sleep(0.5)
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print('Второе решение')
# run('revers_2(num_10000, revers_num=0)')
print(
    timeit(
        'revers_2(num_10000)',
        setup='from __main__ import revers_2, num_10000',
        number=100000))


def revers_3(enter_num):
    # sleep(0.5)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Третье решение')
# run('revers_3(num_10000)')
print(
    timeit(
        'revers_3(num_10000)',
        setup='from __main__ import revers_3, num_10000',
        number=100000))


"""
Самая быстрая оказалась третья функция
Первая функция была вызвана 13 раз, и сама рекурсия внутри сама себя запускала 5 раз, и получили самое большое время
Вторая и третья отработали почти одновременно, хотя третья все таки быстрее из за того что нет математических операций 
а просто встроенный метод переворачивания строки
Если смотреть по модулю timeit то третье решение выигрывает так как наверно математические операции делаются
медленнее чем операции со строкой

timeit

Первое решение
0.144485483
Второе решение
0.08272806599999999
Третье решение
0.04683812400000001

cProfile

Первое решение
         13 function calls (9 primitive calls) in 2.513 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.513    2.513 <string>:1(<module>)
      5/1    0.000    0.000    2.513    2.513 task_3.py:20(revers)
        1    0.000    0.000    2.513    2.513 {built-in method builtins.exec}
        5    2.513    0.503    2.513    0.503 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Второе решение
         5 function calls in 0.503 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.503    0.503 <string>:1(<module>)
        1    0.000    0.000    0.503    0.503 task_3.py:40(revers_2)
        1    0.000    0.000    0.503    0.503 {built-in method builtins.exec}
        1    0.503    0.503    0.503    0.503 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Третье решение
         5 function calls in 0.504 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.504    0.504 <string>:1(<module>)
        1    0.000    0.000    0.504    0.504 task_3.py:58(revers_3)
        1    0.000    0.000    0.504    0.504 {built-in method builtins.exec}
        1    0.504    0.504    0.504    0.504 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""