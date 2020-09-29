"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import timeit
import cProfile


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


enter_num = int(input('введите число: '))
revers(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
"""
def main():
    enter_num = 123456
    revers(enter_num, revers_num=0)
    revers_2(enter_num, revers_num=0)
    revers_3(enter_num)
print(timeit.timeit("main()", setup="from __main__ import main", number=1000))
"""
print(timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=1000))
print(timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=1000))
print(timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=1000))

cProfile.run('revers(100)')
cProfile.run('revers_2(100)')
cProfile.run('revers_3(100)')

"""
Самым эффективным по времени оказался 3 метод, метод используемый срезы.
в 1 и 2 функциях используются арифметические действия, именно из-за них и ухудшается результат

"""