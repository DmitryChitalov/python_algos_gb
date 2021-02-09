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
"""
Анализировались три решения. В качестве параметра передавались числа 5, 7 и 13ти значные.
длина числа     обычная рекурсия        рекурсия+memorise        работа со строкой
5               0.0435754               0.002750499999999989     0.005266699999999985
7               0.052200099999999985    0.0031730999999999843    0.005270600000000014
13              0.08682839999999997     0.004623900000000014     0.007610199999999984

Видно, что наилучшим решением явялется решение с помощью рекурсии и memorise. 
Оно оказывается на порядок лучше остальных. 
Кроме этого можно заметить, что с увеличением размерности числа время практически не увеличивается.
(Здесь похоже на логарифмическую функцию, а по другим замерам вообще Const)
Решение через работу со строкой получилось очень лаконичным и достаточно эффективнм. В несколько раз проигрывает
оптимизированной функции. Увеличение числа на времени исполнения практически не отражается. 

(Похоже на y = kn, k-const)

Итого меморизация сильно ускоряет решение!
"""
from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)
num_10000 = randint(1000000000000000, 100000000000000000)

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


def my_reverse(number):
    number_str = str(number)
    reverse_str = number_str[::-1]
    return int(reverse_str)


print('Работа со строкой: my_reverse')
print(
    timeit(
        'my_reverse(num_100)',
        setup='from __main__ import my_reverse, num_100',
        number=10000))
print(
    timeit(
        'my_reverse(num_1000)',
        setup='from __main__ import my_reverse, num_1000',
        number=10000))
print(
    timeit(
        'my_reverse(num_10000)',
        setup='from __main__ import my_reverse, num_10000',
        number=10000))

print(num_100)
print(num_1000)
print(num_10000)
