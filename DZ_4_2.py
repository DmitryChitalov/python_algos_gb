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
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(1000, 100000)
num_1000 = randint(100000, 1000000)
num_10000 = randint(10000000, 1000000000000)

elapsed_not_opt100 = (timeit.timeit("recursive_reverse(num_100)",
                                    setup="from __main__ import recursive_reverse, num_100",
                                    number=10000)) * 100
elapsed_not_opt1000 = (timeit.timeit("recursive_reverse(num_1000)",
                                     setup="from __main__ import recursive_reverse, num_1000",
                                     number=10000)) * 100
elapsed_not_opt10000 = (timeit.timeit("recursive_reverse(num_10000)",
                                      setup="from __main__ import recursive_reverse, num_10000",
                                      number=10000)) * 100
print(f"Не оптимизированная функция recursive_reverse - {elapsed_not_opt100}\n"
      f"{elapsed_not_opt1000}\n"
      f"{elapsed_not_opt10000}")


def memoize(f):
    cache = {}
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]


@memoize
def recursive_reverse_opt(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


elapsed_opt100 = (timeit.timeit("recursive_reverse_opt(num_100)",
                                setup="from __main__ import recursive_reverse_opt, num_100",
                                number=10000)) * 100
elapsed_opt1000 = (timeit.timeit("recursive_reverse_opt(num_1000)",
                                 setup="from __main__ import recursive_reverse_opt, num_1000",
                                 number=10000)) * 100
elapsed_opt10000 = (timeit.timeit("recursive_reverse_opt(num_10000)",
                                  setup="from __main__ import recursive_reverse_opt, num_10000",
                                  number=10000)) * 100
print(f"Оптимизированная функция recursive_reverse - {elapsed_opt100}\n"
      f"{elapsed_opt1000}\n"
      f"{elapsed_opt10000}")

# ----------------------------ВЫВОДЫ------------------------------------
# Смысл в том что не оптимизированный код выполняет ту же самую операцию
# которую он проводил с меньшими числами, а метод мемоизации сохраняет и
# повторно использует ранние вычисленные значения!
