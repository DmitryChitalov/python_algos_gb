"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import sys
import cProfile
from timeit import timeit


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


def main():
    revers(num)
    revers_2(num)
    revers_3(num)


sys.setrecursionlimit(10000)
num = 5464565464565464564456 ** 100
print(timeit('revers(num)', 'from __main__ import revers, num', number=100))
print(timeit('revers_2(num)', 'from __main__ import revers_2, num', number=100))
print(timeit('revers_3(num)', 'from __main__ import revers_3, num', number=100))
cProfile.run('main()')

"""
Реализация №3 revers_3 самая эфективная и быстрая, так при любом кол-ве цифр, она выполняет одинаковое кол-во шагов
Но не всегда срез выигрывает, например поиск палиндрома, лучше использовать цикл.
Но для задач подобного тпа, реалдизация со срезом, самая быстарая по всем параметрам.

"""