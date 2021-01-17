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


def top_profit_1(dict_obj:dict, count:int) -> list:
    """ Функция принимает на вход два параметра: словарь и целое число,
    и возвращает 'count' пар (ключ, значение) с максимальным значением

    Вариант 1 - сложность O(N log N)
    """
    result_list = []
    dict_items = list(dict_obj.items())                                 # O(N)
    dict_items.sort(key=lambda i: i[1], reverse=True)                   # О(N log N)
    for i in range(count):                                              # O(3)
        result_list.append(dict_items[i])                               # O(1)
    return result_list


def top_profit_2(dict_obj:dict, count:int) -> list:
    """ Функция принимает на вход два параметра: словарь и целое число,
    и возвращает 'count' пар (ключ, значение) с максимальным значением

    Вариант 2 - сложность O(N^2)
    """
    dict_copy = dict_obj.copy()                                         # O(N)
    result_list = []                                                    # O(1)
    for i in range(count):                                              # O(1)
        for k,v in dict_copy.items():                                   # O(N)
            if v == max(dict_copy.values()):                            # O(N)
                result_list.append((k,v))                               # O(1)
                dict_copy.pop(k)                                        # O(1)
                break
    return result_list                                                  # O(1)


def top_profit_3(dict_obj:dict, count:int) -> list:
    """ Функция принимает на вход два параметра: словарь и целое число,
    и возвращает 'count' пар (ключ, значение) с максимальным значением

    Вариант 3 - сложность O(N) - наиболее предпочтительный вариант
    """
    dict_copy = dict_obj.copy()                                         # O(N)
    result_list = []                                                    # O(1)
    for i in range(count):                                              # O(1)
        max_profit_key = ''                                             # O(1)
        max_profit_value = 0                                            # O(1)
        for k, v in dict_copy.items():                                  # O(N)
            if v > max_profit_value:                                    # O(1)
                max_profit_key = k                                      # O(1)
                max_profit_value = v                                    # O(1)

        result_list.append((max_profit_key, max_profit_value))          # O(1)
        dict_copy.pop(max_profit_key)                                   # O(1)
    return result_list                                                  # O(1)


companies = {
    "Рога и копыта": 100500,
    "Медведи и Лоси": 1000,
    "За Орду!": 5000000,
    "Следи за собой": 850000,
    "Кошки-Мишки": 2000000
}

print(top_profit_1(companies, 5))
print(top_profit_2(companies, 5))
print(top_profit_3(companies, 5))
