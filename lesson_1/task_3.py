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
import random
import time


# сложность O(N)
def f_max_value(md):
    max_value = list(md.values())[0]
    max_key = list(md.keys())[0]

    for k, v in md.items():
        if v > max_value:
            max_value = v
            max_key = k

    return max_key, max_value


# сложность O(N^2)
def dict_sort1(md):
    sorted_dict = {}

    for k, v in list(md.items()):
        max_k, max_v = f_max_value(md)
        sorted_dict[max_k] = max_v
        md.pop(max_k)

    return sorted_dict


# сложность O(N)
def top3(ds):
    top3_dict = {}
    count = 0
    for k, v in ds.items():
        if count < 3:
            top3_dict[k] = v
            count += 1
    return top3_dict


# сложность O(N log N)
def dict_sort2(md):
    list_d = list(md.items())
    list_d.sort(key=lambda i: (-i[1], i[0]))

    sorted_dict = {}

    for i in list_d:
        sorted_dict[i[0]] = i[1]
        # print(i[0], ':', i[1])

    return sorted_dict


my_dict = {'city_' + str(x): random.randint(1, 1000) for x in range(random.randint(1, 1000))}

my_dict1 = my_dict.copy()
my_dict2 = my_dict.copy()

start_val = time.time()
print(top3(dict_sort1(my_dict1)))
print("время алгоритма №1 при сложности O(N^2): ", time.time() - start_val)

# более эффективное решение т.к, используется встроенный для списоков метод сортировки. при этом не вызывается функция поиска максимального значения в цикле.
start_val = time.time()
print(top3(dict_sort2(my_dict2)))
print("время алгоритма №2 при сложности O(N log N): ", time.time() - start_val)
