"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def sum_numbers(i, number, counting, numbers_sum):

    if i == counting:
        print(f"Количество элементов - {counting}, их сумма - {numbers_sum}")
    elif i < counting:
        return sum_numbers(i + 1, number / 2 * -1, counting, numbers_sum+number)


try:
    result_counting = int(input("Введите количество элементов: "))
    sum_numbers(0, 1, result_counting, 0)
except ValueError:
    print("Вместо числа вы ввели строку")
