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


def time_it(fun):
    def control(*arg, **kwargs):
        start_time = time.time()
        fun(arg[0])
        print(time.time() - start_time)
    return control


@time_it
def test_list(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
        list_obj.index(i)
    return list_obj


@time_it
def test_dict(n):
    dict_obj = {}
    for i in range(n):
        dict_obj[i] = i
        dict_obj.get(i)
    return test_dict


def timeit_fill():
    """Тестирование заполнения списка и словаря"""
    print(timeit.timeit('[i for i in range(100)]'))
    print(timeit.timeit('{i: i for i in range(100)}'))


# timeit_fill()
test_list(100000)
test_dict(100000)
