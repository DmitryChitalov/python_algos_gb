"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_of_series(num=None, total=1.0, next_el=1.0, count_el=1):
    if num is None:
        num = int(input('Введите количество элементов: '))
    if num == 1:
        print(f'Количество элементов: {count_el}, ', end='')
        print('их сумма: ', end='')
        return total
    next_el = next_el / -2
    count_el += 1
    return sum_of_series((num - 1), total=total + next_el, next_el=next_el, count_el=count_el)


print(sum_of_series())
