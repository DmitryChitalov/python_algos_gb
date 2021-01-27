"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000000000, 10000000000000000000)

n = 10000
print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=n))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=n))
print(
    timeit(
        "recursive_reverse(randint(100000000000000, 10000000000000000000))",
        globals=globals(),
        number=n))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            # print(f'from cache{args}')
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=n))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=n))
print(
    timeit(
        'recursive_reverse_mem(randint(100000000000000, 10000000000000000000))',
        globals=globals(),
        number=n))


"""
Мемоизация помогает при замерах timeit'ом получить ускорение на порядок. при единичном вызове функции мемоизация 
не сработает. так же мемоизация необходима при частых разворотах чисел (причем с одинаковыми остатками от деления)
в рамках одного запуска. в данном примере показывает хороший результат изза того, что одно и тоже число разворачиваем 
n раз
Это результат выполнения, в которой при вызове каждом вызове timeit'ом генерируется рандомное число для разворота (для 
чистоты эксперимента - чтоб расходы были одинаковыми, генерируем рандомное число и в неопримизированной функции)
Мемоизация замедляет выполнения вдвое.

n = 10000
Не оптимизированная функция recursive_reverse
0.012219133030157536
0.017079835990443826
0.053420550015289336
Оптимизированная функция recursive_reverse_mem
0.0013272379874251783
0.0013425510260276496
0.09855322702787817

n = 1000000
Не оптимизированная функция recursive_reverse
1.5048250610125251
1.7265853220014833
5.280357568990439
Оптимизированная функция recursive_reverse_mem
0.13589507300639525
0.14156196097610518
11.005577815987635

Вывод: мемоизация может ускорить при работе с одинаковыми числами
"""