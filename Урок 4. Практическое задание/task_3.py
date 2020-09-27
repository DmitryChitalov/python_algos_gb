"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from random import randint
import timeit


num_input = randint(1000000, 10000000)


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


cProfile.run('revers(num_input)')
cProfile.run('revers_2(num_input)')
cProfile.run('revers_3(num_input)')


print(timeit.timeit("revers(num_input)", setup="from __main__ import revers, num_input"))
print(timeit.timeit("revers_2(num_input)", setup="from __main__ import revers_2, num_input"))
print(timeit.timeit("revers_3(num_input)", setup="from __main__ import revers_3, num_input"))

'''
Согласно тестам, по скорости выполнения самая медленная функция - revers, а самая быстрая - revers_3.
В первом случае функция рекурсивно вызвалась 8 раз, в то время как в остальных случаях идет только 
прямой вызов по одному разу. На данном примере мы также видим, что встроенная функция для работы со строками (revers_3)
выполняется сущесвтенно быстрее, чем математические операции в цикле (revers_2). 
'''