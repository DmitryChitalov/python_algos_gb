"""Решение 1, линейная сложность"""


def get_key(company_income, value):
    
    for k, v in company_income.items():
        if v == value:
            return k


company_income = {"horns_and_hoofs": 10, "mcduck_inc": 100, "umbrella_corp": 50, "cyberdyne": 90, "acme": 20}
company_income_top = company_income
min_number = min(company_income_top.values())
company_income_top.pop(get_key(company_income_top, min_number))
min_number = min(company_income_top.values())
company_income_top.pop(get_key(company_income_top, min_number))
print(company_income_top.keys())

"""Решение 2, сложность линейная"""

company_income = {"horns_and_hoofs": 10, "mcduck_inc": 100, "umbrella_corp": 50, "cyberdyne": 90, "acme": 20}
top_3 = []
top_3_name = []
for company, income in company_income.items():
    top_3.append([income, company])
top_3.sort()
top_3 = top_3[-1:-4:-1]
for company in top_3:
    top_3_name.append(company[1])
print(top_3_name)

"""
Сложность программ одинаковая, но второй вариант более предпочтителен, так как при увеличении
требуемого количества вывода будет большее количество проходов по словарю. Во второй программе
сразу срезается нужное количество.
"""
