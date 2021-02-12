"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

from time import time


def timing(func):
    def wrapper(arg1, arg2):
        start_time = time()
        func(arg1, arg2)
        end_time = time()
        ttt = end_time - start_time
        print(f"Время выполнения: {ttt}")
        return ttt
    return wrapper


@timing
def fill_dict(my_dict: dict, num):
    for i in range(num):
        my_dict[i] = i


@timing
def fill_list(my_list: list, num):
    for i in range(num):
        my_list.append(i)


@timing
def get_dict(my_dict, num):
    for idx in my_dict:
        pass


@timing
def get_list(my_list, num):
    for idx in my_list:
        pass


@timing
def get_rand_dict(my_dict, num):
    for i in range(num):
        ttt = my_dict.get(num - i - 1)


@timing
def get_rand_list(my_list, num):
    for i in range(num):
        ttt = my_list[num - i - 1]


N = 10000000
dict1 = {}
print(f"Создаем словарь на {N} записей")
t1 = fill_dict(dict1, N)

list1 = []
print(f"Создаем список на {N} записей")
t2 = fill_list(list1, N)

if t1 > t2:
    print("Словарь создается дольше\n")
else:
    print("Список создается дольше\n")

print(f"Переберем элементы словаря на {N} записей")
t1 = get_dict(dict1, 0)

print(f"Переберем элементы списка на {N} записей")
t2 = get_list(list1, 0)

if t1 > t2:
    print("Словарь перебирается дольше\n")
else:
    print("Список перебирается дольше\n")

print(f"Выберем {N} элементов по ключу из словаря")
t1 = get_rand_dict(dict1, N)

print(f"Выберем {N} элементов по индексу из списка")
t2 = get_rand_list(list1, N)

if t1 > t2:
    print("Из словаря выбирается дольше\n")
else:
    print("Из списка выбирается дольше\n")

print("Создание словаря должно быть дольше, "
      "т.к. по ключам создаются хеши и проверяется уникальность")
print("Перебирается словарь дольше, т.к. структура данных больше и ее сложнее прочитать")
print("Выборка словаря по ключу должна быть быстрее, но в моем примере, "
      "доступ к списку по индексу быстрее почему-то")
