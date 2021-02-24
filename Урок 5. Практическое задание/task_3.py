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
from timeit import timeit

my_list = [el for el in range(20000)]
my_deque = deque(my_list)
lists='wee'

# добавление  элемент в конец списка и дека
def list_append():

    my_list.append('elem')


def deque_append():
    my_deque.append('elem')


# добавление элементa в начало списка и дека.
def list_appendleft(lst):
    for el in list(lst):
        my_list.insert(0, el)
    # print(my_list)


def deque_appendleft(list):
    my_deque.appendleft(list)


# Удаление элемента с конца списка и дека

def list_pop():
    my_list.pop()

def deque_pop():
    my_deque.pop()

# Удаление элемента с начала списка и дека

def list_popleft(lst):
    lst = lst[1:]

def deque_popleft():
    my_deque.popleft()


numbers = 50000
print('Добавление в список через append: ',
      timeit("list_append()",globals=globals(), number=numbers))
print('Добавление в дек через append: ',
      timeit("deque_append()", globals=globals(), number=numbers))
print('Добавление в начало списка appendleft(insert): ',
      timeit("list_appendleft(lists)",globals=globals(), number=numbers))
print('Добавление в начало дека через appendleft: ',
      timeit("deque_appendleft(lists)", globals=globals(), number=numbers))
print('Удаление из списка pop: ',
      timeit("list_pop()", globals=globals(), number=numbers))
print('Удаление из дека pop: ',
      timeit("deque_pop()", globals=globals(), number=numbers))
print('Удаление с начала списка popleft: ',
      timeit("list_popleft(my_list)", globals=globals(), number=numbers))
print('Удаление с начала дека popleft: ',
      timeit("deque_popleft()", globals=globals(), number=numbers))

"""
Добавление в список через append:  0.008982155999999991
Добавление в дек через append:  0.007240936000000003
Добавление в начало списка appendleft(insert):  21.04990703
Добавление в начало дека через appendleft:  0.006994322000000608
Удаление из списка pop:  0.006247231999999769
Удаление из дека pop:  0.00686632299999701
Удаление с начала списка popleft:  72.417216709
Удаление с начала дека popleft:  0.006763923000008276

Во всех случаях операци с деком быстрее чем со списком
"""