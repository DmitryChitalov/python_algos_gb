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
import random
l = [random.randint(0, 100) for i in range(10)]
print(l)

# O(n^2)
def first_algorithm(my_lst : list):
    min = my_lst[0]
    for i in range (len(my_lst)):
        for j in range(len(my_lst)):
            if (my_lst[i] < my_lst[j]) and (my_lst[i] <= min):
                min = my_lst[i]
                break
    return min
print("First algorithm(O(n^2)): ", first_algorithm(l))

#O(n)
def second_algorithm(my_lst : list):
    min = my_lst[0]
    for i in range (len(my_lst)):
        if (my_lst[i] < min):
            min = my_lst[i]
    return min
print("Second algorithm(O(n)): ",second_algorithm(l))