"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def summer(count, number=1, old_number=-2.0):
    now_number = -(old_number / 2.0)
    if number == count:
        return now_number
    return now_number + summer(count, number + 1, now_number)


while True:
    data = input('Введите количество элементов: ')
    if data.isdigit():
        break
    else:
        print('Введите число!!!')

print(f'Количество элементов: {data}, их сумма: {summer(int(data))}')
