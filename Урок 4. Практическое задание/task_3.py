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


def start_func():
    a = 123456789
    b = revers(a)
    c = revers_2(a)
    d = revers_3(a)
    # print(a, b, c, d)
    # print(type(b), type(c), type(d))


a = 123456789
cProfile.run('start_func()')    # cPrifile показывает 0 милисекунд на каждом реверсе, невозможно составить суждение о скорости
print(
    timeit.timeit(
        "start_func()",
        setup='from __main__ import start_func',
        number=10000))  # общее время составило 0.121919037
print(
    timeit.timeit(
        "revers(a)",
        setup='from __main__ import revers, a',
        number=10000))  # время на функцию реверс 0.0642847159 №3
print(
    timeit.timeit(
        "revers_2(a)",
        setup='from __main__ import revers_2, a',
        number=10000))  # время на функцию реверс_2 0.0394758540 №2
print(
    timeit.timeit(
        "revers_3(a)",
        setup='from __main__ import revers_3, a',
        number=10000))  # время на функцию реверс_3 0.0067838000 №1

"""Самым эффективным оказался, совершенно ожидаемо, реверс_3, состоящий буквально из 2ух строчек кода.
Но возвращаемое им значение относится к классу строковых, значит функция работает не только с числами,
но и с любыми строками. Для задачи с обращением числа, нет никаких проблем, помня о модуле int() и проверке isdigit().
Реверс_2 на своём втором месте с циклом while, с элеганстным математическим фыражением (revers_num + num / 10) * 10,
аккуратно добавляет по одной цифре из входного числа. Возвращает число в типе float
Реверс_3 справляется с задачей в 2 раза дольше чем реверс_2, совершая итераций равных длине числа."""
