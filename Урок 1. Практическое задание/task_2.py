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

#lst = [randint(1,100) for i in range(10)];
#print(lst);
#1
def search_min():
    lst = [randint(1, 100) for i in range(10)];
    print(lst)
    min_num = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
    return min_num;

print(search_min());

#2
def search_mini():
    lst = [randint(1, 100) for i in range(10)];
    print(lst)
    return min(lst);
print(search_mini());
