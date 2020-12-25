"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import random
import time


def track_time(func):  # декоратор
    def wrapper(n):
        start = time.time()
        r = func(n)
        stop = time.time()
        return stop - start

    return wrapper


def get_dict(n):
    # res_dict ={}
    # a=random.random()
    res_dict = {i: random.random() for i in range(n)}
    return res_dict


def get_list(n):
    # a=random.random()
    res_list = [(i, random.random()) for i in range(n)]
    return res_list


@track_time
def take_ten_randon_from_list1(my_list):
    result_list = []
    n = len(my_list) + 1
    for i in range(100):
        a = random.randint(1, n)
        result_list.append(my_list[a])
    return result_list


@track_time
def take_ten_randon_from_dict1(my_dict):
    result_list = []
    n = len(my_dict) + 1
    # my_dict = get_dict(n)
    for i in range(100):
        result_list.append(my_dict.get(random.randint(1, n)))
    return result_list


def take_ten_randon_from_list2(my_list):
    result_list = []
    start = time.time()
    n = len(my_list) + 1
    for i in range(10):
        a = random.randint(1, n)
        result_list.append(my_list[a])
    stop = time.time()
    return stop - start


def take_ten_randon_from_dict2(my_dict):
    result_list = []
    start = time.time()
    n = len(my_dict) + 1
    # my_dict = get_dict(n)
    for i in range(10):
        result_list.append(my_dict.get(random.randint(1, n)))
    stop = time.time()
    return stop - start


if __name__ == "__main__":
    print(take_ten_randon_from_list1(get_list(10000000)))
    print(take_ten_randon_from_dict1(get_dict(10000000)))
    # и вроде все работает но время по нулям, может у меня декоратор плохо работает...

    print(take_ten_randon_from_list2(get_list(10000000)))
    print(take_ten_randon_from_dict2(get_dict(10000000)))
    # нет, дело не в декораторе...
    # весьма странная штука, идешка прям "думает" пока это выполняется но время по нулям в итоге.
    # Надо будет наставника попытать на эту тему наставника
