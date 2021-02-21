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
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


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


test_num = randint(1000000, 100000000)
#print(test_num)

#print(revers(test_num))
print(timeit("revers(test_num)", globals=globals(), number=1000))
#print(revers_2(test_num))
print(timeit("revers_2(test_num)", globals=globals(), number=1000))
#print(revers_3(test_num))
print(timeit("revers_3(test_num)", globals=globals(), number=1000))

cProfile.run('revers(test_num)')
cProfile.run('revers_2(test_num)')
cProfile.run('revers_3(test_num)')

#Реализация через срез быстрее т.к. не требует выполнения арифметических операций
