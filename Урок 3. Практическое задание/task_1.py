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
from functools import wraps


class SomeList:
    def __init__(self):
        self.some_list = []

    def _stopwatch(func):
        @wraps(func)
        def wrapper(*args):
            start_val = time.time()
            func(*args)
            end_val = time.time()
            return print(f'Операция заняла: {end_val - start_val:.10f} сек')
        return wrapper

    @_stopwatch
    def list_generator(self, m):
        self.some_list = [i for i in range(m)]
        return self.some_list

    @_stopwatch
    def sum_elem_list_1(self):
        result = 0
        for i in self.some_list:
            result += i
        print(f'Сумма элементов списка = {result}')
        return result

    @_stopwatch
    def sum_elem_list_2(self):
        result = sum(self.some_list)
        print(f'Сумма элементов списка = {result}')
        return result


list_1 = SomeList()
list_2 = SomeList()
list_3 = SomeList()

list_1.list_generator(1000000)
list_2.list_generator(1000000)
list_3.list_generator(1000000)
# Время программного заполнения списка всегда разное.
# ВЫВОД: написанное выше еще раз подтверждает тот факт, что на скорость выполнения операции влияет множество факторов:
# загрузка компьютера, работа интерпритатора

list_1.sum_elem_list_1()
list_1.sum_elem_list_2()
# Реализовал 2 метода суммирования элементов:
# первый - при помощи цикла ( O(n) ),
# второй - встроенный метод "sum" ( O(1) ),
# в итоге встроенный метод работает гораздо быстрее.
# ВЫВОД: В большинстве случаев встроенные функции работают гораздо быстрее "новых велосипедов", т.к. разработчики языка
# уже за нас поработали над оптимизацией работы данных функций.
print()


class SomeDict:
    def __init__(self):
        self.some_dict = dict()

    def _stopwatch(func):
        @wraps(func)
        def wrapper(*args):
            start_val = time.time()
            func(*args)
            end_val = time.time()
            return print(f'Операция заняла: {end_val - start_val:.10f} сек')
        return wrapper

    @_stopwatch
    def dict_generator(self, n):
        self.some_dict = {x: x for x in range(n)}
        return self.some_dict

    @_stopwatch
    def sum_dict_item_1(self):
        result = 0
        for v in self.some_dict.values():
            result += v
        print(f'Сумма значений словаря = {result}')
        return result

    @_stopwatch
    def sum_dict_item_2(self):
        result = sum(self.some_dict.values())
        print(f'Сумма значений словаря = {result}')
        return result


dict_1 = SomeDict()

dict_1.dict_generator(1000000)
dict_1.dict_generator(1000000)
dict_1.dict_generator(1000000)
# Как и в случае генерации словаря мы получаем всегда разное время выполнения.
# Однако при тех же равных, словарь заполняется дольше примерно в 2 раза, из-за того, что генератору словаря,
# приходится генерировать в 2 раза больше объектов (key и value).
# ВЫВОД: написанное выше еще раз подтверждает тот факт, что на скорость выполнения операции влияет множество факторов:
# загрузка компьютера, работа интерпритатора. Заполнение словаря дольше заполнения списка при одинаковых вводных данных.

dict_1.sum_dict_item_1()
dict_1.sum_dict_item_2()
# Как и в случае со списком, реализовал 2 метода суммирования элементов:
# первый - при помощи цикла ( O(n) ),
# второй - встроенный метод "sum" ( O(1) ),
# в итоге встроенный метод работает гораздо быстрее.
# ВЫВОД: В большинстве случаев встроенные функции работают гораздо быстрее "новых велосипедов", т.к. разработчики языка
# уже за нас поработали над оптимизацией работы данных функций.
