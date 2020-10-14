"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from timeit import timeit


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


cProfile.run('revers(123)')
cProfile.run('revers_2(123)')
cProfile.run('revers_3(123)')
print(
    "timeit функции revers: "
    f"{timeit('revers(123)', setup='from __main__ import revers', number=1000)}")
print(
    "timeit функции revers_2: "
    f"{timeit('revers_2(123)', setup='from __main__ import revers_2', number=1000)}")
print(
    "timeit функции revers_3: "
    f"{timeit('revers_3(123)', setup='from __main__ import revers_3', number=1000)}")

# Вывод: в данном случае лучше использование timeit, тк значения времени не округляются и они более точны (скорее даже
# они просто выводятся хотя бы, в отличии от cProfile :) )
# Самая быстрая функция - revers_3, тк самая простая реализация - превратить число в строку и прочитать с конца, все
# остальное же требует больше времени из-за использования циклов/рекурсий.
