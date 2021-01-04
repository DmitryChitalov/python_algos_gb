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
from random import randint

num_100 = randint(10000, 1000000)


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


print('revers')
print(
    timeit(
        'revers(num_100)',
        setup='from __main__ import revers, num_100',
        number=10000))

print('revers_2')
print(
    timeit(
        'revers_2(num_100)',
        setup='from __main__ import revers_2, num_100',
        number=10000))

print('revers_3')
print(
    timeit(
        'revers_3(num_100)',
        setup='from __main__ import revers_3, num_100',
        number=10000))


def main():
    revers(num_100),
    revers_2(num_100),
    revers_3(num_100)


cProfile.run('main()')

"""
revers
0.012249699999999999
revers_2
0.008478499999999996
revers_3
0.002529499999999997
  
3 алгоритм самый эффективный исходя из результатов timeit, в нем используетсе встроенный метод
среза, когда в первых двух используется рекурсия и цикл.
"""