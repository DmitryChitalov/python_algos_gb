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
import cProfile

num_100 = 99 ** 99


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


print("Время выполнения 1-го варианта: ")
print(timeit(
    'revers(num_100)',
    setup='from __main__ import revers, num_100',
    number=10000))

print("Время выполнения 2-го варианта: ")
print(timeit(
    'revers_2(num_100)',
    setup='from __main__ import revers_2, num_100',
    number=10000))

print("Время выполнения 3-го варианта: ")
print(timeit(
    'revers_3(num_100)',
    setup='from __main__ import revers_3, num_100',
    number=10000))


def main():
    revers(num_100),
    revers_2(num_100),
    revers_3(num_100)


cProfile.run('main()')

"""
Эффективней 3-й алгоритм, т.к используется встроенная функция - python. 
В 1м и 2м алгоритме используется рекурсия и цикл, что не эффективно, нужна оптимизация
"""
