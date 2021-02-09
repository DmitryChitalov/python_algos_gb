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

from random import randint

my_list = [randint(-100, 100) for _ in range(100)]
print(my_list)


def find_min_hard(my_list): #O(n^2)
    for i in my_list:       #O(n)
        min_val = True      #O(1)
        for j in my_list:       #O(n)
            if i > j:           #O(n)
                min_val = False #0(1)
        if min_val:         #O(n)
            return i        #0(1)

def find_min(my_list):      #3n+2
    min_val = my_list[0]    #O(1)
    for i in my_list:       #O(n)
        if i < min_val:     #O(n)
            min_val = i     #O(n)
    return min_val          #O(1)

def find_min_easy(my_list):
    return min(my_list)

print(find_min_hard(my_list))
print(find_min(my_list))
print(find_min_easy(my_list))