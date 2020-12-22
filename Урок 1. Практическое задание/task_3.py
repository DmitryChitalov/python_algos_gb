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

org_dict = {
    'ПАО "РОК"': 91003,
    'ОАО "ПРЫГ"': 683085,
    'ООО "СКОК"': 465929,
    'Фирма "ТРЕСК"': 952579,
    'АйтиКорпорейшн': 860223,
    'ЗАО "ВЕНИК"': 466458,
    'ТК "СУСАНИН"': 249509
}


# V-1
def three_firms(firms_dict):
    income_list = []
    for key, value in firms_dict.items():  # O(n)
        income_list.append(value)        # O(1)

    a = max(income_list)                 # O(n) -- по таблице
    income_list.remove(a)                # O(n)
    b = max(income_list)                 # O(n)
    income_list.remove(b)                # O(n)
    c = max(income_list)                 # O(n)

    three_max_org = {}
    for key, value in firms_dict.items():  # O(n)
        if value == a or value == b or value == c:  # O(1)
            three_max_org[key] = value   # O(n)
    return three_max_org


print(three_firms(org_dict))
"""Сложность O(n).
Решение нельзя назвать оптимальным. Много строчек кода. Много переменных.
Нужно избавиться от лишних переменных.
"""


# V-2
def three_firms_v2(firms_dict):                                      # общая сложность O(n*log n)
    func_dict = {}                                                   # O(1)
    func_list = sorted(list(firms_dict.values()))                    # предполагаю, что по аналогии с sort() O(n*log n)
    for key, value in firms_dict.items():                            # O(n)
        if value == func_list[len(func_list) - 1] \
                or value == func_list[len(func_list) - 2]\
                or value == func_list[len(func_list) - 3]:           # O(1)?
            func_dict[key] = value                                   # O(1)
    return func_dict                                                 # O(1)


print(three_firms_v2(org_dict))
"""Сложность O(n*log n). 
Код стал короче примерно вдвое. Избавилиь от лишних переменных.
Но при этом повысилась сложностьт из-за функции sorted, если я конечно прав и её сложность составляет O(n log n),
тогда можно сказать, что код более читабельный, чем предыдущий, однако имеет более высокую сложность"""


# V-3
def three_firms_v3(firms_dict):      # общая сложность O(n)
    three_dict = {}                                                  # O(1)
    func_dict = dict(firms_dict)                                     # O(1)
    for i in range(3):                                               # O(n)
        income_max = max(func_dict.items(), key=lambda k: k[1])      # O(1)?
        del func_dict[income_max[0]]
        three_dict[income_max[0]] = income_max[1]
    return three_dict


print(three_firms_v3(org_dict))
"""Сложность O(n).
Наиболее оптимальное решение.
"""
