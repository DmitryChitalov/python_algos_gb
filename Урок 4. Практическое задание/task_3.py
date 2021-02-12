"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from cProfile import run
from random import randint
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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


def revers_4(enter_num):
    n_list = list(str(enter_num))
    n_list.reverse()
    return "".join(n_list)


def main():
    for i in range(N):
        my_num = randint(1000000000, 10000000000000)
        revers_1(my_num)
        revers_2(my_num)
        revers_3(my_num)
        revers_4(my_num)


N = 10000

run('main()')

my_num = randint(1000000000, 10000000000000)
print(
    "revers_1 - ",
    timeit(
        'revers_1(my_num)',
        setup='from __main__ import revers_1, my_num',
        number=N))
print(
    "revers_2 - ",
    timeit(
        'revers_2(my_num)',
        setup='from __main__ import revers_2, my_num',
        number=N))
print(
    "revers_3 - ",
    timeit(
        'revers_3(my_num)',
        setup='from __main__ import revers_3, my_num',
        number=N))

print(
    "revers_4 - ",
    timeit(
        'revers_4(my_num)',
        setup='from __main__ import revers_4, my_num',
        number=N))

print(
    "\n1й вариант через рекурсию самый медленный, т.к. получается большое количество вызовов функции\n",
    "что сильно увеличиввает время выполнения.\n",
    "2й варинт через цикл быстрее рекурсии, т.к. циклы всегда эффективнее рекурсии\n",
    "3й варинт через срез самый быстрый, т.к. вызывается встроенная функция Питона\n",
    "4й мой варинт через преобразование числа в список и разворачивание его фукнцией reverse\n",
    "работает медленне среза, т.к. тратится время на разворот списка и на преобразование его в строку.\n",
    "Но все еще быстрее цикла, т.к. используются встроенные функции"
)
