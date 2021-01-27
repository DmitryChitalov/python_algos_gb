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


'''
Не оптимизированная функция recursive_reverse
0.09791569999999998
0.06819610000000001
0.08808110000000002
Оптимизированная функция recursive_reverse_mem
0.00256099999999998
0.003402000000000016
0.0027229999999999754

Мемоизация работает быстрее в данном примере, так как функция-мемоизатор 
запоминает переданные ей значения из 10000 вызовов функции, 
поэтому значения со второго вызова начинают повторяться, и на их 
"вычисление" функция уже тратит гораздо меньше времени. 

Если проводить всего 1 вычисление для каждого числа, 
то функция с мемоизацией работает медленнее, так как на выполнение самой 
функции-мемоизатора тоже требуется время

Мой вывод - мемоизация в данном случае имеет смысл только если функция будет 
применяться для одинаковых чисел или чисел идущих по убывающей, например, 

recursive_reverse_mem(12345)
recursive_reverse_mem(1234)
recursive_reverse_mem(123)
recursive_reverse_mem(12)

В этом случае первый раз функция работает чуть дольше, а в остальные разы 
гораздо быстрее:
9.380000000000499e-05
1.8999999999991246e-06
1.6000000000043757e-06
1.6000000000043757e-06

Если числа будут каждый раз разные, 
например, 2345, 8694, 660433, 986067 то мемоизация не имеет смысла

1.630000000000381e-05
1.0700000000002374e-05
1.3200000000004875e-05
1.1700000000003374e-05

для второго примера скорость выполнения без мемоизации:
1.96000000000085e-05
1.0899999999994248e-05
2.390000000000725e-05
1.180000000000625e-05

Также она может иметь смысл для ОЧЕНЬ БОЛЬШОГО количества вычислений 
подобного рода, где есть шанс, что будут попадаться одинаковые числа. Но на 
мой взгляд процент совпадений не будет настолько велик, чтобы это дало 
ускорение работы программы в разы
'''