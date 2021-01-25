"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from random import randint
import time

# Заполним список и слварь случайными цифрами
n = randint(1, 10000000)

def get_lst(n):
    start_val = time.time()
    lst = [i for i in range(n)]
    end_val = time.time()
    return end_val - start_val


def get_dict(n):
    start_val = time.time()
    dct = {i: i for i in range(n)}
    end_val = time.time()
    return end_val - start_val


print(get_lst(n))
print(get_dict(n))


"""
lst time(1, 5000000): 0.019948482513427734
dict time(1, 5000000): 0.03309226036071777
lst time(1, 10000000): 0.13164710998535156
dict time(1, 10000000): 0.32213783264160156

Заполнение словаря происходит медленнее списка почти примерно два раза.
Вероятно это связано с вычислением хэш функции для каждого ключа.
"""

n = 30000000


# Удаление элемента
def lst_remote(n):
    lst = [i for i in range(n)]
    start_val = time.time()
    lst.pop(2000000)
    end_val = time.time()
    return end_val - start_val


def dict_remote(n):
    dct = {i: i for i in range(n)}
    start_val = time.time()
    dct.pop(2000000)
    end_val = time.time()
    return end_val - start_val


print(lst_remote(n))
print(dict_remote(n))

"""
lst_remote time(10000000)
pop(9000000)
time: 0.0007312297821044922
dct: 0.0

lst_remote (30000000)
pop(2000000)
time: 0.029920101165771484
dct: 0.0

В словаре удление происходит мгновенно благодаря хэш-таблице.

"""
