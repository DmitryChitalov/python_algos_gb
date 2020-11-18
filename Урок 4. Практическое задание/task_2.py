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
from functools import lru_cache

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

elem = [100, 1000, 10000]


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


@lru_cache()
def recursive_reverse_mem_1(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

def slice_optimized(number):
    '''
    Новая написаная функция
    '''
    foo = number
    foo = int(str(foo)[::-1])
    return foo


def test(name):
    for foo in elem:
        print(
            timeit(
                f"{name}(num_{foo})",
                setup=f'from __main__ import {name}, num_{foo}',
                number=10000))


print('__Не оптимизированная функция recursive_reverse')
test("recursive_reverse")

print('__Оптимизированная функция recursive_reverse_mem')
test("recursive_reverse_mem")

print("*"*100)

print('__Оптимизированная функция срезом slice_optimized')
test("slice_optimized")

print('__Оптимизированная функция recursive_reverse_mem_1')
test("recursive_reverse_mem_1")

print(num_100)
print(num_1000)
print(num_10000)
print(recursive_reverse(num_100))
print(recursive_reverse(num_1000))
print(recursive_reverse(num_10000))
print(type(recursive_reverse(num_10000)))
print("*"*100)
print(slice_optimized(num_10000))
"""
Немного переделал код, а то простыня получается (функционал тот-же)
В задании сказано что на выходе мы должны получить число. В предложенном коде мы получаем str и добавляется 0 в конце
перевернутого "числа". Понятно что можно потом int(), но все же. Решение мягко говоря не оч.
Число из num_100 -          429136
Число из num_1000 -         2406917
Число из num_10000 -        1660672359605
Перевернутое из num_100 -   6319240
Перевернутое из num_1000 -  71960420
Перевернутое из num_10000 - 50695327606610
<class 'str'>

По поводу собственной оптимизации - тут конечно приходит на ум срез, преобразовать в строку развернуть и обратно 
преобразовать в число. Просто и практично. 

Когда читал про меморизацию наткнулся на статью на Хабре про декоратор lru_cache(Least Recently Used) декоратор который 
уже написан за нас. Тем более он оказался быстрее в работе (recursive_reverse_mem_1)

С декораторами рекурсии конечно же работают быстрее потому что мы сохраненяем и повторно использкем ранние вычисленные 
значения, а не считаем их заново.

Результаты работы - 
__Не оптимизированная функция recursive_reverse
0.048850199999999996
0.0597342
0.1113342

__Оптимизированная функция recursive_reverse_mem
0.0033229999999999926
0.0033559000000000228
0.003228199999999959
****************************************************************************************************
__Оптимизированная функция срезом slice_optimized
0.0096754
0.009829000000000032
0.011030600000000002

__Оптимизированная функция recursive_reverse_mem_1
0.001235900000000012
0.0012336000000000014
0.001299799999999962
"""