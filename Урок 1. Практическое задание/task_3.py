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

company_info =  [("AT&T", 170756),
    ("Costco Wholesale", 141576),
    ("UnitedHealth Group", 226247),
    ("General Motors", 147049),
    ("Walgreens Boots Alliance", 131537),
    ("Mitsubishi", 145243),
    ("Alphabet", 136819),
    ("Honda Motor", 143302),
    ("Total", 184106),
    ("Glencore", 219754),
    ("CVS Health", 194579),
    ("Kroger", 121162),
    ("Lukoil", 119145),
    ("McKesson", 214319),
    ("Chevron", 166339),
    ("Samsung Electronics", 221579),
    ("AXA", 125578),
    ("Agricultural Bank of China", 139523),
    ("Amazon.com", 232887),
    ("China Construction Bank", 151110),
    ("Daimler", 197515),
    ("Hon Hai Precision Industry", 175617),
    ("Apple", 265595),
    ("China State Construction Engineering", 181524),
    ("Trafigura Group", 180774),
    ("Bank of China", 127714),
    ("EXOR Group", 175009),
    ("AmerisourceBergen", 167939),
    ("Ping An Insurance", 163597),
    ("Verizon Communications", 130863),
    ("Ford Motor", 160338),
    ("Industrial & Commercial Bank of China", 168979),
    ("Allianz", 126799),
    ("General Electric", 120268),
    ("Berkshire Hathaway", 247837),
    ("Gazprom", 131302),
    ("JPMorgan Chase & Co.", 131412),
    ("SAIC Motor", 136392),
    ("Cardinal Health", 136809),
    ("Fannie Mae", 120101)]


#
# for item in company_info:
#     print(f"{item} - {company_info[item]}")

# Сложность: O(N).
def solution1(lst):
    max_vals = [("", 0)] * 3
    for item in lst:                        # O(N)
        for j in range(len(max_vals)):      # O(3)
            if item[1] > max_vals[j][1]:    # O(1) + O(1) + O(1)
                max_vals.insert(j, item)    # O(3)
                max_vals.pop()              # O(1)
                break
    return max_vals


# Сложность: O(NlogN)
def solution2(lst):
    lst_copy = list(lst)                                    # O(N)
    lst_copy.sort(key=lambda tup: tup[1], reverse=True)     # O(NlogN)
    return lst_copy[:3]


print(solution1(company_info))
print(solution2(company_info))


# В первом решении с каждым элементом происходит 3 сравнения, то есть по факту сложность O(3N)
# Во втором решении за счет сортировки сложность получилась O(NlogN)
# Считаю, что второе решение эффективнее, если количество элементов в списке меньше 1000. В районе 1000 элементов
# оба алгоритма работают приблизительно одинаково, log1000 = 3. В списках, с количеством элементов больше 1000 первый
# алгоритм начинает работать эффективнее