"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

#По результатам замеров быстрее всех оказался срез т.к. нет арифметики. cProfile что-то мне по 0 все показывает()

import cProfile
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


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

enter_num = int(input('Введите целое число:'))
revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)

print(
    'Рекурсия: ',
    timeit(
        f'revers_1({enter_num})',
        globals = globals(),
        number = 100000
    )
)

print(
    'Цикл: ',
    timeit(
        f'revers_2({enter_num})',
        globals = globals(),
        number = 100000
    )
)

print(
    'Срез: ',
    timeit(
        f'revers_3({enter_num})',
        globals = globals(),
        number = 100000
    )
)

cProfile.run('revers_1(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')