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


'''
Не оптимизированная функция recursive_reverse
0.0177389
0.0201683
0.0374973

Оптимизированная функция recursive_reverse_mem
0.001513500000000001
0.001514500000000002
0.0016913999999999957

Мемоизация работает быстрее в данном примере, так как функция мемоизатор 
запоминает переданные ей значения из 10000 вызовов функции, 
поэтому значения со второго вызова начинают повторяться, и на их 
"вычисление" функция уже тратит гораздо меньше времени. 
Если проводить всего 1 вычисление для каждого числа, 
то функция с мемоизацией работает медленнее, так как на выполнение самой 
функции мемоизатора тоже требуется время

Мемоизация выгодна если функция будет применяться для одинаковых чисел или чисел идущих по убывающей, например: 

recursive_reverse_mem(123)
recursive_reverse_mem(12)

Первый раз функция работает чуть дольше, а в последующий быстрее, если числа будут каждый раз разные, 
например, 8478, 55578, 2131444, 478875468 то мемоизация не имеет смысла.
'''