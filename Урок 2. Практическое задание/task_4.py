"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def get_sum_range(num_range, first_num=1, sum_row=0, count_item_row=0):
    count_item_row += 1
    sum_row += first_num
    first_num /= -2
    if num_range == 1:
        print(f'Количество элементов: {count_item_row}, а их сумма: {sum_row}')
        return
    else:
        get_sum_range(num_range - 1, first_num, sum_row, count_item_row)


if __name__ == '__main__':
    num = int(input('Введите количество элементов: '))
    get_sum_range(num)
