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


def timer(func):
    def wapper(*args):
        start_func = time.time()
        func(*args)
        print(f'{time.time() - start_func} сек.')
    return wapper


@timer
def filling_lst():
    lst = []
    lst.append('index 0')
    lst.append(1)
    lst.append(True)
    lst.append('index 4')
    lst.append(321)
    lst.append(False)
    return print('Время заполнения (6 элементов) списка')


@timer
def filling_dict():
    my_dict = {}
    my_dict['key1'] = 'value 1'
    my_dict['key2'] = 0
    my_dict['key3'] = False
    my_dict['key4'] = 'value 2'
    my_dict['key5'] = 123
    my_dict['key6'] = True
    return print('Время заполнения (6 пар ключ: значение) словаря')


filling_lst()
filling_dict()

# при нескольких итерациях разница во времени не ясна, так как мало элементов. Как мне кажется, у словаря должено быть
# больше времени на заполнение, так как при записи ключ передается хэш-функции и на его преобразование нужно время.
iteration = 100000
lst = []
my_dict = {}


@timer
def filling_lst2():
    n = 0
    while n < iteration:
        n += 1
        lst.append(n)
    return lst, print('Время заполнения списка 100000 элементов')


@timer
def filling_dict2():
    n = 0
    while n < iteration:
        n += 1
        my_dict['key' + str(n)] = n
    return my_dict, print('Время заполнения словаря 100000 пар')


filling_lst2()
filling_dict2()

# на больших величинах так и есть, словарь заполняется дольше.


@timer
def changes_lst(my_lst):
    for i in range(1, int(iteration/2)):
        my_lst.pop(i)
    return lst, print('Удаление половины списка по индексу занимеает')


@timer
def changes_lst2(my_lst):
    for _ in range(1, int(iteration/2)):
        my_lst.pop()
    return print('Удаление половины списка занимеает')


@timer
def changes_dict(dictionary):
    for i in range(1, int(iteration/2)):
        dictionary.pop('key' + str(i))
    return print('Удаление половины словаря по ключу')


@timer
def changes_dict2(dictionary):
    for _ in range(1, int(iteration/2)):
        dictionary.popitem()
    return print('Удаление половины словаря занимеает')


changes_lst(lst)
changes_dict(my_dict)
changes_lst2(lst)
changes_dict2(my_dict)

# Как мы видим удаление по индексу в списке намного дольше, чем удаление по ключу в словаре. Так как
# словарь хедж-таблица. Но при удалении просто последних элементов по времени выигрывает список. Отсюда вывод словарь
# быстрее в любых дествиях с ключом (замена, удаление, поиск). Но в стеках, очереди и деке явно будет лучше список.
