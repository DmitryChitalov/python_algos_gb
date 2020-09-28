"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_elements(n, element=1, elem_count=0, result=0):
    if n == elem_count:
        return print(f'Количество элементов - {elem_count}, их сумма - {result}')
    else:
        result += element
        element *= -0.5
        elem_count += 1
        return sum_elements(n, element, elem_count, result)


try:
    sum_elements(int(input('Введите количество элементов: ')))
except ValueError:
    print('Введено некорректное значение, завершение программы')
