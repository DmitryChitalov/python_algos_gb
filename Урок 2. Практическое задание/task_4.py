"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def arr_avg(in_index, in_val):
    v_sum = 0
    if in_index > 0:
        v_sum = in_val + arr_avg((in_index-1), (-1)*in_val/2)
    return v_sum


if __name__ == '__main__':
    print('Enter number of values:')
    v_num = input()
    v_sum = arr_avg(int(v_num), 1)
    print('Average value: ' + str(v_sum))
