"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75"""


def recurs(count, numb, input, summ):
    if count == input:
        print(f"Количество элементов - {input}\n"
              f"Их сумма - {summ}")
    if count < input:
        recurs(count + 1, numb / - 2, input, summ + numb)


user_input = input("Введите количество элементов ")
while not user_input.isdigit():
    user_input = input("Нужно ввести число! Введите количество элементов ")

recurs(0, 1, int(user_input), 0)
