"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from timeit import timeit
from cProfile import run

enter_num = 79865


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


print(revers_3(enter_num))
print(run('revers(enter_num)'))
print(run('revers_2(enter_num)'))
print(run('revers_3(enter_num)'))
print(timeit('revers(enter_num)', setup='from __main__ import revers, enter_num', number=1000000))
print(timeit('revers_2(enter_num)', setup='from __main__ import revers_2, enter_num', number=1000000))
print(timeit('revers_3(enter_num)', setup='from __main__ import revers_3, enter_num', number=1000000))

'''
reverse_3 является самой эффективной реализацией, т.к. имеет самую низкую сложность и занимает меньше всего времени
на обработку. Далее следует реализация через цикл - reverse_2. Рекурсивная реализация reverse имеет самую высокую 
сложность и занимает значительно больше времени на выполнение.
'''
