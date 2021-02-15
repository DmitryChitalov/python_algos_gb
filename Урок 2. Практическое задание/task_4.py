"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_of_progression(iterations, multiplicator, currect_number):
    if iterations == 1:
        return currect_number
    else:
        return currect_number + sum_of_progression(iterations - 1, multiplicator, currect_number * multiplicator)


iterations = input("Введите количество элементов: ")
if not iterations.isdigit():
    print("Вы ввели не число!")
    exit()
print(sum_of_progression(int(iterations), -0.5, 1))
