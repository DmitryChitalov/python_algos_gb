"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import time


def stopwatch(data):
    def tmp(*args, **kwargs):
        t = time()
        res = data(*args, **kwargs)
        print(f"Time to complete: {round(time() - t, 9)}")
        return res

    return tmp


@stopwatch
def list_stopwatch(num):
    my_list = [i for i in range(num)]
    print(len(my_list), type(my_list))


@stopwatch
def list_insert_stopwatch(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)
    print(len(my_list), type(my_list))


@stopwatch
def dict_stopwatch(num):
    n = range(num)
    my_dict = {i: x for i, x in zip(n, n)}
    print(len(my_dict), type(my_dict),)


list_stopwatch(100000)
list_insert_stopwatch(100000)
dict_stopwatch(100000)

"""
    На примерах произвели заполнение списка (2 способа) и словаря. Результаты замеров:
    
    # для 10000 элементов:
    10000 <class 'list'> Time to complete: 0.0...
    10000 <class 'list'> Time to complete: 0.01695466
    10000 <class 'dict'> Time to complete: 0.000999689
    
    # для 100000 элементов:
    100000 <class 'list'> Time to complete: 0.005958
    100000 <class 'list'> Time to complete: 1.907715
    100000 <class 'dict'> Time to complete: 0.01296
    
    # для 100000 элементов:
    1000000 <class 'list'> Time to complete: 0.063828707
    1000000 <class 'list'> Time to complete: 310.315540314
    1000000 <class 'dict'> Time to complete: 0.139625788
    
    Наименее затратны операции заполнения списка списковыми включениями - сложность линейная - O(n).
    Наиболее затратны операции со списком при использовании insert - сложность (как минимум) - O(n^2).
    Заполнение словаря - сложность так же линейная, но требуются операции с ключами и значениями. 
"""
