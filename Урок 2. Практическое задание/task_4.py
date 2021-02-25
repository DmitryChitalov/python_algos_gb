"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""
def recur_sum(i, numb, n_count, total):
    """Рекурсия"""
    if i == n_count:
        print(f"Quantity of elems - {n_count}, elem sum - {total}")
    elif i < n_count:
        print(numb)
        return recur_sum(i + 1, numb / 2 * -1, n_count, total+numb)


try:
    N_QUANTITY = int(input("Input quantity of elements: "))
    recur_sum(0, 1, N_QUANTITY, 0)
except ValueError:
    print("Invalid input! Not number!")