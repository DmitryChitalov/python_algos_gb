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
        return '' #str(number % 10)
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


"""
    * в реализации алгоритма без мемоизации я немного изменил return для условия (if number == 0),
    мне показалось, что к строке добавляется лишний "0". 
    Очевидно, что мемоизация значительно ускоряет обработку запроса за счёт кеширования результатов
    вычислений и отсутствия необходимости в рекрсивных вызовах функции.
"""

def revesre_slice(nums):
    return str(nums)[::-1]

print('Функция с использованием срезов revesre_slice')
print(
    timeit(
        'revesre_slice(num_100)',
        setup='from __main__ import revesre_slice, num_100',
        number=10000))
print(
    timeit(
        'revesre_slice(num_1000)',
        setup='from __main__ import revesre_slice, num_1000',
        number=10000))
print(
    timeit(
        'revesre_slice(num_10000)',
        setup='from __main__ import revesre_slice, num_10000',
        number=10000))


def reverse_with_for(nums):
    reversed_str = ''
    for el in str(nums):
        reversed_str = el + reversed_str
    return reversed_str

print('Функция с использованием цикла for')
print(
    timeit(
        'reverse_with_for(num_100)',
        setup='from __main__ import reverse_with_for, num_100',
        number=10000))
print(
    timeit(
        'reverse_with_for(num_1000)',
        setup='from __main__ import reverse_with_for, num_1000',
        number=10000))
print(
    timeit(
        'reverse_with_for(num_10000)',
        setup='from __main__ import reverse_with_for, num_10000',
        number=10000))

"""
    В качестве альтернатив приведенным алгоритмам я использовал срезы и цикл for.
    Замеры однозначно показали, что алгоритм с мемоизацией обладает наименьшим временем
    исполнения несмотря на рекурсию (хотя от срезов я ожидал большего).
    Для срезов мы имеем константную сложность O(1),
    а для цикла for - сложность линейная O(n).
"""
