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
    'com1': 290,
    'com2': 1000,
    'com3': 4222,
    'com4': 123,
    'com8': 0,
    'com9': 78,
    'com10': 6666,
    'com11': 5666
}


# Вариант 1. Сложность O(N logN)
def find_max1(com_dict):
    lst = list(com_dict.values())
    lst.sort(reverse=True)
    lst_max = []
    for i in range(3):
        lst_max = [key for i in range(3) for key, val in com_dict.items() if lst[i] == com_dict[key]]
    return lst_max


# Вариант 2. Сложность O(N)
def find_max2(com_dict):
    result = {}
    copy_dict = com_dict.copy()
    for i in range(3):
        max_val = max(copy_dict.values())
        for key, val in copy_dict.items():
            if val == max_val:
                result[key] = copy_dict.pop(key)
                break
    return result


# Вариант 3. Сложность O(N).
# Этот вариант считаю лучшим, так как в сравнении с вариантом 2 (с такой же сложностью)
# здесь меньше обходов, а значит выше скорость выполнения
def find_max3(com_dict):
    lst_max = []
    for key, val in com_dict.items():
        if len(lst_max) < 3:
            lst_max.append([key, val])
        else:
            for i in range(3):
                if lst_max[i][1] < val:
                    lst_max[2] = [key, val]
                    break
        lst_max.sort(key=lambda com: com[1], reverse=True)
    return lst_max


print(find_max1(company_profit))
print(find_max2(company_profit))
print(find_max3(company_profit))




