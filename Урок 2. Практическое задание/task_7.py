"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def equation(number, left_side = 5, right_side = 6):
    if left_side == right_side:
        print(f'Выполнено равенство: {left_side == right_side}')
    elif left_side < right_side:
        return equation(number, left_side + 1, number * (number + 1) / 2)

try:
    entered_number = int(input('Введите число: '))
    equation(entered_number)
except ValueError:
    print('Введите число')