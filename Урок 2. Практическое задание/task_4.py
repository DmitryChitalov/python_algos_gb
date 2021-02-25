"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_rec(current_element_value, total_elements_count, result_sum: int = 0, current_element_index: int = 0):
    if current_element_index == total_elements_count:
        return result_sum
    elif current_element_index < total_elements_count:
        return sum_rec(-current_element_value/2, total_elements_count,
                             result_sum + current_element_value, current_element_index + 1)


while True:
    try:
        elements_count = int(input("Введите количество элементов > "))
        elements_sum = sum_rec(1, elements_count)
        print(f"Сумма: {elements_sum}")
    except ValueError:
        print("Число не является целым.")
        continue
    break