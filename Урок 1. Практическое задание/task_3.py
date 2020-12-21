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
from collections import Counter
from heapq import nlargest

test_lst = random.sample(range(100000, 1000000), 10)
DATABASE = {}
i = 1
for number in test_lst:
    DATABASE["Company #" + str(i)] = number
    i += 1

print(DATABASE)


def find_top3_1(db):
    y = sorted(db.items(), key=lambda x: x[1], reverse=True)  # O(N*logN)
    return y[:3]


def find_top3_2(db):
    k = Counter(db)
    return k.most_common(3)  # O(N*log3) в случае если указано кол-во или O(N*logN) если кол-во не указано


def find_top3_3(db):
    return nlargest(3, db, key=db.get)  # O(N*log3) - эффективное решение если нужно выбрать n элементов из словаря


top3_1 = find_top3_1(DATABASE)
for stat in top3_1:
    print(stat[0], stat[1], sep=" => ")

print('====================')

top3_2 = find_top3_2(DATABASE)
for stat in top3_2:
    print(stat[0], stat[1], sep=" => ")

print('====================')

top3_3 = find_top3_3(DATABASE)
for stat in top3_3:
    print(stat, DATABASE.get(stat), sep=" => ")
