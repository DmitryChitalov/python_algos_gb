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

sample_list = []
sample_dict = {}


def timing(func):
    import time

    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@timing
def fill_list(n):
    i = 0
    while i < n:
        sample_list.insert(0, i)
        i += 1
    return sample_list


@timing
def fill_dict(n):
    key = 0
    while key < n:
        sample_dict[key] = 1
        key += 1
    return sample_dict


fill_list(100000)
fill_dict(100000)

