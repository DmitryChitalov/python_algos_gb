"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from random import randint
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


enter_num = randint(10000000000000, 1000000000000000000000000000)

run('revers(enter_num)')
run('revers_2(enter_num)')
run('revers_3(enter_num)')
print(f" revers {timeit('revers(enter_num)', number=10000, globals=globals())}")
print(f" revers_2 {timeit('revers_2(enter_num)', number=10000, globals=globals())}")
print(f" revers_3 {timeit('revers_3(enter_num)', number=10000, globals=globals())}")

# cProfile ничего нам не показал
# revers и revers2 дольше из-за рекурсии. revers3 лучший вариант.
