"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit
from cProfile import run


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


enter_num = [1000, 10000, 100000]

for i in enter_num:
    print(timeit('revers(i)', setup='from __main__ import revers, i', number=1_000_000))
    print(timeit('revers_2(i)', setup='from __main__ import revers_2, i', number=1_000_000))
    print(timeit('revers_3(i)', setup='from __main__ import revers_3, i', number=1_000_000), '\n')
    print(run('revers(i)'))
    print(run('revers_2(i)'))
    print(run('revers_3(i)'), '\n')


"""Выводы:
    Самая эффективная реализация - revers_3, т.к. она имеет самую простую сложность - O(n)
"""