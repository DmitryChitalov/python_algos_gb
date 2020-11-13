"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
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


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def recursive_reverse1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse1(number // 10)}'


cProfile.run('revers(12345)')
cProfile.run('revers_2(12345)')
cProfile.run('revers_3(12345)')
cProfile.run('recursive_reverse1(12345)')

print(timeit.timeit("revers(12345)", setup="from __main__ import revers"))
print(timeit.timeit("revers_2(12345)", setup="from __main__ import revers_2"))
print(timeit.timeit("revers_3(12345)", setup="from __main__ import revers_3"))
print(timeit.timeit("recursive_reverse1(12345)", setup="from __main__ import recursive_reverse1"))

'''Из трех представленных в задании наиболее эффективно работает решение со срезами строк , хуже всего - рекурсивное решение
Ради интереса я добавила еще решение рекурсией с мемоизацией и это решение оказалось самым эффективным ,
не смотря на огромное количество вызывов функции'''