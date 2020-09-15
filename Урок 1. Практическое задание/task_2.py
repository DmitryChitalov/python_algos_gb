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

mylist = [[random.randint(0, 20) for _ in range(10)],
          [random.randint(0, 30) for _ in range(10)],[random.randint(0, 30) for _ in range(10)]]
# mylist1 = [random.randint(0, 100) for _ in range(10) ]
# mylist.append(mylist1)
print(mylist)


def search_min(args):
    """
    :param args:
    :return:
    O(n**2)
    """
    mymin = args[0][0]  # 1
    for i in range(len(args)):  # n
        for j in range(len(args[0])):  # n
            if args[i][j] <= mymin:  # 1
                mymin = args[i][j]  # 1
    return mymin


print(search_min(mylist))


def search_min2(args):
    """
            :param args:
        :return:
        O(n)
        """
    args = sum(args, [])  # n
    return min(args)  # n



print(search_min2(mylist))
