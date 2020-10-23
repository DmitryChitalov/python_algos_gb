"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


# 1-й вариант: O(n log n) - линейно-логарифмическая
def max_profit1(dict_obj):
    lst = list(dict_obj.items())   # O(len(dict_obj))
    lst.sort(key=lambda i: i[1])  # O(n log n)
    return lst[2:]


# 2-й вариант: O(n^2) - квадратичная
def max_profit2(dict_obj):
    lst = list(dict_obj.items())  # O(len(dict_obj))
    swapped = True
    while swapped:  # O(n)
        swapped = False
        for i in range(len(lst) - 1):  # O(n)
            if lst[i][1] > lst[i + 1][1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
    return lst[2:]


# 3-й вариант: (n^4)
def max_profit3(dict_obj):
    lst_final = []
    lst = list(dict_obj.values())  # O(len(dict_obj))
    for x in range(3):  # O(n)
        temp = max(lst)   # O(n)
        res = [key for key in dict_obj if dict_obj[key] == temp]  # O(n)
        lst_final.append((res[0], temp))  # O(1)
        lst.remove(temp)  # O(n)
    return lst_final


dict_value = {'Company1': 100000, 'Company2': 150000, 'Company3': 170000, 'Company4': 80000, 'Company5': 90000}
print(max_profit1(dict_value))
print(max_profit2(dict_value))
print(max_profit3(dict_value))

""" 1-й вариант лучше - O(n log n) - линейно-логарифмическая сложность алгоритма, так как при увеличении размера
 входных данных будет выполнено меньше всего операций по сравнению с другими алгоритмами. 
"""