"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (желательно хотя бы два)
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

# Хранилище с информацией

companies = {
    'Exxon Mobil': 265700000,
    'WalMart': 524000000,
    'Royal Dutch Shell': 311600000,
    'Sinopec Group': 369200000,
    'China National Petroleum': 364100000,
    'Saudi Aramco': 329800000,
    'State Grid': 387000000,
    'Toyota': 280500000,
    'BP': 278400000,
    'Volkswagen': 275200000
}


# Первый вариант решения

def max_year_profit(data):                    # O(N Log N)
    companies_list = list(data.items())       # O(N)
    companies_list.sort(key=lambda i: i[1])   # O(N Log N)
    companies_list.reverse()                  # O(N)
    return dict(companies_list[:3])           # O(N)


# Второй вариант решения

def top_year_profit(data):                                               # O(N^2)
    array = list(data.values())                                          # O(N)
    array.sort()                                                         # O(N Log N)
    new_dict = {k: v for k, v in companies.items() if v in array[-3:]}   # O(N^2)
    return new_dict                                                      # O(1)


# Третий вариант решения

def big_year_profit(data):                                               # O(N^2)
    array = list(data.values())                                          # O(N)
    for i in range(len(array) - 1):                                      # O(N) * O(N) = O(N^2)
        max = i                                                          # O(1)
        j = i + 1                                                        # O(1)
        while j < len(array):                                            # O(N)
            if array[j] > array[max]:                                    # O(1)
                max = j                                                  # O(1)
            j += 1                                                       # O(1)
        array[i], array[max] = array[max], array[i]                      # O(1)
    new_dict = {k: v for k, v in data.items() if v in array[:3]}         # O(N^2)
    return new_dict                                                      # O(1)


print('Компании с наибольшей годовой прибылью:')
print(max_year_profit(companies))
print(top_year_profit(companies))
print(big_year_profit(companies))

'''
Наиболее предпочтителен первый вариант решения, имеющий линейно-логарифмическую сложность, так как второй и третий
варианты имеют квадратичную сложность и занмают больше времени на выполнение.
'''