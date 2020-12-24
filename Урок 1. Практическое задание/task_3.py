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
    'netflix': 100000000000,
    'marussia': 500000333,
    'yandex': 90000000000,
    'gazmyas': 30907080,
    'IP Ivanova': 239839030093
}

# Вар 1
listed_companies = list(companies.items())
# print(listed_companies)
listed_companies.sort(key=lambda i: i[1], reverse=True)
# print(listed_companies)
print(f'Самая крутая компания {listed_companies[0]}\n'
      f'Вторая по крутости {listed_companies[1]}\n'
      f'Так себе компания {listed_companies[2]}')
# Сложность O(n*logn)

# Вар 2

listed_companies = list(companies.items())
print(listed_companies)
for i in range(len(listed_companies)):
    low = i
    for z in range(i+1, len(listed_companies)):
        if listed_companies[z][1] > listed_companies[low][1]:
            low = z
    listed_companies[i], listed_companies[low] = listed_companies[low], listed_companies[i]
print(f'Самая крутая компания {listed_companies[0]}\n'
       f'Вторая по крутости {listed_companies[1]}\n'
       f'Так себе компания {listed_companies[2]}')

# Сложность O(n**2)

# Вариант 1 является более удачным, поскольку имеет меньшую сложность