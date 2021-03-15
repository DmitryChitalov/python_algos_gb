"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from random import randint
from cProfile import run


# рекурсия
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


# цикл while
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# через срезы
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]

    return revers_num


num_100 = randint(10000000000000000, 10000000000000000000)

print('revers - рекурсия ')
print(
    timeit(
        'revers(num_100)',
        setup='from __main__ import revers, num_100',
        number=10000))

print('revers_2 - цикл while ')
print(
    timeit(
        'revers_2(num_100)',
        setup='from __main__ import revers_2, num_100',
        number=10000))

print('revers_3 - через срезы ')
print(
    timeit(
        'revers_3(num_100)',
        setup='from __main__ import revers_3, num_100',
        number=10000))

run('revers(num_100)')
run('revers_2(num_100)')
run('revers_3(num_100)')

"""
revers - рекурсия      0.016205700000000003       - самая медленная реализация
revers_2 - цикл while  0.011196499999999998       - средняя  
revers_3 - через срезы 0.003287100000000001       - самая быстая реализация

"""
