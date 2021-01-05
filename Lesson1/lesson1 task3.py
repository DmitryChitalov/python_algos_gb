"""
Задание 3.

Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

"""

companies = {
    'labirint': 17785,
    'chitai-gorod': 77000,
    'bookvoed': 15342,
    'book24': 14578,
    'biblioglobus': 76391,
    'belygorod': 782409,
    'respublica': 429781
}

#решение полностью вытащено из лекций

# первый способ - сложность O(n)
def three_rich(year_list):
    input_max = {}
    list_d = dict(year_list)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max
print(three_rich(companies))

# второй способ - сложность O(N*LogN)
list_dictionary = list(companies.items())
list_dictionary.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_dictionary[i][0], ':', list_dictionary[i][1])

# всегда предпочтителен вариант с наименьшей сложностью, в данном случае - с линейной, это первый вариант