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


num_100 = randint(10000, 1000000000)
num_1000 = randint(1000000, 10000000000)
num_10000 = randint(100000000, 100000000000000000)

"""Делаем замеры с помощью cProfile"""

print("\n Замеры функции revers\n ")

run('revers(num_100)')
run('revers(num_1000)')
run('revers(num_10000)')

print("\n Замеры функции revers_2\n ")

run('revers_2(num_100)')
run('revers_2(num_1000)')
run('revers_2(num_10000)')

print("\n Замеры функции revers_3\n ")

run('revers_3(num_100)')
run('revers_3(num_1000)')
run('revers_3(num_10000)')

"""Делаем замеры с помощью timeit"""

print("\n3 функции на num_100\n")

print(timeit("revers(num_100)", globals=globals(), number=10000))
print(timeit("revers_2(num_100)", globals=globals(), number=10000))
print(timeit("revers_3(num_100)", globals=globals(), number=10000))

print("\n3 функции на num_1000\n")

print(timeit("revers(num_1000)", globals=globals(), number=10000))
print(timeit("revers_2(num_1000)", globals=globals(), number=10000))
print(timeit("revers_3(num_1000)", globals=globals(), number=10000))

print("\n3 функции на num_10000\n")

print(timeit("revers(num_10000)", globals=globals(), number=10000))
print(timeit("revers_2(num_10000)", globals=globals(), number=10000))
print(timeit("revers_3(num_10000)", globals=globals(), number=10000))


#По полученным данным видно, что быстрее всего третья фенкция revers_3 - срез, т.к в ней нет никаких арифметических
#операций