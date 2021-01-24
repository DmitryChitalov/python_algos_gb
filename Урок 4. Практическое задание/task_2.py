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


"""
При запуске расчета по 1-му числу один раз меморизация не нужна, так как на 1 проходе она вообще не будет 
использоваться: при первом проходе в кэш будут записываться {срез: перевернутый срез} числа до того момента, 
пока срезанное число не станет иметь 0-вую длину. При этом, если мы рассчитали один срез одной длины, то в дальнейшем
алгоритме он использоваться не будет, так как его длина всегда больше, чем следующие рассчитанные срезы.

Если запускать расчет по одному и тому же числу много раз, то на 2 и последующих рассчетах механизм рекурсии
не будет использоваться вообще, так как в кэше вся необходимая информация уже будет иметься.

Если запускать расчет по нескольким числам последовательно, то в первых расчетах меморизация будт бесполезна, однако 
в будущих расчетах она оптимизирует расчет, если срез разрядов рассчитываемого числа 
совпадет с разрядами уже рассчитанных чисел, так как в кэше уже будет информация по расчетам этих срезов.

Для оптимизации можно уйти от рекурсии к циклу


Не оптимизированная функция recursive_reverse
0.07031221100000001
0.090391093
0.161577115
Оптимизированная функция recursive_reverse_mem
0.004480556999999996
0.0045880779999999954
0.004395793000000037
"""