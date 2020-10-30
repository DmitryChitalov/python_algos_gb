"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from datetime import datetime

some_list = []
some_dict = {}
n = 10 ** 5  # число операций


def time_decorator(some_func):
    """Вычисляет время выполения декорируемой функции"""

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} составило {datetime.now() - start}')
        return result

    return wrapper


@time_decorator
def fill_list(lst, num):
    """Заполняет список"""
    for i in range(num):
        # lst.append(i) # Сложность операции O(1). Вставка в конец списка
        lst.insert(0, i)  # Сложность операции O(n) (по документации). Вставка в начало списка


fill_list(some_list, n)
print('_' * 100)


@time_decorator
def fill_dict(dct, num):
    """Заполняет словарь"""
    for i in range(num):
        dct[i] = i


fill_dict(some_dict, n)
print('_' * 100)

"""
Операция заполнения словаря занимает меньше времени, так как он представляет из себя хеш-таблицу и операция 
добавления нового элемента имеет сложность О(1).
Операция добавления элемента в конец списка тоже имеет сложность О(1). Операция добавления в список с использованием
insert имеет сложность O(n).
Поэтому функция fill_dict(dct, num) отрабатывает гораздо быстрее fill_list(lst, num) с использованием insert.
"""


# Операции удаления, получения по индексу и ключу
@time_decorator
def change_list(lst):
    """Выполняет операции по изменению списка"""
    for i in range(1000):  # удаляем 1000 элементов из списка
        lst.pop(i)
    for j in range(1000):
        lst[j] = lst[j + 1]  # изменяем тысячу элементов в списке


change_list(some_list)
print('_' * 100)


@time_decorator
def change_dict(dct):
    """Выполняет операции по изменению словаря"""
    for i in range(1000):
        dct.pop(i)  # удаляем тысячу ключей из словаря
    for j in range(1001, 2002):
        dct[j] = 'fill'  # изменяем тысячу значений в соваре


change_dict(some_dict)
print('_' * 100)

"""
В функции change_list(lst) операции удаления элемента не с конца списка lst.pop(i) выполняются за О(n). Обращение по
индексу с изменением элемента списка выполняется за О(1).
В функции change_dict(some_dict) все операции изменения словаря проходят за время O(1).
Следовательно функция по изменению словаря отрабатывает гораздо быстрее.
"""
