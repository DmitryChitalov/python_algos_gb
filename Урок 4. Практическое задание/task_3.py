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

print(revers(123))
print(revers_2(123))
print(revers_3(123))

setup = 'from __main__ import revers, revers_2, revers_3 '
# cProfile.run('revers(123)')
# print(timeit('revers(123)', setup=setup), 'revers')
# cProfile.run('revers_2(123)')
# print(timeit('revers(132)', setup=setup), 'revers_2')
# cProfile.run('revers_3(123)')
# print(timeit('revers_3(123)', setup=setup),'revers_3')
