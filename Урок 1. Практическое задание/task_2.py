"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
# Сложность: O(n^2) - квадаратичная сложность
def func_min_val(my_list):
    min_val = my_list[0]
    for el in my_list[1:len(my_list)]:
        if el < min_val:
            min_val = el
    return min_val

my_list = [1, 5, 6, 1, 2, 2, 3, 4, 7]
res = func_min_val(my_list)
print(res)

# Сложность: O(n) - линейная сложность
def func_min_2(my_list):
    return min(my_list)

my_list = [1, 0, 6, 1, 2, 2, -1, 4, 7]
res = func_min_2(my_list)
print(res)