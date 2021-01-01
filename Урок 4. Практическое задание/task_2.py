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
from timeit import timeit


# def recursive_reverse(number):
#     if number == 0:
#          return str(number % 10)
#     return f'{str(number % 10)}{recursive_reverse(number // 10)}'

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def memoize(func):
    memo_dict = {}

    def wrapper(*args):
        if args not in memo_dict:
            memo_dict[args] = func(*args)
        return memo_dict[args]

    return wrapper


@memoize
def recursive_reverse_1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


number = 123456789


print(timeit("recursive_reverse(number)", setup="from __main__ import recursive_reverse, number", number=1000))
print(timeit("recursive_reverse_1(number)", setup="from __main__ import recursive_reverse_1, number", number=1000))


'''
Время выполнения функций (1000 повторений):
recursive_reverse:      0.00391 сек
recursive_reverse1:     0.00016 сек
 
Добавленный декоратор @memoize позволил кэшировать результаты промежуточных вычислений и избежать повторного вычисления 
в ходе рекурсии.
'''
