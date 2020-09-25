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

company = {
    'Sony': 2800,
    'Lenovo': 333,
    'Microsoft': 28000,
    'Apple': 98765,
    'Gaz': 55555,
    'Tinkoff': 3000
}

list_company = list(company.items())
num_val = 3

# Вариант 1 сложность = O(n log n)
print('-' * 25)
list_company.sort(key=lambda i: i[1], reverse=True)
for i in range(num_val):
    print(f'{list_company[i][0]}:{list_company[i][1]}')
print('-' * 25)


# Вариант 2 сложность = O(N)
def search_max_profit_3(lst, num_of_val):
    output = {}
    dictionary = dict(lst)
    for i in range(num_of_val):
        maximum = max(dictionary.items(), key=lambda k_v: k_v[1])
        del dictionary[maximum[0]]
        output[maximum[0]] = maximum[1]
    return output


for i in search_max_profit_3(company, num_val):
    print(f'{i}:{company[i]}')
print('-' * 25)


# Вариант 3 сложность = O(n ** 2)
def search_max_profit_1(lst, num_of_val):
    for idx_1 in range(len(lst)):
        min_val_idx = idx_1
        for idx_2 in range(idx_1 + 1, len(lst)):
            if lst[idx_2][1] > lst[min_val_idx][1]:
                min_val_idx = idx_2
        lst[idx_1], lst[min_val_idx] = lst[min_val_idx], lst[idx_1]
    return lst[0:num_of_val]


for i in search_max_profit_1(list_company, num_val):
    print(f'{i[0]}:{i[1]}')
print('-' * 25)

# Вариант 2 самый эффективный, т.к. самый быстрый
