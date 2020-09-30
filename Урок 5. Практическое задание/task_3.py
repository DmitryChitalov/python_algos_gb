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
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   
   100000    0.080    0.000    2.894    0.000 task_3.py:17(list_create)
   100000    0.566    0.000    3.361    0.000 task_3.py:21(deque_create)
   
   100000    0.039    0.000    0.054    0.000 task_3.py:25(list_append)
   100000    0.032    0.000    0.045    0.000 task_3.py:30(deque_append)
   
   100000    0.031    0.000    0.075    0.000 task_3.py:35(list_insert_into_beginning)
   100000    0.030    0.000    0.043    0.000 task_3.py:40(deque_insert_into_beginning)
   
   100000    0.032    0.000    0.046    0.000 task_3.py:45(list_pop)
   100000    0.032    0.000    0.046    0.000 task_3.py:49(deque_pop)
   
   100000    0.030    0.000    0.054    0.000 task_3.py:53(list_pop_from_beginning)
   100000    0.030    0.000    0.043    0.000 task_3.py:57(deque_pop_from_beginning)
   
   100000    0.030    0.000    0.058    0.000 task_3.py:61(list_insert_into_middle)
   100000    0.031    0.000    0.100    0.000 task_3.py:66(deque_insert_into_middle)
   
   100000    0.018    0.000    0.018    0.000 task_3.py:71(list_get)
   100000    0.019    0.000    0.019    0.000 task_3.py:75(deque_get)
   
операция                -   кто быстрее
создание                -   список 
добавление в конец      -   очередь
добавление в начало     -   очередь
удаление из конца       -   одинаково
удаление из начала      -   очередь
добавление в средину    -   список
получение из средины    -   список

Вывод:
При операциях добавление и удаление в начале и конце используем очередь.
При операциях с "i" элементами импользуем список
"""
import cProfile
from collections import deque


def list_create():
    return [x for x in range(1000)]


def deque_create():
    return deque([x for x in range(1000)])


def list_append(my_list_in):
    my_list_in.append('value')
    return my_list_in


def deque_append(my_deque_in):
    my_deque_in.append('value')
    return my_deque_in


def list_insert_into_beginning(my_list_in):
    my_list_in.insert(0, '500')
    return my_list_in


def deque_insert_into_beginning(my_deque_in):
    my_deque_in.appendleft('500')
    return my_deque_in


def list_pop(my_list_in):
    return my_list_in.pop()


def deque_pop(my_deque_in):
    return my_deque_in.pop()


def list_pop_from_beginning(my_list_in):
    return my_list_in.pop(0)


def deque_pop_from_beginning(my_deque_in):
    return my_deque_in.popleft()


def list_insert_into_middle(my_list_in):
    my_list_in.insert(500, '500')
    return my_list_in


def deque_insert_into_middle(my_deque_in):
    my_deque_in.insert(500, '500')
    return my_deque_in


def list_get(my_list_in):
    return my_list_in[500]


def deque_get(my_deque_in):
    return my_deque_in[500]


def main():
    for _ in range(100000):
        x = list_create()
        y = deque_create()
        list_append(x)
        deque_append(y)
        list_pop(x)
        deque_pop(y)
        list_insert_into_beginning(x)
        deque_insert_into_beginning(y)
        list_pop_from_beginning(x)
        deque_pop_from_beginning(y)
        list_insert_into_middle(x)
        deque_insert_into_middle(y)
        list_get(x)
        deque_get(y)


if __name__ == '__main__':
    cProfile.run('main()')
