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
#  отсортировать словарь по значениям и вывести первые три значения

dict_company = {'ARARA': 230210, 'DEKA': 180000, 'KIMBO': 275000,
                'PARMA': 273650, 'OLSO': 281890, 'MILLA': 310000}

# O(N^2)
def sorted_dict(arr):
    for i in range(len(arr)):
        lowest_num = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] > arr[lowest_num][1]:
                lowest_num = j
        arr[i], arr[lowest_num] = arr[lowest_num], arr[i]
    return arr[:3]


items_dictionary = list(dict_company.items())
for i in sorted_dict(items_dictionary):
    print(i)
#################################################

# что то не сразу допер, зациклился на функциях...
# O(N*logN)
list_from_dict = list(dict_company.items())
list_from_dict.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dict[i][0], ':', list_from_dict[i][1])


# доделал с помощью примера, изначально не работало как надо
# O(n)
def top_comp(arr):
    input_max = {}
    list_d = dict(arr)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda kv: kv[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max


print(top_comp(dict_company))





