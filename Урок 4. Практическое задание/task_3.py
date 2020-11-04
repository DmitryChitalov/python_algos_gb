"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""


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
    return int(revers_num)


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


from timeit import timeit
import cProfile, time

num = 123456789

#print(timeit('revers(num)', setup = 'from __main__ import revers, num', number = 1000))
#print(timeit('revers_2(num)', setup = 'from __main__ import revers_2, num', number = 1000))
#print(timeit('revers_3(num)', setup = 'from __main__ import revers_3, num', number = 1000))

def upper(f):
    #time.sleep(1)
    return timeit(f.__name__+'(num)', setup = f'from __main__ import {f.__name__}, num', number = 10000)

for i in [revers, revers_2, revers_3]:
    print(f'{upper(i)} {i.__name__}')


def all_():
    num = 123456789
    revers(num)
    revers_2(num)
    revers_3(num)

cProfile.run('all_()')

# первая - затратная рекурсия
# вторая - обычный цикл
# третья - встроенные функции. (не знал, что так можно [::-1])

