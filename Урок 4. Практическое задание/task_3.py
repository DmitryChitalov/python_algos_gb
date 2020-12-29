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

cProfile.run('revers(123456789987654321)')
cProfile.run('revers_2(123456789987654321)')
cProfile.run('revers_3(123456789987654321)')
print(timeit('revers(123456789987654321)', 'from __main__ import revers'))
print(timeit('revers_2(123456789987654321)', 'from __main__ import revers_2'))
print(timeit('revers_3(123456789987654321)', 'from __main__ import revers_3'))
# Версия номер 3 самая эффективная, так как делает обратное число за 1 проход
# Рекурсия вызывается 19 раз, данные по времени:
# 1 - 6.271982
# 2 - 4.4030461999999995
# 3 - 0.41121319999999884

