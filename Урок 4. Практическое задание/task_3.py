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
from timeit import timeit

"""
def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate
"""


#@memoize
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return f'{revers_num}'
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return f'{revers(enter_num, revers_num)}'


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


def main():                         # основная функция вызова всех входимых в нее функций
    res_1 = revers(number)
    res_2 = revers_2(number)
    res_3 = revers_3(number)


number = randint(10000000000, 100000000000)     # вводимое число
cProfile.run('main()')                          # вызов Профилировки всех алгоритмов

print('Рекурсивная функция revers')                     # вывод времени выполнения 1й ф-ии с помощью timeit
print(
    timeit(
        'revers(number)',
        setup='from __main__ import revers, number',
        number=10000))

print('Функция с циклом while revers_2')                # вывод времени выполнения 2й ф-ии с помощью timeit
print(
    timeit(
        'revers_2(number)',
        setup='from __main__ import revers_2, number',
        number=10000))

print('Функция revers_3')                               # вывод времени выполнения 3й ф-ии с помощью timeit
print(
    timeit(
        'revers_3(number)',
        setup='from __main__ import revers_3, number',
        number=10000))

"""Результаты: Профилировка с помощью cProfile показала, что каждый из 3х алгоритмов достаточно оптимизирован.
   1) Рекурсивная функция <<revers>> оказалась самой изящной, но и самой медленной (количество вызовов 
      ncalls составило 12). 
      Но мы уже знаем, что ее можно оптимизировать засчет мемоизации. 
   2) Функция с циклом while <<revers_2>> занимает второе место по скорости выполнения. Количество итераций
      цикла зависит от длины вводимого числа. При каждой итерации производятся вычисления как с вводимым числом, 
      так и с результирующим.
   3) Функция revers_3 оказалась самой быстрой. Она использует стандартную функцию перевода числа в строковый
      тип str и срез строки с обратным шагом. 
   Вывод: иногда самое простое решение оказывается самым лаконичным и быстрым. 
   Также существуют другие решения, которые можно использьзовать. И если они кажутся недостаточно быстрыми, 
   то их можно попробовать оптимизировать.
   Вопрос, стоит ли тратить время на написание длинного кода ради выгоды в долях ms, когда можно 
   получить нужный результат с помощью стандартных функций за относительно такое же время и двигаться дальше.
   """
