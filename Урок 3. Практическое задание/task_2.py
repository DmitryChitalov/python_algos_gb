"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib

my_hash_list = []  # Список с хешами.


def get_reg():
    """
В функции производится "регистрация пользователя", вводится логин и пароль. Логин затем используется при
хешировании в качестве "соли". Хеш помещяется в список 'хеш-таблицу'.
    :return: возращает функция список 'хеш-таблицу'.
    """
    print('-Введите логин и пароль или зарегестрируйтесь-')
    login = input('Введите логин :')
    password = input('Введите пароль : ')
    solt = login
    hash_pass = hashlib.sha256(password.encode() + solt.encode()).hexdigest()
    my_hash_list.append(hash_pass)
    return my_hash_listimport time


def time_of_function(function):
    """
Функция - декоратор, принимает на входе функцию, время работы которой измеряет.
Печатает время работы обрабатываемой фунции.
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        res_time = start_time - time.perf_counter()
        print(f'Функция работает {res_time} c.')
        return res

    return wrapped


@time_of_function
def gen_list(x):
    '''
    Функция принимае x, размер списка, проверяет есть такое значение или нет и еслин, то добавляет уникальное значение.
    Здесь они все уникальные,с просто чтобы проверить работу списка и в поиске тоже.
    :return: возвращает сгенерированный список
    '''
    my_list = []
    for el in range(x):
        if el in my_list:
            continue
        else:
            my_list.append(el)
    print('Работа по созданию списка.')
    return my_list


@time_of_function
def gen_dict(x):
    '''
       Функция принимае x, размер словаря и значение ключа, проверяет есть такое значение или нет и еслин,
       то добавляет уникальное значение.
       Здесь они все уникальные,с просто чтобы проверить работу списка и в поиске тоже.
       :return: возвращает сгенерированный словарь.
       '''
    my_dict = {}
    for key in range(x):
        if key in my_dict:
            continue
        else:
            my_dict = {str(x): x + 12 }
    print('Работа по созданию словаря.')
    return my_dict





gen_dict(9999)

print()

gen_list(9999)import time


def time_of_function(function):
    """
Функция - декоратор, принимает на входе функцию, время работы которой измеряет.
Печатает время работы обрабатываемой фунции.
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        res_time = start_time - time.perf_counter()
        print(f'Функция работает {res_time} c.')
        return res

    return wrapped


@time_of_function
def gen_list(x):
    '''
    Функция принимае x, размер списка, проверяет есть такое значение или нет и еслин, то добавляет уникальное значение.
    Здесь они все уникальные,с просто чтобы проверить работу списка и в поиске тоже.
    :return: возвращает сгенерированный список
    '''
    my_list = []
    for el in range(x):
        if el in my_list:
            continue
        else:
            my_list.append(el)
    print('Работа по созданию списка.')
    return my_list


@time_of_function
def gen_dict(x):
    '''
       Функция принимае x, размер словаря и значение ключа, проверяет есть такое значение или нет и еслин,
       то добавляет уникальное значение.
       Здесь они все уникальные,с просто чтобы проверить работу списка и в поиске тоже.
       :return: возвращает сгенерированный словарь.
       '''
    my_dict = {}
    for key in range(x):
        if key in my_dict:
            continue
        else:
            my_dict = {str(x): x + 12 }
    print('Работа по созданию словаря.')
    return my_dict





gen_dict(9999)

print()

gen_list(9999)import time


def time_of_function(function):
    """
Функция - декоратор, принимает на входе функцию, время работы которой измеряет.
Печатает время работы обрабатываемой фунции.
    """
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        res_time = start_time - time.perf_counter()
        print(f'Функция работает {res_time} c.')
        return res

    return wrapped


@time_of_function
def gen_list(x):
    '''
    Функция принимае x, размер списка, проверяет есть такое значение или нет и еслин, то добавляет уникальное значение.
    Здесь они все уникальные,с просто чтобы проверить работу списка и в поиске тоже.
    :return: возвращает сгенерированный список
    '''
    my_list = []
    for el in range(x):
        if el in my_list:
            continue
        else:
            my_list.append(el)
    print('Работа по созданию списка.')
    return my_list


@time_of_function
def gen_dict(x):
    '''
       Функция принимае x, размер словаря и значение ключа, проверяет есть такое значение или нет и еслин,
       то добавляет уникальное значение.
       Здесь они все уникальные,с просто чтобы проверить работу списка и в поиске тоже.
       :return: возвращает сгенерированный словарь.
       '''
    my_dict = {}
    for key in range(x):
        if key in my_dict:
            continue
        else:
            my_dict = {str(x): x + 12 }
    print('Работа по созданию словаря.')
    return my_dict





gen_dict(9999)

print()

gen_list(9999)


def verification():
    """
    Здесь производится "вход в программу", запрашивается пара логин и пароль. Логин затем используется при
    хешировании в качестве "соли". Хеш сверяется со списком 'хеш-таблицей'. В случае совпадения "пароль верный",
    если нет, перенаправляется на 'регистрацию'.
    :return:
    """
    login = input('Введите логин :')
    check_password = input('Введите пароль : ')
    solt = login
    check_password = hashlib.sha256(check_password.encode() + solt.encode()).hexdigest()

    if check_password in my_hash_list:
        print('Пароль верный')
    else:
        print('Пароль не верный.')
        get_reg()


get_reg()

print(my_hash_list[-1])  # Выводится последний внесенный в список хеш.

verification()