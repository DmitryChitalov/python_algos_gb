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
from timeit import timeit
from collections import deque


def append_left_list(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def append_left_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.appendleft(i)


def append_right_list(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def append_right_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.append(i)


def pop_left_list(my_list):
    for i in range(len(my_list)):
        my_list.pop(0)


def pop_left_deque(my_deque):
    for i in range(len(my_deque)):
        my_deque.popleft()


def pop_right_list(my_list):
    for i in range(len(my_list)):
        my_list.pop()


def pop_right_deque(my_deque):
    for i in range(len(my_deque)):
        my_deque.pop()


num = 10000

my_list1 = [el for el in range(num)]
my_deque1 = deque(my_list1)

print(f"append_left_list({num}): ",
      timeit(f"append_left_list({num})", globals=globals(), number=1000))
print(f"append_left_deque({num}): ",
      timeit(f"append_left_deque({num})", globals=globals(), number=1000))
print()
print(f"append_right_list({num}): ",
      timeit(f"append_right_list({num})", globals=globals(), number=1000))
print(f"append_right_deque({num}): ",
      timeit(f"append_right_deque({num})", globals=globals(), number=1000))
print()
my_list2 = my_list1.copy()
my_deque2 = my_deque1.copy()
print("pop_left_list(my_list2): ",
      timeit("pop_left_list(my_list2)", globals=globals(), number=1000))
print("pop_left_deque(my_deque2): ",
      timeit("pop_left_deque(my_deque2)", globals=globals(), number=1000))
print()
my_list3 = my_list1.copy()
my_deque3 = my_deque1.copy()
print("pop_right_list(my_list3): ",
      timeit("pop_right_list(my_list3)", globals=globals(), number=1000))
print("pop_right_deque(my_deque3): ",
      timeit("pop_right_deque(my_deque3)", globals=globals(), number=1000))
print()
print("my_list1.reverse(): ",
      timeit("my_list1.reverse()", globals=globals(), number=1000))
print("my_deque1.reverse(): ",
      timeit("my_deque1.reverse()", globals=globals(), number=1000))

'''
Измерения проводились на списках и деках длиной 10000.
Проверено 5 операций: добавление/удаление в оба конца и переворот.

append_left_list(10000):  39.8171607
append_left_deque(10000):  1.7753530999999967

append_right_list(10000):  1.8371027000000026
append_right_deque(10000):  1.7885080999999943

pop_left_list(my_list2):  0.0190011000000041
pop_left_deque(my_deque2):  0.0026367999999976632

pop_right_list(my_list3):  0.0027949999999989927
pop_right_deque(my_deque3):  0.0026791000000017107

my_list1.reverse():  0.007236000000006015
my_deque1.reverse():  0.010166600000005133

Выводы:
Больше всего дек выигрывает при добавлении слева.
Удаление слева дек тоже выполняет быстрее.

При добавлении и удалении справа результаты очень близки и находятся в пределах 
погрешности измерения.

Переворот лист выполняет быстрее.

Дек, однозначно, стоит использовать, если планируется множественное 
добавление/удаление в начале списка.
'''
