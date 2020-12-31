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

companies = {
    'Company 1': 500,
    'Company 2': 100,
    'Company 3': 20,
    'Company 4': 35,
    'Company 5': 16,
    'Company 6': 1000,
    'Company 7': 1200,
    'Company 8': 15,
    'Company 9': 1,
    'Company 10': -8
}


def search_1(dct): # The complexity is O(n^2)
    max_dict = list(dct.items())
    for i in range(0, len(max_dict) - 1):  # O(n)
        for j in range(i + 1, len(max_dict)):  # O(n)
            if max_dict[i][1] < max_dict[j][1]:  # O(1)
                buf = max_dict[i]
                max_dict[i] = max_dict[j]
                max_dict[j] = buf
    return max_dict[:3]


def search_2(dct):  # O(n * logN)
    max_dict = list(dct.items())
    max_dict.sort(key=lambda el: el[1]) # O(n * logN)
    return max_dict[-3:]


print(search_1(companies))
print(search_2(companies))

# Better to use the second option with O(N * logN) complexity
