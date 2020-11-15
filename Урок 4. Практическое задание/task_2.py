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

from timeit import Timer

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

# рекурсия имеет самую большую сложность, я предложил в своем решении константную сложность,
# т.к. она имеет наибольшую скорость работы

def revolution(number):
    number = str(number)
    new_number = number[::-1]
    return new_number

t1 = Timer("recursive_reverse(987654)", "from __main__ import recursive_reverse")
print("recursion ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("revolution(987654)", "from __main__ import revolution")
print("revolution ", t2.timeit(number=1000), "milliseconds")


