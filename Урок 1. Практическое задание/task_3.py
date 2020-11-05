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
data_base = { 'aeroflot': 2000000, 's7': 1500000, 'ural_airlines': 1000000, 'nord_wind': 1000000,
              'rossiya': 1350000, 'pobeda': 1750000, 'azur_air': 800000}

#Сложность 1 вариант: линейно-логарифмическая

profit_list = list(data_base.values())
profit_list.sort(reverse=True)
top_list = profit_list[:3]
top3 = {}

for key, value in data_base.items():
    if value in top_list:
        top3[key] = value

print(top3) #тк словарь неупорядочен, выводятся 3 компании с наибольшей прибылью в случайном порядке

# Сложность 2 вариант: линейно-логарифмическая (линейная?)
import operator

top3 = sorted(data_base.items(), key=operator.itemgetter(1), reverse=True)[:3]
print(top3)

"""тк в этом варианте сортировка идет не по типу list, а по типу dict_items, а все стандартные операции
со словарями имеют более высокую производительность, нежели чем со списками, то могу предположить, что
сложность этого решения может быть и линейная ( этот вариант в таблицах не описан). В любом случае,
второй вариант решения предпочтительнее, тк используются встроенные модули , нет необходимости создавать
промежуточные структуры , как в варианте 1. Читаемость кода выше, объем меньше, результат упорядочен."""



