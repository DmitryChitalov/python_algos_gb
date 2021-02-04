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

db = {'Microsoft': 10000, "Apple": 18000, 'Samsung': 13000, 'Huawei': 20000, 'MTC': 1000}


def find_max_1(inp_db):
    i = 0
    top_comp = list()
    for company in inp_db.items():
        if i < 3:
            top_comp.append(company)
        else:
            for j in range(3):
                if top_comp[j][1] < company[1]:
                    top_comp.pop(j)
                    top_comp.insert(j, company)
                    break
        i += 1
    return top_comp

def find_max_2(inp_db):
    input_list=list(inp_db.items())
    input_list.sort(key=lambda x:x[1],reverse=True)
    return(input_list[0:3])


print(find_max_1(db))
print(find_max_2(db))
