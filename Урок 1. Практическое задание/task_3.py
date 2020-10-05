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


# Хранилище компаний
companies = [
    {'id': 1, 'name': 'Lorem', 'profit_year': 10000.00},
    {'id': 2, 'name': 'Ipsum', 'profit_year': 12000.00},
    {'id': 3, 'name': 'Dolor sit amet', 'profit_year': 15000.00},
    {'id': 4, 'name': 'Duis aute', 'profit_year': 123458.55},
    {'id': 5, 'name': 'Quis autem', 'profit_year': 58000.00},
    {'id': 6, 'name': 'Рога и Копыта', 'profit_year': 5000.00},
    {'id': 7, 'name': 'На деревне', 'profit_year': 88005.44},
    {'id': 8, 'name': 'ИП Пупкин', 'profit_year': 23000.00},
    {'id': 9, 'name': 'ООО', 'profit_year': 30000.00},
    {'id': 10, 'name': 'Однажды', 'profit_year': 55000.00}
]


###########################################
def output_companies(companies):
    """
    Функция вывода компаний.

    """
    for comp in companies:
        print(f"{comp['id']}: {comp['name']}. Прибыль: {comp['profit_year']}")


###########################################
def get_best_1(companies, count = 3):
    """
    Вариант 1.
    Функция выбора определенного количества лучших компаний из списка.

    """
    bests = []
    for comp in companies:
        if len(bests) == 0:
            bests.append(comp)
            continue
        if len(bests) < count:
            for i in range(len(bests)):
                if comp['profit_year'] > bests[i]['profit_year']:
                    bests.insert(i, comp)
                    break
                if i == len(bests) - 1:
                    bests.append(comp)
            continue
        for i in range(len(bests)):
            if comp['profit_year'] > bests[i]['profit_year']:
                bests.insert(i, comp)
                bests.pop()
                break
    return bests


###########################################
def get_best_2(companies, count = 3):
    """
    Вариант 2.
    Функция выбора определенного количества лучших компаний из списка.

    """
    l_func = lambda comp: comp['profit_year']
    return sorted(companies, key=l_func, reverse=True)[:count]
    # return sorted(companies, key=lambda comp: comp['profit_year'], reverse=True)[:count]


###########################################
def get_best_3(companies, count = 3):
    """
    Вариант 3.
    Функция выбора определенного количества лучших компаний из списка.

    """
    bests = []
    while count > 0:
        indx_max = 0
        for j in range(1, len(companies)):
            if companies[j]['profit_year'] > companies[indx_max]['profit_year']:
                indx_max = j
        bests.append(companies[indx_max])
        companies.pop(indx_max)
        count -= 1
    return bests


print('\n')

print('Вариант 1:')
output_companies(get_best_1(companies))
print('-' * 30, end="\n\n")

print('Вариант 2:')
output_companies(get_best_2(companies))
print('-' * 30, end="\n\n")

print('Вариант 3:')
output_companies(get_best_3(companies))
print('-' * 30, end="\n\n")
