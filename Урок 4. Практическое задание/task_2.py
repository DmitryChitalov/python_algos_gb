"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

# Вариант 3. Реализация через строки

def reverse_num(number):
    """ 
    Выводит цыфры числа в обратном порядке
    1234 -> 4321
    """
    digits = str(number) # кастуем целое число в строку
    return int(digits[::-1]) # выводим в обратном порядку

print("Проверка на числе 1234",reverse_num(1234))


print("Реализация через строки")
print(
    timeit(
        'reverse_num(num_10000)',
        setup='from __main__ import reverse_num, num_10000',
        number=100))



print(
    timeit(
        'reverse_num(num_10000)',
        setup='from __main__ import reverse_num, num_10000',
        number=1000))


print(
    timeit(
        'reverse_num(num_10000)',
        setup='from __main__ import reverse_num, num_10000',
        number=10000))


""" 
python3 'Урок 4. Практическое задание/task_2.py'
Не оптимизированная функция recursive_reverse
0.04699776099732844
0.0901618799980497
0.10288136600138387
Оптимизированная функция recursive_reverse_mem
0.00304687800235115
0.0027225290032220073
0.0029481449964805506
Проверка на числе 1234 4321
Реализация через строки
6.573600694537163e-05
0.0009218310005962849
0.0061399669939419255

Быстродейстие реализации через массивы и строки значительно выше так как не используются ресурсоемкие операции деления, накопление данных в аппартном стеке в случае рекурсии. Идут операции по кастованию типов и копирование извлечение данных из памяти.

Мемоизация позволяет в данном случае значительно сократить время выполнения, поскольку среди случайно выпавших чисел значительное количество повторяется. Поэтому сохранение предыдущих вычислений позволяет избегать излишних операций деления. 
"""