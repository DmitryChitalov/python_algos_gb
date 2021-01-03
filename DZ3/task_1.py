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


def froze_time(function):
    def wrapper(*args):
        start_time = time.time()
        function(args[0])
        print(time.time() - start_time)

    return wrapper


@froze_time
def test_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
        my_list.index(i)
#    print(my_list)
    return my_list


@froze_time
def test_dict(n):
    my_dict = dict()
    for i in range(n):
        my_dict[i] = i * 2
        my_dict.get(i)
#    print(dict_obj)
    return my_dict


test_list(2500)
test_dict(2500)
