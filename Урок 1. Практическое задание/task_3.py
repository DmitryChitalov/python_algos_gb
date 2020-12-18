"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно
выполнить
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
from random import randint

companies_profits = {'name' + str(i): randint(5000, 1000000) for i in
                     range(1, 51)}
#  Выбрал словарь, т.к. мало опыта работы с ними
#  Основная сложность возникла с извлечением ключа для максимального значения

def max_profit_v1(my_dict):
    """"
    O(N)
    Через переменную max делаем перебор элементов, находим наибольший,
    убираем его из массива, добавляем в result
    """
    dict = my_dict.copy()
    result = {}
    while len(result) < 3:
        max = list(dict.values())[1]
        key = list(dict.keys())[1]
        for i, j in dict.items():
            if j > max:
                key = i
                max = j
        result[key] = max
        dict.pop(key)
    return result


def max_profit_v2(dict):
    """ O(n**2)
    Сделал для разнообразия, почти все варианты получаются как О(N)
    """
    companies = list(dict.keys())
    profits = list(dict.values())
    for source_number in range(len(profits)):
        for target_number in range(source_number + 1,
                                   len(profits)):
            if profits[source_number] < profits[target_number]:
                profits[source_number], profits[target_number] = \
                    profits[target_number], profits[source_number]
                companies[source_number], companies[target_number] = \
                    companies[target_number], companies[source_number]
    result = {companies[i]: profits[i] for i in range(3)}
    return result


def max_profit_v3(dict):
    """По аналогии с первой весрией, но через генератор для поиска значения
    ключа, чтобы вырезать его из словаря, для поиска нового максимума
    По эффективности аналогично первому варианту, так как в обоих случаях
    прогон по словарю идет 3 раза
    Данный вариант может быть немного эффективнее с учетом меньшего количества
    присваивания переменных"""
    temp = dict.copy()
    result = {}
    while len(result) < 3:
        max1 = max(temp.values())
        key1 = [k for k, v in temp.items() if v == max1]
        result[key1[0]] = max1
        temp.pop(key1[0])
    return result


print(max_profit_v1(companies_profits))
print(max_profit_v2(companies_profits))
print(max_profit_v3(companies_profits))
