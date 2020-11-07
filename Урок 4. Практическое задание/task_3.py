"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import timeit

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


print('Измерение функции revers - Рекурсия:')
cProfile.run('revers(1000000)')
print(timeit.timeit("revers(1000000)", setup="from __main__ import revers", number=10000))

print('Измерение функции revers_2 - Цикл While:')
cProfile.run('revers_2(1000000)')
print(timeit.timeit("revers_2(1000000)", setup="from __main__ import revers_2", number=10000))

print('Измерение функции revers_3 - Срез:')
cProfile.run('revers_3(1000000)')
print(timeit.timeit("revers_3(1000000)", setup="from __main__ import revers_3", number=10000))


"""
Результаты по модулю timeit:

Цикл - 0.046281251999999995
Рекурсия - 0.04639191800000003
Срез - 0.012074646000000022

По результатам можно сделать вывод, что:
Рекурсия, как и цикл, ожидаемо, занимает большее количество времени, чем срез.
"""
