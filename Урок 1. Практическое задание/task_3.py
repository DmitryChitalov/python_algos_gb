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

########################################################################################################################
company = {'samsung': 50000, 'apple': 100000, 'microsoft': 80000, 'motortola': 10000, 'RomanIP': 250000}

"""
Имеет квадратичную сложность, скорость средняя, 
однако благодаря своей лаконичности легко читается. 
"""
# Сложность: O(n ** 2)


number_one = company.copy()
for i in range(3):
    profit = max(number_one.values())
    firm = ''.join(([i for i in number_one if number_one[i] == profit]))
    print(f'{firm}: {profit}')
    del number_one[firm]

########################################################################################################################
    """
    Как и предыдущая, сложность - квадратичная, скорость средняя, 
    в отличии от предыдущей, имеет более громоздкую структуру,
    что в свою очередь усложняет понимание кода. 
    """
# Сложность: O(n ** 2)


number_two = company.copy()
idx = 3
while idx != 0:
    profit = []
    for p in number_two.values():
        profit.append(p)
    for f in number_two.keys():
        if number_two[f] == max(profit):
            print(f'{f}: {number_two[f]}')
            break
    del number_two[f]
    idx -= 1

########################################################################################################################
    """
    Относительно быстрый и лаконичный способ выполнения задачи. 
    Минимальная нагрузка из всех предоставленных решений.
    """
# Сложность: O(n * log * n)


number_tree = company.copy()
profit = list(number_tree.items())
profit.sort(key=lambda b: b[1])
profit.reverse()
for i in profit[:3]:
    print(f'{i[0]}: {i[1]}')

