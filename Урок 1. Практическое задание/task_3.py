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

companies_dict = {'ООО Батарейка': 53254673.33, 'ООО Какие Люди': 23335230.43, 'ООО Где я': 2153129.81,
                  'ООО КомПСС': 3473073.76, 'ООО БУДХиБ': 5846934.90, 'ПАО Добрый Д': 7830023.62}


# Решение №1 (сложность O(2n)):
# (Это лучшее из трёх решение, исходя из сложности, а так же краткости кода.)
def profit_1(input_list):
    input_list_sorted = {k: input_list[k] for k in sorted(input_list, key=input_list.get, reverse=True)}
    print(f'Три компании с наибольшей годовой прибылью:\n')
    for k in tuple(input_list_sorted)[:3]:
        print(f'{k}, {input_list_sorted[k]}\n')



# profit_1(companies_dict)


# Решение №2 (сложность O(3*(n^2)):
def profit_2(input_list):
    out = []
    max_key = ''
    print(f'Три компании с наибольшей годовой прибылью:\n')
    for _ in range(3):
        max_profit = 0
        for v in input_list.values():
            if v > max_profit:
                max_profit = v
        for k, v in input_list.items():
            if v == max_profit:
                out.append(f'{k}, {v}')
                max_key = k
                break
        for k in input_list.keys():
            if k == max_key:
                print(f'{k}, {input_list.pop(max_key)}')
                break


# profit_2(companies_dict)


# Решение №3 (сложность O(2*(n^2))
def profit_3(input_list):
    profit_storage = []
    for _ in range(3):
        max_profit = 0
        for v in input_list.values():
            if v > max_profit and v not in profit_storage:
                max_profit = v
        profit_storage.append(max_profit)

    for k in input_list.keys():
        for i in profit_storage:
            if input_list[k] == i:
                print(f'{k}, {input_list[k]}')

# profit_3(companies_dict)
