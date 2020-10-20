"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def rec_elements_sum(i: int, num: float, n_counter: int, count_sum: float) -> float:
    if i == n_counter:
        print(f'Количество элементов {n_counter}, их сумма = {count_sum}')
    elif i < n_counter:
        return rec_elements_sum(i + 1, num / 2 * -1, n_counter, count_sum + num)


num = int(input('Ведите число к которому будет применина следующия формула(n/2 * -1):'))
elements_counter = int(input('Ведите количество повторений:'))
rec_elements_sum(0, num, elements_counter, 0)
