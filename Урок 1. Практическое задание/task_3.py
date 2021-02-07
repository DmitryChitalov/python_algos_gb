"""
Задание 3.
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


company = {
    "best_restaurant": 20000,
    "worst_cafe": 500,
    "worst_restaurant": 3000,
    "best_lounge_bar": 1000,
    "worst_lounge_bar": 5000,
    "best_cafe": 15000,
    "best_night_club": 112000,
    "worst_night_club": 16000
}

# Вариант 1


def search_three_max(lst):
    list_to_dict = dict(lst)
    list_of_max = {}
    for i in range(3):
        max_val = max(list_to_dict.items(), key=lambda key_value: key_value[1])
        del list_to_dict[max_val[0]]
        list_of_max[max_val[0]] = max_val[1]
    return list_of_max

# Общая сложность алгоритма O(N)


print(search_three_max(company))


# Вариант 2
# Общая сложность алгоритма O(NlogN)


dict_to_list = list(company.items())
dict_to_list.sort(key=lambda key_value: key_value[1], reverse=True)
for i in range(3):
    print(dict_to_list[i][0], ':', dict_to_list[i][1])

# 1 Вариант решения оптимальнее, так как общая сложность алгоритма меньше, соответственно быстродействие выше.
# 2 Вариант решения мне кажется лаконичнее, но изменяется иходный список, что есть не очень хорошо.
