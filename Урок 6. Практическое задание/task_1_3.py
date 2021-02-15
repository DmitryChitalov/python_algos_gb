# Python 3.8.0 win 64x
# Lesson_4 Task_2 (реверс числа)

from timeit import timeit
import memory_profiler

num = 634214497715963421449771596342144977159634214497715963421449771596342144977159


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


# print('Не оптимизированная функция recursive_reverse')  # 0.453
# print(timeit("recursive_reverse(num)", setup='from __main__ import recursive_reverse, num', number=10000))
# print('Оптимизированная функция recursive_reverse_mem')  # 0.002
# print(timeit('recursive_reverse_mem(num)', setup='from __main__ import recursive_reverse_mem, num', number=10000))

# т.к. у рекурсивной функции есть ограничения на кол-во реркусий
# попробуем решить задачу всеми представленными способами и найти наиболее оптимальное решение

# для расчетов затраченной памяти будем использовать декоратор
def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        return res, m2[0] - m1[0]

    return wrapper


@decor
def reverse_1(number):
    reverse = 0
    while number > 0:
        reminder = number % 10
        reverse = (reverse * 10) + reminder
        number = number // 10
    return reverse


big_num = 634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159634214497715963421449771596342144977159
print('\nreverse_1:')
print(reverse_1(big_num)[1])  # 21516


@decor
def reverse_2(number):
    return int(str(number)[::-1])


print('\nreverse_2:')
print(reverse_2(big_num)[1])  # 21516

# # 1. Ленивые вычисления (yield)
#
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         m1 = memory_profiler.memory_usage()
#         res = func(args[0])
#         m2 = memory_profiler.memory_usage()
#         return res, m2[0] - m1[0]
#
#     return wrapper
#
#
# @decor
# def reverse_number_1(number):
#     def new_num(number):
#         yield number % 10
#
#     reverse = []
#     for _ in range(number):
#         reverse.append(new_num(number))
#         number = number // 10
#     return reverse
#
#
# print(reverse_number_1(123456789))
#
#
# # 3. Использовать NumPy
# @decor
# def reverse_number_1(number):
#     def new_num(number):
#         yield number % 10
#
#     reverse = []
#     for _ in range(number):
#         reverse.append(new_num(number))
#         number = number // 10
#     return reverse
#
