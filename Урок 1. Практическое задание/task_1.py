"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции
2) определите сложность алгоритма в целом

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'

Примечание:
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random


#############################################################################################
def check_1(lst_obj):  # итоговая сложность: линейная (n)
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: !!!.
    """
    lst_to_set = set(lst_obj)  # сложность: линейная (n)
    return lst_to_set  # сложность: константная (1)


#############################################################################################
def check_2(lst_obj):  # итоговая сложность: квадратичная (n^2)
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: !!!.
    """
    for j in range(len(lst_obj)):          # сложность: линейная (n)
        if lst_obj[j] in lst_obj[j+1:]:    # сложность: линейная (n)
            return False                   # сложность: константная (1)
    return True                            # сложность: константная (1)


#############################################################################################
def check_3(lst_obj):  # итоговая сложность: линейно-логарифмическая (n log(n))
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: !!!
    """
    lst_copy = list(lst_obj)                 # сложность: линейная (n)
    lst_copy.sort()                          # сложность: линейно-логарифмическая (n log(n))
    for i in range(len(lst_obj) - 1):        # сложность: линейная (n)
        if lst_copy[i] == lst_copy[i+1]:     # сложность: константная (1)
            return False                     # сложность: константная (1)
    return True                              # сложность: константная (1)

#############################################################################################


for j in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
