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

def deque_append(deque):
    deque.append('arrr')
    return deque

def deque_appendleft(deque):
    deque.appendleft('arrr')
    return deque

def deque_clear(deque):
    deque.clear()
    return deque

def deque_count(deque):
    return deque.count("3")


def deque_extend(deque,list):
    deque.extend(list)
    return deque


def deque_extendleft(deque,list):
    deque.extendleft(list)
    return deque

def deque_pop(deque):
    deque.pop()
    return deque

def deque_popleft(deque):
    deque.popleft()
    return deque

def deque_remove(deque):
    deque.remove(3)
    return deque

def deque_reverse(deque):
    deque.reverse()
    return deque


def deque_rotate(deque):
    deque.rotate(2)
    return deque

"""Методы list"""

def list_append(list):
    list.append('arrr')
    return list

def list_extend(list):
    list.extend(list)
    return list

def list_insert(list):
    list.insert(1, "rawr")
    return list

def list_remove(list):
    list.remove(3)
    return list

def list_pop(list):
    list.pop(2)
    return list

def list_index(list):
    return list.index(3)

def list_count(list):
    return list.count(2)

def list_reverse(list):
    list.reverse()
    return list

def list_copy(list):
    p = list.copy()
    return p

def list_clear(list):
    list.clear()
    return list


numbers = [1, 2, 3, 4, 5, 6, 3, 5, 3, 6]
deque_number = deque(numbers)



dict_of_deque = {}
dict_of_lists = {}

dict_of_deque["append"] = (timeit('deque_append', setup='from __main__ import deque_append', number=10000000))
dict_of_deque["appendleft"] = (timeit('deque_appendleft', setup='from __main__ import deque_appendleft', number=10000000))
dict_of_deque["count"] = ({timeit('deque_count', setup='from __main__ import deque_count', number=10000000)})
dict_of_deque["extend"] = ({timeit('deque_extend', setup='from __main__ import deque_extend', number=10000000)})
dict_of_deque["extendleft"] = ({timeit('deque_extendleft', setup='from __main__ import deque_extendleft', number=10000000)})
dict_of_deque["pop"] = ({timeit('deque_pop', setup='from __main__ import deque_pop', number=10000000)})
dict_of_deque["popleft"] = ({timeit('deque_popleft', setup='from __main__ import deque_popleft', number=10000000)})
dict_of_deque["remove"] = ({timeit('deque_remove', setup='from __main__ import deque_remove', number=10000000)})
dict_of_deque["reverse"] = ({timeit('deque_reverse', setup='from __main__ import deque_reverse', number=10000000)})
dict_of_deque["clear"] = ({timeit('deque_clear', setup='from __main__ import deque_clear', number=10000000)})


dict_of_lists["append"] = ({timeit('list_append', setup='from __main__ import list_append', number=10000000)})
dict_of_lists["count"] = ({timeit('list_count', setup='from __main__ import list_count', number=10000000)})
dict_of_lists["extend"] = ({timeit('list_extend', setup='from __main__ import list_extend', number=10000000)})
dict_of_lists["pop"] = ({timeit('list_pop', setup='from __main__ import list_pop', number=10000000)})
dict_of_lists["remove"] = ({timeit('list_remove', setup='from __main__ import list_remove', number=10000000)})
dict_of_lists["reverse"] = ({timeit('list_reverse', setup='from __main__ import list_reverse', number=10000000)})
dict_of_lists["clear"] = ({timeit('list_clear', setup='from __main__ import list_clear', number=10000000)})

print(f'Deque: {dict_of_deque}')
print(f'List: {dict_of_lists}')

print("Deque: ")
print(f" rotate: {timeit('deque_rotate', setup='from __main__ import deque_rotate', number=10000000)}")

print("List: ")
print(f" copy: {timeit('list_copy', setup='from __main__ import list_copy', number=10000000)}")

"""Выводы:
Deque более вариативный, чем обычный list. Хотя некоторые его методы более медлительны (например, appendleft). 
Хорош, если нужно воткнуть значение не только в конец, но и в начало. С другой стороны, идентичные с List методы в Deque
выполняются быстрее. 
"""
