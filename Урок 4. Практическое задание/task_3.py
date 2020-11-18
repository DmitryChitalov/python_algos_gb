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


print('Через Timeit')
nums = randint(10000,1000000)
revers(nums)
revers_2(nums)
revers_3(nums)


# print(f'Функция с использованием рекурсии: '
#       f'{timeit("revers(nums)", setup="from __main__ import revers_2", number=100000)})
# print(f'Функция с использованием рекурсии: '
#       f'{timeit("revers_2(nums)", setup="from __main__ import revers_2", number=100000)})
# print(f'Функция с использованием рекурсии: '
#       f'{timeit("revers_3(nums)", setup="from __main__ import revers_3", number=100000)})

cProfile.run('revers(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')

# Как и ожидалось самый быстрый способ это срез, но у меня не получается запустить функцию
