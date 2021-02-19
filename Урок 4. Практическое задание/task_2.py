"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации,
если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

from timeit import timeit
from random import randint


# Без мемоизации
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse:')
print(
    timeit(
        "recursive_reverse(num_100)",
        globals=globals(),
        number=100000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        globals=globals(),
        number=100000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        globals=globals(),
        number=100000))

print()


# С мемоизацией
def memoize(f):  # декоратор memoize, f - функция-аргумент
    cache = {}

    def decorate(*args):  # функция-обёртка

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)  # f - это будет recursive_reverse_mem
            return cache[args]

    return decorate  # возврат функции-обёртки


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem:')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        globals=globals(),
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        globals=globals(),
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        globals=globals(),
        number=100000))

"""
Не оптимизированная функция recursive_reverse:
0.281369348
0.31858060399999993
0.6150991250000001

Оптимизированная функция recursive_reverse_mem:
0.023437659999999916
0.02317926800000003
0.023351931999999964
"""
# Ответ на ? "Есть ли смысл применять мемоизацию?"
# на замерах видно, что практически на порядок отличается время
# выполнения функции с мемоизацией и без неё. То есть ответ: смысл есть.
