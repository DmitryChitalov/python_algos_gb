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


def show_operation_time(func):
    def g(data):
        start = time()
        func(data)
        stop = time()
        print(stop - start)
        return

    return g


start = time()
my_list = [i for i in range(999999)]
stop = time()
print(stop - start)  # 0.06697845458984375
start = time()
my_dict = {f'{i}': i for i in range(999999)}
stop = time()
print(stop - start)  # 0.14095330238342285


start = time()
for i in my_list:
    my_list[i] = 555
stop = time()
print(stop - start)  # 0.07097673416137695

start = time()
for i in my_dict.keys():
    my_dict[i] = 555
stop = time()
print(stop - start)  # 0.20893168449401855


@show_operation_time
def my_list_sort(list):
    sorted(list, reverse=True)
    return


@show_operation_time
def my_dict_sort(dict):
    sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return


my_list_sort(my_list)
my_dict_sort(my_dict)

# По всем операциям время выполнения меньше со списками.
# По причине того, что в словаре используется дополнительно хеш
# это объясняет более долгое создание словаря
# При вводе нового значения хеш так же пересчитывается для элемента хеш таблицы
