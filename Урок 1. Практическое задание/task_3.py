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



из двух функций max_by_score более быстрая
"""



companies = {"gazprom": 100, "novatec": 50, "rosseti": 75, "lukoil": 80, "rosneft": 99, "vaz": 25, "mailru": 49, "shell": 110}


def max_by_sort_and_del(dct):                       # O(n^2)
    dict_of_3max = {}
    dct_temp = dct.copy()

    for i in range(3):                              # O(n)
        max_res = 0
        keys_sample = ""
        for key, values in dct_temp.items():        # O(n)
            if values > max_res:
                max_res = values
                keys_sample = key
        dict_of_3max[i] = (keys_sample, max_res)
        del dct_temp[keys_sample]
    return dict_of_3max


def max_by_score(dct):                                 # O(n)
    position = ('1', '2', '3')
    dic_res = dict.fromkeys(position, ("test", 0))
    for key, values in dct.items():                    # O(n)
        if values > dic_res['1'][1]:
            dic_res['3'] = dic_res['2']
            dic_res['2'] = dic_res['1']
            dic_res['1'] = (key, values)
        elif values > dic_res['2'][1]:
            dic_res['3'] = dic_res['2']
            dic_res['2'] = (key, values)
        elif values > dic_res['3'][1]:
            dic_res['3'] = (key, values)
    return dic_res


dict_res = max_by_sort_and_del(companies)
print(dict_res)

dict_res = max_by_score(companies)
print(dict_res)


