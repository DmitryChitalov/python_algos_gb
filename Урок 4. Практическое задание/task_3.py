"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
"""
Наиболее эффективна реализация с переводом в строку и выводом ее 
в обратном порядке - так как фактически это только операции с памятью
"""
from timeit import timeit
import cProfile
import pstats

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

print('Enter decimal integer:')
in_num = int(input())

print(
    timeit(
        "revers(in_num)",
        setup='from __main__ import revers, in_num',
        number=1000))
print(
    timeit(
        "revers_2(in_num)",
        setup='from __main__ import revers_2, in_num',
        number=1000))
print(
    timeit(
        "revers_3(in_num)",
        setup='from __main__ import revers_3, in_num',
        number=1000))

cProfile.run('revers(in_num)')
cProfile.run('revers_2(in_num)')
cProfile.run('revers_3(in_num)')