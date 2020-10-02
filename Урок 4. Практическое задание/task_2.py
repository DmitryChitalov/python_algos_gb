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

"""Функция recursive_reverse с рекурсией выполняется дольше всего 
(время выполнения: 0.653700745) """

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

"""Функция rev выполняется быстрее, чем recursive_reverse
потому что нет рекурсии и применяются встроенные функции и срез 
(время выполнения: 0.10090892600000001)"""

def rev(number):
    n = str(number)
    r = n[::-1]
    a = int(r)
    return a

"""Из-за применения мемоизации уменьшается время выполнения 
функция new_rec_reverse по сравнению с recursive_reverse 
(время выполнения: 0.02515015899999995) """

def memo_rev(func):
    mem = {}
    def wrapper(num):
        if num not in mem:
            mem[num] = func(num)
        return mem[num]
    return wrapper

@memo_rev
def new_rec_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{new_rec_reverse(number // 10)}'

print(timeit.timeit("recursive_reverse(123456789)", setup="from __main__ import recursive_reverse", number = 100000))
print(timeit.timeit("rev(123456789)", setup="from __main__ import rev", number = 100000))
print(timeit.timeit("new_rec_reverse(123456789)", setup="from __main__ import new_rec_reverse", number = 100000))


