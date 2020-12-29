"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memo(f):
    dct = {}

    def decorate(num):
        if num in dct.keys():
            return dct[num]
        else:
            dct[num] = f(num)
            return dct[num]
    return decorate


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)} {recursive_reverse(number // 10)}'


@memo
def recursive_reverse_2(number):
    if number == 0:
        return ''  # убираем нулевой индекс
    return f'{str(number % 10)} {recursive_reverse_2(number // 10)}'


print(recursive_reverse(12345))
print(recursive_reverse_2(12345))

num = 10000

print(
    timeit.timeit(
        "recursive_reverse(num)",
        setup='from __main__ import recursive_reverse, num',
        number=10000))  # 0.0251143

print(
    timeit.timeit(
        'recursive_reverse_2(num)',
        setup='from __main__ import recursive_reverse_2, num',
        number=10000))  # 0.0019417000000000045

"""
Мемоизация ускоряет код в 10 раз.
"""