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

COMPANY_DICT = {"Марвел": 23587, "ДиСиКомикс": 54754, "Амбрелла": 2545549, "ДолгостройЛТД": 3153223, "МММ": 3465987}

company_dict_values = list(COMPANY_DICT.values())
company_dict_keys = list(COMPANY_DICT.keys())
company_dict_values_2 = company_dict_values.copy()

# 1 вариант - сложность O(n log n):
sorted_values = sorted(COMPANY_DICT.values(), reverse=True)[:3]  # O(n log n)
for item in sorted_values:                                       # O(1)
    find_index = company_dict_values.index(item)                 # O(n)
    max_key = company_dict_keys[find_index]
    print(max_key)

# 2 вариант - сложность O(n):
for i in range(3):                                               # O(1)
    max_value = max(company_dict_values_2)                       # O(n)
    find_index = company_dict_values.index(max_value)            # O(n)
    max_key = company_dict_keys[find_index]                      # O(1)
    print(max_key)
    company_dict_values_2.remove(max_value)                      # O(n)
