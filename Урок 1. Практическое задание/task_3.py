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
company_info_dict = {'T_LLS':10000, 
                'Company_Sur':20000,
                'Hugs_llc': 45000,
                'Company_therd':30000,
                'Fifth_company':15000,
                'Company_sixth':58000
                }
# var_1
def max_profit_var1 (dict_t1):
    l_keys = list(dict_t1.keys())               # O(n)    
    l_values = list(dict_t1.values())           # O(n) ==> O(n*n)= n**2
    l_values.sort(reverse=False)                # O(n log n)
    lst_max_profit_after_sort = l_values[3:]    # итого = O(n**2), как превалирущее
    lst_primary_comp=[]
    for i in l_keys:
        var_val = dict_t1[i]
        if var_val in lst_max_profit_after_sort:
            lst_primary_comp.append(i)
    return lst_primary_comp 

print(f"Наибольшая прибыль у : {'; '.join(max_profit_var1(company_info_dict))}'\n'")

# var_2
def max_profit_var2 (dict_t2):
    lst_max_profit = []
    var_element = 0
    while var_element < 3:
        max_prof = max(dict_t2, key=dict_t2.get)      # O(n)
        lst_max_profit.append(max_prof)               # O(1)
        dict_t2.pop(max_prof)                         # O(1)
        var_element += 1                              # итого = O(n) как превалирущее  
    return lst_max_profit                             # вывод - более эффективное решение

print(f"Наибольшая прибыль у :{'; '.join(max_profit_var2(company_info_dict))}")