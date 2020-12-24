"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time
import random


def track_time(func): # декоратор, так декоратор
    def wrapper(n):
        start= time.time()
        r = func(n)
        stop = time.time()
        return stop - start
    return wrapper

@track_time
def full_list(n):
    res_list =[]
    for i in range(n):
        res_list.append((i, random.random()))
    return res_list

@track_time
def full_dict(n):
    res_dict ={}
    for i  in range(n):
        res_dict.update([(i+1,random.random())])
    return res_dict

@track_time
def full_list1(n):
    res_list =[]
    a=random.random()
    for i in range(n):
        res_list.append((i, a))
    return res_list

@track_time
def full_list2(n):
    a=random.random()
    res_list = [ (i,a) for i in range(n)]
    return res_list

@track_time
def full_dict1(n):
    res_dict ={}
    a=random.random()
    for i  in range(n):
        res_dict.update([(i+1,a)])
    return res_dict

@track_time
def full_dict2(n):
    # res_dict ={}
    a=random.random()
    res_dict = { i:a for i in range(n)}
    return res_dict


if __name__== "__main__":
    print(f'{full_list(10000)} список по первому способу')
    print(f'{full_dict(10000)} словарь по первому способу\n')
    # В таком виде у меня словарь собирается сильно дольше, прям иногда в 2 раза. Приэтом да, время плавает
    # возможно дело в рандоме
    print(f'{full_list1(10000)} список по второму способу')
    print(f'{full_list2(10000)} список по второму способу через генератор\n') # вот тут вобще странно, это просто другая
    # форма записи но время разбегается с предыдущим.
    print(f'{full_dict1(10000)} словарь по второму способу')
    print(f'{full_dict2(10000)} словарь по второму способу через генератор') # при прочих равных  на двух десятков
    # замерах этот способ оказался быстрее для словарей. Но системы/корреляции так и нет, или я ее не вижу.
    # Хотя машина не загружена; может как-то приоритет процесса повысить можно?
    # или у меня в в коде ошибка и я задание не понял?


    # а у нас будет про многопоточность?  в этом курсе?