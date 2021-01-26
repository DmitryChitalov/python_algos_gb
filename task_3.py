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


def search_large1(dict_test):                   # Итоговая O! = n + n
    sorted_v = sorted(dict_test.items(), key=lambda i: i[1], reverse=True)  # Оценка сложности:
    # O(1)      O(1)    O(1)                    O(n)                        => O(n)

    return [sorted_v[i][0] for i in range(3)]
    # O(1)  O[len() =  O(n)        O(1)]        =>O(n)


def search_large2(dict_test):                   # Итоговая O! = n+ n + n
    prof_dict = {j: i for (i, j) in dict_test.items()}                      # O(n)
    sorted_v = sorted(prof_dict.items(), key=lambda i: i[0], reverse=True)  # O(n)
    return [sorted_v[i][1] for i in range(3)]                               # O(n)


def search_large3(dict_test):                   # Итоговая O! = n*(n*log(n))
    sorted_values = sorted(dict_test.values(), reverse=True)    # O(1)
    sorted_dict = {}                                            # O(1)

    for i in sorted_values[0:3]:                # O(n)
        for k in dict_test.keys():              # O(*n)
            if dict_test[k] == i:               # O(log(n))
                sorted_dict[k] = dict_test[k]   # O(1)
                break                           # O(1)
    return list(sorted_dict)                    # O(1)


def search_large4(dict_test):                   # Итоговая O! = n +1 +n +1
    prof_dict = {j: i for (i, j) in dict_test.items()}  # O(n)
    list_max = []                                       # O(1)
    for i in range(3):                      # O(len     # O(1)  => O(n)
        max_elem = max(prof_dict.keys())                # O(n)
        list_max.append(prof_dict.get(max_elem))        # O(1)
        prof_dict.pop(max_elem)                         # O(1)

    return list_max                                     # O(1)


dict_comp = {
    'Clxqjnnyl': 2700,
    'B_nbpcapiw': 38000,
    'C_paswtntq': 36000,
    'A_vltujfdb': 42000,
    'Bjgfrsjuq': 2700,
    'Lapaswtntq': 3555}

# 2. Оценка сложности каждого решения

print(search_large1(dict_comp))     # O! n+n
print(search_large2(dict_comp))     # O! n+n+n
print(search_large3(dict_comp))     # O! n**2
print(search_large4(dict_comp))     # O! n +n +1 +1

# 3. Самая эффективная функция по результатам оценки сложности
# search_large1()
