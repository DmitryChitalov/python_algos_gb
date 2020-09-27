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

# решение через рекурсию - это заведомо долгое.
# Причем: при небольших значениях рекурсия не так долго работает,
# но когда числа большие - то мы начинаем заполнять стек огромным количеством вызовов и время начинает расти:
# чем больше больше числа, тем дороже нам обходится рекурсия.

# Решение через срезы медленное, так как срезы - это не in place --> на создание каждого объекта уходит время.

# А самое быстрое решение - через старый добрый цикл

# причем исследования через timeit это подтверджают, а cProfile показал всё по нулям - типа всё ок и улучшать нечего.


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Функция revers: ')

print(
    timeit(
        "revers(num_100)",
        setup='from __main__ import revers, num_100',
        number=100000))
print(
    timeit(
        "revers(num_1000)",
        setup='from __main__ import revers, num_1000',
        number=100000))
print(
    timeit(
        "revers(num_10000)",
        setup='from __main__ import revers, num_10000',
        number=100000))

print()
cProfile.run('revers(num_10000)')

# Самое быстрое решение - через старый добрый цикл


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print('Функция revers_2')
print(
    timeit(
        "revers_2(num_100)",
        setup='from __main__ import revers_2, num_100',
        number=100000))
print(
    timeit(
        "revers_2(num_1000)",
        setup='from __main__ import revers_2, num_1000',
        number=100000))
print(
    timeit(
        "revers_2(num_10000)",
        setup='from __main__ import revers_2, num_10000',
        number=100000))

print()
cProfile.run('revers_2(num_10000)')

# Решение через срезы медленное так как срезы - это не in place --> на создание каждого объекта уходит время


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Функция revers_3')
print(
    timeit(
        "revers_3(num_100)",
        setup='from __main__ import revers_3, num_100',
        number=100000))
print(
    timeit(
        "revers_3(num_1000)",
        setup='from __main__ import revers_3, num_1000',
        number=100000))
print(
    timeit(
        "revers_3(num_10000)",
        setup='from __main__ import revers_3, num_10000',
        number=100000))

print()
cProfile.run('revers_3(num_10000)')
