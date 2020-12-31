"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

# Если я правильно поняла задание, я сделала замеры с помощью timeit и cProfile
# cProfile показал, что все функции очень быстрые, цифр больше 0 не было
# timeit показал, что в целом функции работают на одном уровне, но третья быстрее все
# И еще когда я начала проверять, заметила, что 1 и 2 функции не дописаны до конца, они не возвращали результат,
# я их немного доделала


import cProfile
from timeit import timeit
import random


def revers(enter_num, revers_num=''):
    if enter_num == 0:
        print(revers_num)
    else:
        last = enter_num % 10
        revers_num = str(revers_num) + str(last)
        enter_num = enter_num // 10
        revers(enter_num, str(revers_num))


def revers_2(enter_num, revers_num=''):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = str(revers_num) + str(num)
        enter_num = enter_num // 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = random.randint(100000, 1000000)


def main():
    revers(num)
    revers_2(num)
    revers_3(num)


print(timeit("revers", setup="from __main__ import revers", number=10000))
print(timeit("revers_2", setup="from __main__ import revers_2", number=10000))
print(timeit("revers_3", setup="from __main__ import revers_3", number=10000))
cProfile.run('main()')
