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

my_list1 = [
    {"name": "abc", "profit": 12500},
    {"name": "abb", "profit": 500},
    {"name": "bbq", "profit": 15500},
    {"name": "ewq", "profit": 1200}]


# Первое решение сложность O(3N)
def find_best_company(my_list):
    profit_list = []  # O(1)
    best_profit = 0  # O(1)
    best_count = 0  # O(1)
    for ind in range(len(my_list)):  # O(N)
        profit_list.append(my_list[ind]["profit"])  # O(1)
    for y in range(len(profit_list)):  # O(N)
        if profit_list[y] > best_profit:  # O(N)
            best_profit = profit_list[y]  # O(1)
            best_count = y  # O(1)
    return best_count  # O(1)


best_company = []  # O(1)

# я думаю что сложность этой конструкции while O(3) так как надо 3 раза перебирать списки хотя
# внутри конструкции while сложность каждой операции O(1)
while len(best_company) != 3:  # O(9)
    i = find_best_company(my_list1)  # O(1)
    best_company.append(my_list1.pop(i))  # O(2)

print(best_company)

# Второе решение сложность O(3N) так как надо 3 раза выполнять по 4 операции в которых одна операция
# требует нахождение максимума 3 раза
my_list2 = [
    {"name": "abc", "profit": 12500},
    {"name": "abb", "profit": 500},
    {"name": "bbq", "profit": 15500},
    {"name": "ewq", "profit": 1200}]
profit_list2 = []  # O(1)
better_company = []  # O(1)


def find_better_company(my_list):
    index_max = max(range(len(my_list)), key=my_list.__getitem__)  # O(N)
    return index_max  # O(1)


a = 0
while a < len(my_list2):  # O(N)
    profit_list2.append(my_list2[a]["profit"])  # O(1)
    a += 1  # O(1)

for b in range(3):  # O(12)
    index_better_value = find_better_company(profit_list2)  # O(1)
    better_company.append(my_list2[index_better_value])  # O(1)
    my_list2.pop(index_better_value)  # O(1)
    profit_list2.pop(index_better_value)  # O(1)

print(better_company)

# Третье решение сложность O(N)

my_list3 = [
    {"name": "abc", "profit": 12500},
    {"name": "abb", "profit": 500},
    {"name": "bbq", "profit": 15500},
    {"name": "ewq", "profit": 1200}]


def convert_list(my_list):
    my_dict = {}  # O(1)
    for index in range(len(my_list)):  # O(N)
        my_dict[my_list[index]["name"]] = my_list[index]["profit"]  # O(1)
    return my_dict  # O(1)


company_dict = convert_list(my_list3)  # O(1)
company_first = max(company_dict, key=company_dict.get)  # O(N)
company_dict.pop(company_first, None)  # O(1)
company_second = max(company_dict, key=company_dict.get)  # O(N)
company_dict.pop(company_second, None)  # O(1)
company_third = max(company_dict, key=company_dict.get)  # O(N)

print(company_first)
print(company_second)
print(company_third)
