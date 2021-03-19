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

from operator import itemgetter
from random import randrange, random
from time import process_time

# генерирует список пар (название, выручка)
# [("ABCD",12.34),("FDGR",74.23)]
def gen_db(size=10):
    return [
        (''.join(
            chr(randrange(ord('A'), ord('Z')))
            for i in range(4)
        ), 100 * random())
        for i in range(size)
    ]

# Метод №1
def top3_1(db): # O(n*log(n))
    return sorted(db, key=itemgetter(1), reverse=True)[:3]

# Метод №2
# чтобы корректно сравнивать с методом №1,
# считаем сравнение и перестановку за 1 операцию
def top3_2(db): # O(n*3)
    r1 = r2 = r3 = ('NONE', -1)
    for i in db:            # O(3*n)
        if r1[1] < i[1]:    # O(1)
            r1, i = i, r1
        if r2[1] < i[1]:    # O(1)
            r2, i = i, r2
        if r3[1] < i[1]:    # O(1)
            r3, i = i, r3
    return (r1, r2, r3)

def print_result(res):
    for nm, val in res:
        print(f"{nm}: {val}")

def timeit(fun, *args):
    t0 = process_time()
    ret = fun(*args)
    dt = process_time()-t0
    return ret, dt

dbsize = 500
db = gen_db(dbsize)

print()
print("Database:")
if dbsize<25:
    print_result(db)
print()
print("Top 3 (method 1):")
res, dt = timeit(top3_1, db)
print_result(res)
print("time: ", dt)
print()
print("Top 3 (method 2):")
res, dt = timeit(top3_2, db)
print_result(res)
print("time: ", dt)

# Для больших (dbsize>1000) списков однозначно эффективнее метод №2.
# Измерения показывают, что для dbsize=10 быстрее №2,
# а для dbsize=400 быстрее №1