"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
count = int(input("Введите количество элементов (n) ряда "))
calc = 1
res = 0


def my_func(count, calc, res):
    res = res + calc
    if count == 1:
        print("Сумма ряда равна " + str(res))
        exit()
    calc = calc / 2 * (-1)
    count -= 1
    my_func(count, calc, res)


my_func(count, calc, res)
