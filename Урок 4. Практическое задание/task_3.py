"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from timeit import Timer


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


cProfile.run('revers(1234567890)')
cProfile.run('revers_2(1234567890)')
cProfile.run('revers_3(1234567890)')

rev_1 = Timer('revers(1234567890)', 'from __main__ import revers')
print("revers 1", rev_1.timeit(number=10000), "milliseconds")
rev_2 = Timer('revers(1234567890)', 'from __main__ import revers')
print("revers 2", rev_2.timeit(number=10000), "milliseconds")
rev_3 = Timer('revers(1234567890)', 'from __main__ import revers')
print("revers 3", rev_3.timeit(number=10000), "milliseconds")

"""
Задание 3.
сравнение 
revers 1 медленнее всего, т.к. содержит рекурсию и ветвление

revers 2 быстрее revers 1 за счет исключения ветвления 

revers 3 быстрее всех, т.к. использует встроенную функцию 
"""