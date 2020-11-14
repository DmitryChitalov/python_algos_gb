"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile
import random

num = random.randint(100000000, 1000000000)


def reverse(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        reverse(enter_num, revers_num)


def reverse_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def reverse_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(
    timeit(
        "reverse(num)",
        setup='from __main__ import reverse, num',
        number=10000))
print(
    timeit(
        "reverse_2(num)",
        setup='from __main__ import reverse_2, num',
        number=10000))
print(
    timeit(
        "reverse_3(num)",
        setup='from __main__ import reverse_3, num',
        number=10000))


cProfile.run('reverse(num)')
cProfile.run('reverse_2(num)')
cProfile.run('reverse_3(num)')

'''
Выводы: Из представленных алгоритмов наиболее эффективна функция со встроенными
строковыми методами № 3. Модуль cProfile оказался не показателен на быстрых функциях,
хотя сообщил о рекурсивности в первой функции
'''