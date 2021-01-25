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
import copy

def generate_list(n):
    res = [i for i in range(0, n)]
    random.shuffle(res)
    return res

# Алгоритм № 1 со сложностью O(n^2).
def find_min_1(i_lst):
    if not i_lst:
        return

    buf_lst = copy.copy(i_lst)

    for i in range(0, len(buf_lst)):
        for j in range(i+1, len(buf_lst)):
            if buf_lst[i] > buf_lst[j]:
                l_buf      = buf_lst[i]
                buf_lst[i] = buf_lst[j]
                buf_lst[j] = l_buf
    return buf_lst[0]

# Алгоритм № 2 со сложностью O(n).
def find_min_2(i_lst):
    if not i_lst:
        return

    l_min_val = i_lst[0]

    for rec_lst in i_lst:
        if rec_lst < l_min_val:
            l_min_val = rec_lst
    return l_min_val

g_lst = generate_list(5)
print(g_lst)

print(find_min_1(g_lst))
print(find_min_2(g_lst))

print(g_lst)
