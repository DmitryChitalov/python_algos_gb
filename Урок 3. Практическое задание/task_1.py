"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

"""В данной задаче измерил время в семи функциях:
Дважды заполнил списки
и дважды заполнил словари (с одними входными данными).
Дважды, т.к. скопировал список и словарь для следующих трех функций, 
в которых получал значение по индексу в списке
и из словаря получал значения по ключу, и значения ключ - значение.

Выводы: т.к. операции append и d[k] = v имеют сложность O(1) - константную, то время заполнения списков и словарей 
у них равно (погрешность при многократном запуске составляла 0,001
 
При получении значений index и get имеют сложность O(1),а у items - O(n), 
но в каждом алгоритме мной применен цикл for - O(n). И как показали замеры items работает 
медленнее (0,032 - 0,046)(иногда до 2-х раз)
Самые быстрые index (0,013 - 0,014) для списка, и get (0,0099 - 0,014) для словарей
Но погрешность между index и get незначительна.
 """


import time
import hashlib

text = 'Python — активно развивающийся язык программирования, новые версии с добавлением/изменением ' \
       'языковых свойств выходят примерно раз в два с половиной года. Язык не подвергался официальной ' \
       'стандартизации, роль стандарта де-факто выполняет CPython, разрабатываемый под контролем автора языка. ' \
       'В настоящий момент Python занимает третье место в рейтинге TIOBE с показателем 10,2 %[16]. ' \
       'Аналитики отмечают, что это самый высокий балл Python за все время его присутствия в рейтинге.'


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(f'Время выполнения функции {function.__name__} {time.time() - start_time}')
        return res

    return wrapped


@time_of_function
def substrings_hash_list(text):
    substrings_hash = []
    for i in text:
        substrings_hash.append(hashlib.sha256(i.encode()).hexdigest())
    i = 1
    text_rev = text[::-1]
    while i < len(text):
        head = text[i:]
        tail = text_rev[i:]
        substrings_hash.append(hashlib.sha256(head.encode()).hexdigest())
        substrings_hash.append(hashlib.sha256(tail[::-1].encode()).hexdigest())
        if tail in text:
            substrings_hash.append(hashlib.sha256(tail.encode()).hexdigest())
        i += 1
    return f'Количество подстрок: {len(set(substrings_hash))}'


substrings_hash_list(text)


@time_of_function
def substrings_hash(text):
    substrings_hash = []
    for i in text:
        substrings_hash.append(hashlib.sha256(i.encode()).hexdigest())
    i = 1
    text_rev = text[::-1]
    while i < len(text):
        head = text[i:]
        tail = text_rev[i:]
        substrings_hash.append(hashlib.sha256(head.encode()).hexdigest())
        substrings_hash.append(hashlib.sha256(tail[::-1].encode()).hexdigest())
        if tail in text:
            substrings_hash.append(hashlib.sha256(tail.encode()).hexdigest())
        i += 1
    return substrings_hash


list_for_index = substrings_hash(text)


@time_of_function
def substrings_hash_dict(text):
    substrings_hash_dict = {}
    for i in text:
        substrings_hash_dict[i] = hashlib.sha256(i.encode()).hexdigest()  # находим все одиночные подстроки
    i = 1
    text_rev = text[::-1]
    while i < len(text):
        head = text[i:]
        tail = text_rev[i:]
        substrings_hash_dict[head] = hashlib.sha256(head.encode()).hexdigest()
        substrings_hash_dict[tail[::-1]] = hashlib.sha256(tail[::-1].encode()).hexdigest()
        if tail in text:
            substrings_hash_dict[tail] = hashlib.sha256(tail.encode()).hexdigest()
        i += 1
    return f'Количество подстрок: {len(substrings_hash_dict)}\n'


substrings_hash_dict(text)


@time_of_function
def substrings_hash_dict(text):
    substrings_hash_dict = {}
    for i in text:
        substrings_hash_dict[i] = hashlib.sha256(i.encode()).hexdigest()  # находим все одиночные подстроки
    i = 1
    text_rev = text[::-1]
    while i < len(text):
        head = text[i:]
        tail = text_rev[i:]
        substrings_hash_dict[head] = hashlib.sha256(head.encode()).hexdigest()
        substrings_hash_dict[tail[::-1]] = hashlib.sha256(tail[::-1].encode()).hexdigest()
        if tail in text:
            substrings_hash_dict[tail] = hashlib.sha256(tail.encode()).hexdigest()
        i += 1
    return substrings_hash_dict


dict_for_get_and_items = substrings_hash_dict(text)


@time_of_function
def time_for_items(dict):
    for k, v in dict.items():
        print(k, v, end='')
        print('\r', end='')


time_for_items(dict_for_get_and_items)


@time_of_function
def time_for_get(dict):
    for i in dict.keys():
        print(dict.get(i), end='')
        print('\r', end='')


time_for_get(dict_for_get_and_items)


@time_of_function
def time_list_index(text):
    for i in range(len(text)):
        print(text[i], end='')
        print('\r', end='')


time_list_index(list_for_index)
