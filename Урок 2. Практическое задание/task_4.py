"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def calc_row(dept, el=1):
    if dept > 1:
        dept -= 1
        el += calc_row(dept, el * (-0.5))

    return el


if __name__ == '__main__':
    print(calc_row(int(input('Введите кол. членов ряда: '))))
