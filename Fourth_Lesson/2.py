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
from random import randint

def recursive_reverse(number):
    if number == 0:
        return ''  #str(number % 10)  Закомментированный мной кусок кода добавлял к конечному числу лишний 0 в конец
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

numb =  randint(9999999, 99999999)

# Без применения мемоизации
print(timeit("recursive_reverse(numb)",setup= "from __main__ import recursive_reverse, numb",number=10000))

def memorize(func):
    cache = {}
    def wrapper(num):
        if cache.get(num):
           return cache[num]
        else:
            cache[num]=func(num)
            return cache[num]
    return wrapper

@memorize
def recursive_reverse_after(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

# С применением мемоизации
print(timeit("recursive_reverse_after(numb)",setup= "from __main__ import recursive_reverse_after, numb",number=10000))

"""
В отимизированной функции recursive_reverse_after мемоизация имеет значение, 
т. к при достаточно больом количестве замеров мемоизация приносит заметный выйгрыш в скорости.
 Мемоизация полезна здесь, так как для 10000 вызовов функции с одним и тем же входным аргументом,
значение функции не рассчитывается рекурсивно, а берётся из хеш-таблицы, благодаря чему мы получаем выйгрыш в скорости
"""