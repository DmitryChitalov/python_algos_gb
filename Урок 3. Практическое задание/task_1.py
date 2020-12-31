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

my_dict = {}
my_list = []


def timer(func):
    def inner(*args, **kwargs):
        start_val = time.time()
        print(func(*args, **kwargs))
        end_val = time.time()
        print(f'Время составило: {(end_val - start_val)*1000} * 10^(-3)')

    return inner


@timer
def get_dict(my_dict=my_dict, val=input('Введите значение: ')):
    for key in range(1, 4):
        my_dict[key] = val
    return my_dict


@timer
def get_list(my_list=my_list, val=input('Введите значение: ')):
    for i in range(1, 4):
        my_list.append(val)
    return my_list


@timer
def func_dict():
    del my_dict[3]
    return my_dict


@timer
def func_list():
    del my_list[2]
    return my_list


if __name__ == '__main__':
    get_dict()
    get_list()
    print('\n')
    func_dict()
    func_list()

## По результатам видно, что время заполнения списка и операций над ним быстрее приблизительно в 3 раза. Это свидетельствует о том, что чтобы наполнить словарь нужно больше времени, так как словарь является хеш-таблицей, где для ключей необходима генерация хеша.