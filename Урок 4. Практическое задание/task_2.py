"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.

Ответ: Непосредственно эта функция в мемоизации не нуждается при однократном ее приминении, т.к. все значения,
которые попадают в кэш при ее вычислении будут разными и обращения к кэшу для получения значени произведено не будет
(к примеру для чила 111111 кэш будет выглядеть так: {0: '', 1: '1', 11: '11', 111: '111', 1111: '1111',
11111: '11111', 111111: '111111'}, ни одно из значений не повторяется и не будет повторяться ни при каком переданном
аргументе, если функция запущенна в первый раз). Но если учесть тот факт, что функции могут использоваться за один
жизненный цикл программы неоднократно, то в мемоизации подобных функций (в которых при первом запуске нет обращения к
кэшу) есть смысл (кэш будет сохранен до конца работы программы, при этом пополняясь в случае запуска функции с
другими аргументами); тем более, что при использовании декоратора lru_cache заметной потери в производительности при
первом вызове функции не наблюдается (в отличии от той, что дана в примере). """

from timeit import timeit
from random import randint
from functools import lru_cache


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


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


@lru_cache
def recursive_reverse_lru(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


if __name__ == '__main__':
    num_100 = randint(10000, 1000000)
    num_1000 = randint(1000000, 10000000)
    num_10000 = randint(100000000, 10000000000000)

    print('Не оптимизированная функция recursive_reverse')
    print(timeit("recursive_reverse(num_100)", number=10000, globals=globals()))
    print(timeit("recursive_reverse(num_1000)", number=10000, globals=globals()))
    print(timeit("recursive_reverse(num_10000)", number=10000, globals=globals()))

    print('Оптимизированная функция recursive_reverse_mem')
    print(timeit('recursive_reverse_mem(num_100)', number=10000, globals=globals()))
    print(timeit('recursive_reverse_mem(num_1000)', number=10000, globals=globals()))
    print(timeit('recursive_reverse_mem(num_10000)', number=10000, globals=globals()))

    print('Оптимизированная функция recursive_reverse_lru')
    print(timeit('recursive_reverse_lru(num_100)', number=10000, globals=globals()))
    print(timeit('recursive_reverse_lru(num_1000)', number=10000, globals=globals()))
    print(timeit('recursive_reverse_lru(num_10000)', number=10000, globals=globals()))
