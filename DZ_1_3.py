"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
from random import randint
from collections import Counter

rand = []
while len(rand) < 10:
    rand.append(randint(50000, 1000000))
comp_name = ['Yandex', 'Mail', 'Google', 'Amazon', 'VAZ',
             'VK', 'Facebook', 'Instagram', 'SpaceX', 'Tesla']
comp_dict = {}
i = 0
while i < len(rand):
    comp_dict[comp_name[i]] = rand[i]
    i += 1
print(comp_dict)

# Первый вариант с помощью sorted
print(sorted(comp_dict, key=comp_dict.get, reverse=True)[:3])
# Сложность O(n log n)

# Второй вариант с помощью most_common
print(dict(Counter(comp_dict).most_common(3)))
# Сложность O(n log n)

# Третий вариант с циклом


def max3(comp_input):
    max_comp = []
    a = dict(comp_input)
    el = 0
    while el < 3:
        maximum = max(a, key=a.get)     # max - O(n)
        max_comp.append(maximum)        # append - O(1)
        a.pop(maximum)                  # pop - O(1)
        el += 1
    return max_comp


print(max3(comp_dict))
# Сложность O(n)


"Третий вариант лучший, и не изменяет словарь, а сортировка как мы видим усложняет процесс"

print(Counter(comp_dict))