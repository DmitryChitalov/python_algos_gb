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
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def recursive_reverse1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse1(number // 10)}'


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print(timeit.timeit("recursive_reverse(123456)", setup="from __main__ import recursive_reverse"))
print(timeit.timeit("recursive_reverse1(123456)", setup="from __main__ import recursive_reverse1"))

'''Мемоизация — это подход, который позволяет нам сохранять результаты промежуточных решений, для того 
чтобы в следующих расчетах не повторять тоже самое.
Теперь повторный вызов функции с одинаковым значением не будет приводить к рекурсии.
Вместо этого результат будет возвращаться из словаря memory, в который записываются результаты предыдущих 
вычислений.(Материал из конспекта)
Данный подход улучшил время в ~17 раз
'''