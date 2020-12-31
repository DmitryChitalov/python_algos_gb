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


def memorize(func):
    def memo(n, memory={}):
        rec = memory.get(n)
        if rec is None:
            rec = func(n)
            memory[n] = rec
        return memory[n]
    return memo


@memorize
def recursive_reverse1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


number = int(input("Введите число "))
print(recursive_reverse1(number))
# В комментариях время исполнения:
print(timeit.timeit("recursive_reverse(number)", setup="from __main__ import recursive_reverse, number"))       # 2.27
print(timeit.timeit("recursive_reverse1(number)", setup="from __main__ import recursive_reverse1, number"))     # 0.23


""" Замеры времени показывают: Использование 'мемоизации' сокращает время исполнения программы
Результаты работы рекурсивной функции сохраняются в хэш-таблице
обработка данных в таблице происходит быстрее работы рекурсии """