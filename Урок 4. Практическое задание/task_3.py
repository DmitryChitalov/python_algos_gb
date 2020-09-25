"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


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

import cProfile
from timeit import timeit

enter_num = 8475058


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


print(timeit('revers', setup='from __main__ import revers', number=1000000))
print(timeit('revers_2', setup='from __main__ import revers_2', number=1000000))
print(timeit('revers_3', setup='from __main__ import revers_3', number=1000000))


def main(*args):
    revers(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)


cProfile.run('main()')
#   Функция revers - написана с помощью рекурсии, а она как известно замедляет работу кода.
#cProfile показал что функция с рекурсией вызывалась 8 раз, когда остальные всего 1.
#   Функция revers_2 - содержит много строк кода содержащих вычисления и бессконечный цикл. сложность - O(N)
#   Функция revers_3 -Написана с помощью смены типизации данных и имеет сложность O(b-a), что выше и быстрее O(N)
#Профилировщик не выявил узких\уязвимых мест у всех функций, так что не вижу смысла их улучшать.
# 0.04256520000000001
# 0.03551979999999999
# 0.030427800000000005
#         14 function calls (7 primitive calls) in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 12345.py:17(revers_2)
#        1    0.000    0.000    0.000    0.000 12345.py:25(revers_3)
#        1    0.000    0.000    0.000    0.000 12345.py:36(main)
#      8/1    0.000    0.000    0.000    0.000 12345.py:7(revers)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}