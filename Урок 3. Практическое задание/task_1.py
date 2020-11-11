"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time
import random


def time_delta(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper



@time_delta
def dict_update(n, mydict={}):
    for k in range(n):
        mydict[k] = random.randint(0, 100)

    return mydict

@time_delta
def list_update(n, mylist=[]):
    for el in range(n):
        mylist.append(el)

    return mylist



print(dict_update(8))
print(list_update(8))


