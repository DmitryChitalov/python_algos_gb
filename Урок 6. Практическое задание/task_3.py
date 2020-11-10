"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from memory_profiler import profile, memory_usage
from time import process_time
from pympler import asizeof
from sys import getsizeof
from random import randint


@profile()
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = 123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
revers_3(num)
# print(asizeof.asizeof(revers_3(num)))
# print(getsizeof(revers_3(num)))

"""
 Т.к. рекурсия вызвает сама себя, видимо происходит и повторный вызов декаратора
 возможно тогда нужно делать измерения по отсечкам до и после, а не использую декоратор
"""
