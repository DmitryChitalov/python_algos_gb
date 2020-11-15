"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import timeit

def time_measure(func):
    def executor(*args):
        start = timeit.default_timer()
        return_value = func(*args)
        end = timeit.default_timer()
        print('Время выполнения функции: {:.10f} секунд.'.format(end - start))
        return return_value
    return executor

@time_measure
def add_to_list(el):
    my_list.append(el)
    return my_list

@time_measure
def add_to_dict(el):
    my_dict.update(el)
    return my_dict


my_dict = {}
my_list = []

add_to_list(123456789)
# add_to_list('programmer')
# add_to_list(True)
add_to_dict({'key1': 123456789})
# add_to_dict({'programmer': 'python'})
# add_to_dict({(5, 6, 7, 8): False})

""" Из полученных результатов делаю вывод, что время примерно одинаковое при заполнении словаря и списка различными значениями"""