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

company_dict = {
    'Apple': 48745498,
    'Samsung': 45484546,
    'Xiaomi': 1574854,
    'Bosh': 1596845,
    'LG': 4578456,
    'Intel': 10578921,
}
# Решение №1
# Сложность решения: O(n)
max_profit = []
max_num = 0
max_num_2 = 0
max_num_3 = 0
for k, v in company_dict.items():
    if max_num <= v:
        max_num = v
max_profit.append(max_num)
for k, v in company_dict.items():
    if v == max_num:
        continue
    elif max_num_2 <= v:
        max_num_2 = v
max_profit.append(max_num_2)
for k, v in company_dict.items():
    if v == max_num:
        continue
    if v == max_num_2:
        continue
    elif max_num_3 <= v:
        max_num_3 = v
max_profit.append(max_num_3)
for k, v in company_dict.items():
    if v in max_profit:
        print(k)
print()
# Решение №2
# Сложность решения: O(nlogn)
profit_list = []
for v in company_dict.values():
    profit_list.append(v)
profit_list.sort(reverse=True)
for k in company_dict.keys():
    if company_dict[k] in profit_list[:3]:
        print(k)
print()
# Решение №3
# Сложность решения: O(n**2)
while len(company_dict) > 3:
    for k, v in company_dict.items():
        if v == min(company_dict.values()):
            company_dict.pop(k)
            break
for k in company_dict.keys():
    print(k)

"""
Вывод: решение №1 эфективнее, так его сложность O(n), нет вложеных циклов
В решении №2 используется сортировка списка sort(), что делает его сложность O(nlogn)
В решении №3 тоже импользуется вложеный цикл в цикле, но он еще и изменяет словарь, сложность O(n**2)
"""
