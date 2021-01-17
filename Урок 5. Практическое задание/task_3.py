"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import Timer

first_data = [el for el in range(101)]
second_data = deque([el for el in range(101)])

third_data = [el for el in range(101)]
fourth_data = deque([el for el in range(101)])

fifth_data = [el for el in range(101)]
sixth_data = deque([el for el in range(101)])

seventh_data = [el for el in range(101)]
eighth_data = deque([el for el in range(101)])

ninth_data = [el for el in range(101)]
tenth_data = deque([el for el in range(101)])


# Добавление в начало
def add_left_to_list(data, num):
    data.insert(0, num)
    return data


def add_left_to_deque(data, num):
    data.appendleft(num)
    return data


time_1 = Timer('add_left_to_list(first_data, 777)', 'from __main__ import first_data, add_left_to_list')
print(f'1st Program execution time: {round(time_1.timeit(number=100000), 7)} milliseconds')

time_2 = Timer('add_left_to_deque(second_data, 777)', 'from __main__ import second_data, add_left_to_deque')
print(f'1st Program execution time: {round(time_2.timeit(number=100000), 7)} milliseconds')

'''
Операция с очередью выполняется быстрее операции со списком
'''


# Добавление в конец
def add_right_to_list(data, num):
    data.append(num)
    return data


def add_right_to_deque(data, num):
    data.append(num)
    return data


time_3 = Timer('add_right_to_list(third_data, 777)', 'from __main__ import third_data, add_right_to_list')
print(f'2nd Program execution time: {round(time_3.timeit(number=100000), 7)} milliseconds')

time_4 = Timer('add_right_to_deque(fourth_data, 777)', 'from __main__ import fourth_data, add_right_to_deque')
print(f'2nd Program execution time: {round(time_4.timeit(number=100000), 7)} milliseconds')

'''
Операция с очередью выполняется чуть быстрее операции со списком
'''


# Деление каждого элемента в структуре данных на длину этой структуры
def list_division(data):
    for el in data:
        el / len(data)
    return data


def deque_division(data):
    for el in data:
        el / len(data)
    return data


time_5 = Timer('list_division(fifth_data)', 'from __main__ import fifth_data, list_division')
print(f'3rd Program execution time: {round(time_5.timeit(number=100000), 7)} milliseconds')

time_6 = Timer('deque_division(sixth_data)', 'from __main__ import sixth_data, deque_division')
print(f'3rd Program execution time: {round(time_6.timeit(number=100000), 7)} milliseconds')

'''
Операции выполняются за приблизительно одинаковый промежуток времени
'''


# Реверс структуры данных

def list_reverse(data):
    data.reverse()
    return data


def deque_reverse(data):
    data.reverse()
    return data


time_7 = Timer('list_reverse(seventh_data)', 'from __main__ import seventh_data, list_reverse')
print(f'4th Program execution time: {round(time_7.timeit(number=100000), 7)} milliseconds')

time_8 = Timer('deque_reverse(eighth_data)', 'from __main__ import eighth_data, deque_reverse')
print(f'4th Program execution time: {round(time_8.timeit(number=100000), 7)} milliseconds')

'''
Операция со списком выполняется чуть быстрее операции с очередью
'''


# Перемещение одного элемента с конца очереди в начало

def rotate_list(data):
    data.insert(0, data.pop())
    return data


def rotate_deque(data, num=1):
    data.rotate(num)
    return data


time_9 = Timer('rotate_list(ninth_data)', 'from __main__ import ninth_data, rotate_list')
print(f'5th Program execution time: {round(time_9.timeit(number=100000), 7)} milliseconds')

time_10 = Timer('rotate_deque(tenth_data)', 'from __main__ import tenth_data, rotate_deque')
print(f'5th Program execution time: {round(time_10.timeit(number=100000), 7)} milliseconds')

'''
Операция с очередью выполняется быстрее операции со списком
'''

'''
Вывод: операции, связанные с действиями над элементами (перемещение, удаление, добавление), выполняются быстрее в случае
с очередями по причине асимптотической сложности О(1) для очередей против О(N) для списков.
'''