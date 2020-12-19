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
company_profit = {
    'Company_1': 50000,
    'Company_2': 40000,
    'Company_3': 100000,
    'Company_4': 20000,
    'Company_5': 30000,
    'Company_6': 200000,
    'Company_7': 45000,
    'Company_8': 3000
}

def get_three_max_profit_1(dict_obj):
    keys_list = list(dict_obj.keys())
    value_list = list(dict_obj.values())
    value_list.sort(reverse=True)
    three_max_profits = value_list[:3]
    company_with_max_profit_names = []
    for elem in keys_list:
        value = dict_obj[elem]
        if value in three_max_profits:
            company_with_max_profit_names.append(elem)
    return company_with_max_profit_names


def get_three_max_profit_2(dict_obj):
    list_values = list(dict_obj.values())
    three_max_profits = []
    for num in range(3):
        max_value = max(list_values)
        three_max_profits.append(max_value)
        list_values.remove(max_value)
    names_company = [key for key in dict_obj if dict_obj[key] in three_max_profits]
    return names_company


def get_three_max_profit_3(dict_obj):
    max_profit_list = []
    list_items = list(dict_obj.items())
    list_items.sort(key=lambda val: val[1], reverse=True)
    for num in range(3):
        max_profit_list.append(list_items[num][0])
    return max_profit_list


"""
get_three_max_profit_1 и get_three_max_profit_2 имеют сложность O(n**2), 
а функция get_three_max_profit_3 O(nlogn) за счёт использования метода sort. 
Соответственно функция get_three_max_profit_3 является наилучшим решением
"""


if __name__ == '__main__':
    print(company_profit)
    company_names_1 = get_three_max_profit_1(company_profit)
    print(company_names_1)
    company_names_2 = get_three_max_profit_2(company_profit)
    print(company_names_2)
    company_names_3 = get_three_max_profit_3(company_profit)
    print(company_names_3)
