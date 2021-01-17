"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
from pympler import asizeof
from random import randint
import numpy as np

""" 1. Задача - определить количество различных подстрок строки S длиной N, состоящая только из строчных 
латинских букв."""

"""Первоначальное решение:"""


@profile
def substring_1(my_string):
    my_dict = {}
    i = 1
    j = 0
    k = 0
    while k <= len(my_string):
        while i <= len(my_string):
            if k < i:
                my_dict[my_string[k:i]] = 1
            i += 1
            j += 1
        i = 1
        k += 1
    dictionary_length = len(my_dict)
    print(dictionary_length)

"""Оптимизированное решение:"""


@profile
def substring_2(my_string):
    my_set = set(my_string)
    i = 1
    j = 0
    k = 0
    while k <= len(my_string):
        while i <= len(my_string):
            if k < i:
                my_set.add(my_string[k:i])
            i += 1
            j += 1
        i = 1
        k += 1
    dictionary_length = len(my_set)
    print(dictionary_length)


substring_1(str('papa'*100))
substring_2(str('papa'*100))

"""
Задача 2. Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
"""

"""
Первоначальное решение:
"""


class UserData:

    def __init__(self, name, login, password, activated: bool):
        self.name = name
        self.login = login
        self.password = password
        self.activated = activated

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def check_activation(self, login):
        if self.activated == True:
            return True
        else:
            return False


def find_user(login):
    if login in userbase.keys():
        return userbase.get(login)
    else:
        return None


def authorization(user_login, user_password):
    user = find_user(user_login)
    if user is None:
        print('Пользователь с таким логином не найден.')
    else:
        if user.check_password(user_password) is False:
            print('Пароль неверный.')
        else:
            if user.check_activation(user_login) is False:
                print('Пожалуйста, активируейте свою учетную запись.')
            else:
                print(f'Добро пожаловать, {find_user(user_login).name}')


sidorsidorov = UserData('Sidor Sidorov', 'sidorsidorov', 'qweasd', True)
userbase = {}
userbase['sidorsidorov'] = sidorsidorov

authorization('sidorsidorov', 'qweasd')
print(asizeof.asizeof(sidorsidorov))

"""
Оптимизированное решение:
"""


class UserData_with_slots:
    __slots__ = ['name', 'login', 'password', 'activated']

    def __init__(self, name, login, password, activated: bool):
        self.name = name
        self.login = login
        self.password = password
        self.activated = activated

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def check_activation(self, login):
        if self.activated == True:
            return True
        else:
            return False


ivanivanov = UserData_with_slots('Ivan Ivanov', 'ivanivanov', 'qwerty', True)
userbase['ivanivanov'] = ivanivanov

authorization('ivanivanov', 'qwerty')
print(asizeof.asizeof(ivanivanov))


"""
Задача 3. Определить число,которое встречается в массиве чаще всего.

Первоначальное решение:

"""


array = [randint(0, 100) for _ in range(1000)]
new_array = []

@profile
def func_1():
    for el in array:
        count1 = array.count(el)
        new_array.append(count1)

    max_1 = max(new_array)
    elem = array[new_array.index(max_1)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_1} раз(а)'


"""
Решение с ипользованием Numpy
"""

np_array = np.array([randint(0, 100) for _ in range(1000)])
new_array_2 = np.array([], int)


@profile
def func_2():
    global new_array_2
    for el in np_array:
        count2 = np.count_nonzero(np_array == el)
        new_array_2 = np.append(new_array_2, count2)

    max_2 = np.max(new_array_2)
    elem_2 = np_array[np.argmax(new_array_2)]
    return f'Чаще всего встречается число {elem_2}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(asizeof.asizeof(array), asizeof.asizeof(new_array))
print(asizeof.asizeof(np_array), asizeof.asizeof(new_array_2))
print(func_1())
print(func_2())



"""
Версия Python 3.9, разрядность ОС - Windows

Задача 1. Для видимого влияния на занимаемый объем памяти строка увеличена в 100 раз. 
Первое решение substring_1 заняло 19.1 MiB, инкремент записи в словарь дал увеливение на 0,2 MiB. 
Во втором рещении substring_2 запись в словарь заменена на запись в set, т.к. ключи в словаре в данном случае не имели
смысла. В результате инвремент запись в множество занимает 0,0 MiB.
Экономия памяти за счет замены словаря на множество.

Задача 2. 
В решении 2 в классе UserData_with_slots добавлена конструкция __slots__, которая позволила уменьшить размер объекта 
класса с 608 до 280.

Задача 3.
В решении 2 исходный список np_array и промежуточный список new_array заменены на массив np.array, 
что позволило уменьшить размер исходного списка с 12080 байт до 4112 байт, при этом размер промежуточного списка
увеличился с 56 байт до 112 байт.
При проверке в профилировщике памяти стало очевидно, что создание промежуточного массива (new_array_2) как 
np.array при помощи функции np.append использует больше памяти, чем функция append для обчного спика (0,2 MiB против
0,0 MiB). Поэтому в данном случае в решении 2 использование массива np.array для промежуточной переменной
не является оптимальным решением. Достаточно ограничиться преобразованием исходного массива.

"""
