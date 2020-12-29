"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через меморизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь меморизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
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


def memorize(f):
    cache = {}

    def decorate(num):

        if num in cache.keys():
            return cache[num]
        else:
            cache[num] = f(num)
            return cache[num]
    return decorate


@memorize
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

# При вызове функций для одного числа, вариант без меморизации выполняется
# быстрее, так как не тратит время на составление хэш таблицы
# При многократном вызове функции (для одного и того же число),
# вариант с меморизацией выполняется быстрее
# Нет необходимости применять меморизацию в данном случае
print('Выполнение функции для одного числа, один раз, время умножено на 1000 '
      'для наглядности результата')
print('Без оптимизации')
print(
    timeit(
        'recursive_reverse(123456789987654321)',
        setup='from __main__ import recursive_reverse, num_100',
        number=1) * 1000)
print('С оптимизацией')
print(
    timeit(
        'recursive_reverse_mem(123456789987654321)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=1) * 1000)
# В связи с чем у меня возник вопрос - каким образом timeit для повторного
# вычисления значений, не составляет кэш заново, а берет данные из прошлого
# кэша? После вызова функции, кэш не удаляется? Почему за 10 000 вызовов
# формируется только один кэш?