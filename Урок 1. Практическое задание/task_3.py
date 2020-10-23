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


def very_top(info_dict):
    """
    Это вспомогательная функция определения одного максимального элемента для функции top_v1
    T(n) = n*log(n) + 1*n
    """
    max_profit = max(info_dict.values())                # O(n*log(n))
    for el in info_dict:                                # O(n)
        if info_dict.get(el) == max_profit:             # O(1)
            return el


def top_v1(info_dict):
    """
    T(n) = 1 + n + 3*(n*log(n) + 1*n + 1 + 1) = 3*n*log(n) + 4n + 7
    """
    top3 = []                                           # O(1)
    info_dict_copy = info_dict.copy()                   # O(n)
    for i in range(3):                                  # O(3)
        cur_top = very_top(info_dict_copy)              # T(n) = n*log(n) + 1*n
        top3.append(cur_top)                            # O(1)
        info_dict_copy.pop(cur_top)                     # O(1)
    return top3


def top_v2(info_dict):
    """
    T(n) = 1 + n + n * (n*log(n) + n + 2) + 1 = 2 + n + n^2*log(n) + n^2 + 2n + 1 = (1+log(n))*n^2 + 3n + 3
    """
    min_profit_company = ''                             # O(1)
    info_dict_copy = info_dict.copy()                   # O(n)
    while len(info_dict_copy) > 3:                      # O(n)
        min_profit = min(info_dict_copy.values())       # O(n*log(n))
        for el in info_dict_copy:                       # O(n)
            if info_dict_copy.get(el) == min_profit:    # O(1)
                min_profit_company = el                 # O(1)
        info_dict_copy.pop(min_profit_company)          # O(1)
    return list(info_dict_copy.keys())


information_storage = {'MAIL.RU': 18690, 'Yandex': 12830, 'МТС': 54240, 'АФК Система': 65686, 'МГТС': 39730,
              'Наука-Связь': 0.27, 'Ростелеком': 14780, 'Таттелеком': 810.09, 'Центральный Телеграф': 2090}

print(top_v1(information_storage))

print(top_v2(information_storage))

"""
Вывод: сложность функции top_v1 определяется как 3*n*log(n)
в то время как функция top_v2 : log(n)*n^2, что бри больших 'n' будет заметно сложнее.
Более эффективной будет функция top_v1 
"""
