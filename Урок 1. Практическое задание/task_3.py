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
сompanies = {
    'yandex': 2000,
    'amdocs': 4500,
    'oracle': 5300,
    'sibintek': 450,
    'rostelecom': 10,
    'vimpelcom': 200,
    'mts': 4030,
    }

# O(N^2)
def sorted(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]
    return random_list[0:3]

list_from_dictionary = list(сompanies.items())
for i in sorted(list_from_dictionary):
    print(i[0], ':', i[1])

print('#' * 18)

# O(N)
def top3(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max

print(top3(сompanies))

"Лучший вариант второй, т.к. имеет минимальную  сложность " \
"и решает поставленную задачу без изменение исходного словаря и без лишней сортировки"