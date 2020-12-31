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


def main():
    revers(12345678901)
    revers_2(12345678901)
    revers_3(12345678901)


cProfile.run('main()')
cProfile.run('revers(12345678901)')

print('revers   ', timeit.timeit("revers(12345678901)", "from __main__ import revers", number=1000))
print('revers_2 ', timeit.timeit("revers_2(12345678901)", "from __main__ import revers_2", number=1000))
print('revers_3 ', timeit.timeit("revers_3(12345678901)", "from __main__ import revers_3", number=1000))

# cProfile показал 0.000 для всех функций, но timeit показал, что самая быстрая функция revers_3
# revers    0.005522200000000005
# revers_2  0.005540599999999979
# revers_3  0.0006726999999999983
