"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_series_numbers(number_in_row, counter=0, number=1.0, sum_of_numbers=0.0):
    if counter == number_in_row:
        return f'Количество элементов = {number_in_row}, их сумма = {sum_of_numbers}'
    elif counter < number_in_row:
        return sum_series_numbers(number_in_row, counter + 1, number / 2 * -1, sum_of_numbers + number)
    else:
        print('Что-то пошло не так')


if __name__ == '__main__':
    print(sum_series_numbers(int(input('Введите количество элементов: '))))
