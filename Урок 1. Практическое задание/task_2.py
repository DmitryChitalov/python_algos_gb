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
a = []
i = 0
while i < 5:
    j=round(random.random()*100)
    a.append(j)
    i+=1
print(a)



def minimum(lst_obj):
    lst_symbols = list(lst_obj)
    result = lst_symbols[0]
    for i in range(len(lst_symbols)):
        for j in range(len(lst_symbols)):
            if lst_symbols[j] < lst_symbols[i] and lst_symbols[j]<result:
                result = lst_symbols[j]
    return result     

def minimum2(lst_obj):
    lst_symbols = list(lst_obj)
    result = lst_symbols[0]
    for i in range(len(lst_symbols)):
        if lst_symbols[i] < result:
            result = lst_symbols[i]
    return result
print(minimum(a))
print(minimum2(a))