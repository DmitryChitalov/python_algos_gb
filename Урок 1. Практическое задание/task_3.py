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

import copy

# input
firm_inc = {'google': 1.5, 'tesla': 2, 'uber': 0.5, 'mcdonalds': 0.3, 'netflix': 0.1, 'shell': -0.3, 'rwe': -0.5}


# resolution_1
def comparison_1(d):
    top_3 = sorted(d, key=d.get, reverse=True)[:3]
    print(top_3)


# resolution_2

def comparison_2(d):
    for z in range(0, 3):
        for company, income in d.items():
            maxi = 1
            for company2, income2 in d.items():
                if income < income2:
                    maxi = 0
            if maxi == 1:
                print(f'{company}: {income}')
                del_company = company
        d.pop(del_company)


# resolution_3

def comparison_3(d):
    for z in range(0, len(d) - 4):
        for company, income in d.items():
            mini = 1
            for company2, income2 in d.items():
                if income < income2:
                    mini = 0
            if mini == 1:
                print(f'{company}: {income}')
                del_company = company
        d.pop(del_company)


print('\nfoo_1:')
comparison_1(firm_inc)
print('\nfoo_2:')
comparison_2(firm_inc)
print('\nfoo_3:')
# 3rd function will not show an output as it has the same output as the 2nd
comparison_3(firm_inc)

# Функция 1 имеет сложность O(n log n), потому что функция sort имеет подобную сложность
# Функция 2 имеет сложность O(n^3), потому что имеет три встроенных цикла for
# Функция 3 имеет сложность O(n^3), потому что имеет три встроенных цикла for
# Наиболее эффективной функцие считаю первую, так как она перебирает список полностью только один раз при сортировке,
# что позволят сэкономить ресурсы при исполнении. Вторая по эффективности функция номер два поскольку требует меньше
# итераций для достижения результата, чем треться функция
