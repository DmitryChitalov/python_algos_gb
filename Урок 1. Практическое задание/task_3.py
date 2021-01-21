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
d = {'1d':3, '2a':2, '3f':6}

def maximum(dictionary):
    list_profit = []
    for key in dictionary:
        list_profit.append(dictionary.get(key))
    result = list_profit[0]
    for i in range(len(list_profit)):
        for j in range(len(list_profit)):
            if list_profit[j] > list_profit[i] and list_profit[j] > result:
                result = list_profit[j]
    result = (list(dictionary.keys())[list(dictionary.values()).index(result)])
    return result
#O(n^2)

def maximum2(dictionary):
    list_profit = []
    for key in dictionary:
        list_profit.append(dictionary.get(key))
    result = list_profit[0]
    for i in range(len(list_profit)):
        if list_profit[i] > result:
            result = list_profit[i]
    result = (list(dictionary.keys())[list(dictionary.values()).index(result)])
    return result
#O(n)
#Эффективнее решение 2 так, как линейные операции проще квадратичных
print(maximum(d))

