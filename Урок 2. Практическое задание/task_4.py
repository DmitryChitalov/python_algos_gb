"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def elem_sum(fin_number, cur_number=2, div=2, sum=0):
    try:
        fin_number = int(fin_number)
        if cur_number > fin_number:
            return sum + 1
        else:
            if cur_number % 2 == 0:
                sum -= 1 / div
                return elem_sum(fin_number, cur_number + 1, div * 2, sum)
            else:
                sum += 1 / div
                return elem_sum(fin_number, cur_number + 1, div * 2, sum)
    except ValueError:
        return elem_sum(input("Пожалуйста введите целое положительное число!: "))


print(elem_sum(input("Пожалуйста введите целое положительное число: ")))
