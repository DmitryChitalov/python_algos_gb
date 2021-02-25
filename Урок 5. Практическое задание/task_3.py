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

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit

list_with_range = [el for el in range(10000)]
deque_with_range = deque()
deque_with_range.extend(list_with_range)


def list_append(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def deque_append(num):
    my_list = deque()
    for i in range(num):
        my_list.append(i)


def list_appendleft(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def deque_appendleft(num):
    my_list = deque()
    for i in range(num):
        my_list.appendleft(i)


def list_extend(lst_range):
    my_list = []
    my_list.extend(lst_range)


def deque_extend(lst_range):
    my_list = deque()
    my_list.extend(lst_range)


def list_extendleft(lst_range):
    my_list = []
    for el in lst_range:
        my_list.insert(0, el)


def deque_extendleft(lst_range):
    my_list = deque()
    my_list.extendleft(lst_range)


def list_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def deque_pop(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop()


def list_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.pop(0)


def deque_popleft(lst_range):
    for i in range(len(lst_range)):
        a = lst_range.popleft()


def list_reverse(lst_range):
    a = lst_range.reverse()


def deque_reverse(lst_range):
    a = lst_range.reverse()


name_list = 'list_append deque_append list_appendleft deque_appendleft' \
            ' list_extend deque_extend list_extendleft deque_extendleft ' \
            'list_pop deque_pop list_popleft deque_popleft ' \
            'list_reverse deque_reverse'.split()

# Для чистоты эксперимента, если в функцию подается список,
# то для deque будет подаваться deque список, для list соотвественно list

num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id <= 3:
        print(
            f"{func_name} -",
            timeit(stmt=func_name + f'(1000)',
                   number=num_time,
                   globals=globals()))
    else:
        if id % 2 == 0:
            print(
                f"{func_name}(list_with_range.copy()) -",
                timeit(stmt=func_name + f'({list_with_range})',
                       number=num_time,
                       globals=globals()))
        else:
            print(
                f"{func_name}(deque_with_range.copy()) -",
                timeit(stmt=func_name + f'({deque_with_range})',
                       number=num_time,
                       globals=globals()))

'''
Добавление элемента - примерно одинаково для list и deque
list_append - 0.49652428200000004
deque_append - 0.463914013

Добавление в начало deque делает быстрее list
list_appendleft - 1.97609362
deque_appendleft - 0.455118508

Добавление списка элементов быстрее у списка 
list_extend(list_with_range.copy()) - 0.7476620669999998
deque_extend(deque_with_range.copy()) - 1.6898748569999995

Добавление слева deque делает значительно быстрее
list_extendleft(list_with_range.copy()) - 163.697030988
deque_extendleft(deque_with_range.copy()) - 1.677079469000006

Извлечение элемента примерно за одно время
list_pop(list_with_range.copy()) - 4.969085119999988
deque_pop(deque_with_range.copy()) - 5.061069882999988

ИЗвлечение элемента слева у deque гораздо быстрее
list_popleft(list_with_range.copy()) - 75.79563973200001
deque_popleft(deque_with_range.copy()) - 4.7595127789999765

Переворот у списка быстрее
list_reverse(list_with_range.copy()) - 0.5832129479999821
deque_reverse(deque_with_range.copy()) - 1.3740138690000094

deque лучше делает все операции слева
Обычные операции со списком отрабатывают примерно за одинаковое время

Операции, где нужен быстрый доступ ( реверс), на списке работают быстрее 
'''