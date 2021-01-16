"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

"""
import time

check_1 = time.time

# def search_min_lst_quad (lst_test_min_1): 
def search_min_lst_qud (ltmq): # ltmq = lst_test_min_quad
    for i in ltmq:
        var_min = True
        for j in ltmq:
            if i > j:
                var_min = False
        if var_min:
            return i
test_lst = [35,21,34,58,54,34] 
print(search_min_lst_qud(test_lst))
"""
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

def search_min_lst_line (ltml): # ltml == list_test_min_2
    elem_1 = ltml[0]
    for i in ltml:
        if i < elem_1:
            elem_1 = i
    return elem_1

test_lst_2 = [35,21,34,58,54,34] 
print (search_min_lst_line(test_lst_2))