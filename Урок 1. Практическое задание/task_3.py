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

############################################################
companies = [{"name": "Ambrella", "income": 12},
             {"name": "Karaduk", "income": 13},
             {"name": "Igor & Co", "income": 3},
             {"name": "Simon 23", "income": 55},
             {"name": "R232", "income": 4},
             ]

# 1 ###########################################################
"""
2: решение не возможно оценить в "нотации О-большое"
Вроде одна строка. Но сложность её составляющих не известна.
3: Удобно, так как одна строка. 
"""
print(f"Top companies: {sorted(companies, key=lambda k: k['income'], reverse=True)[0:3]}")

# 2 ###########################################################
"""
2: O(N log N)
3: Скорее всего быстрее предыдущего. Но не уверен
"""
top3 = []
for comp in companies:
    if len(top3) < 3:
        top3.append(comp)
    else:
        min_top_income = 0
        min_top_index = -1
        i = 0
        while i < len(top3):
            if comp.get("income") > top3[i].get("income") and comp.get("income") > min_top_income:
                min_top_income = top3[i].get("income")
                min_top_index = i
            i += 1
        if min_top_index >= 0:
            top3[min_top_index] = comp
print(f"Top companies: {top3}")
# 3 ##########################################################
while len(companies) > 3:
    min_top_income = float('inf')
    min_top_index = -1

    j = 0
    while j < len(companies):
        ddd = companies[j]
        this_company_income = companies[j].get('income')
        if min_top_income > this_company_income:
            min_top_income = this_company_income
            min_top_index = j
        j += 1

    companies.remove(companies[min_top_index])
print(f"Top companies: {companies}")
##########################################################
