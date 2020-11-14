"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
#
Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import timeit
import cProfile

enter_num = int(input("Введите число"))


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


print(timeit.timeit("revers(enter_num)",
                    setup="from __main__ import revers,enter_num", number=1000))
print(timeit.timeit("revers_2(enter_num)",
                    setup="from __main__ import revers_2,enter_num", number=1000))
print(timeit.timeit("revers_3(enter_num)",
                    setup="from __main__ import revers_3,enter_num", number=1000))


"""Введите число 100
0.0012100000000003774 рекурсия ? . Квадратичная сложность О-нотации
0.0009523000000006832 Содержит цикл.
0.0006113000000000923 Константная сложность. Без цикла, без рекурсий.
 Возвращает тип str."""


cProfile.run(revers())
""" Данное сообщение у всех 3 исполнений. Достаточно малоинформативное для сравнения. 
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 proto.py:6(revers)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
cProfile.run(revers_2())
cProfile.run(revers_3())
