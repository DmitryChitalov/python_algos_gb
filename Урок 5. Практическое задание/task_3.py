"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует действительности.
"""

from collections import deque
from timeit import timeit


my_usual_lst = ['KarabasBarabas', 84771, 86421, 82764, 8974, None]

my_deq_lst = deque(my_usual_lst)


def add_to_end_usual_lst():
    return my_usual_lst.append('05')


def add_to_end_deq_lst():
    return my_deq_lst.append('05')


print('Insert element to the end of usual list: ',
      timeit('add_to_end_usual_lst()', setup='from __main__ import add_to_end_usual_lst', number=10000))

print('Insert element to the end of deque list: ',
      timeit('add_to_end_deq_lst', setup='from __main__ import add_to_end_deq_lst', number=10000))

'''
Здесь по замерам выходит:
Insert element to the end of usual list:  0.0016631000000000007
Insert element to the end of deque list:  0.00016700000000000048
В данном случае намного быстрее deque
'''


def add_to_start_usual_lst():
    return my_usual_lst.insert(0, '05')


def add_to_start_deq_lst():
    return my_deq_lst.appendleft('05')


print('Insert element to the start of usual list: ',
      timeit('add_to_start_usual_lst', setup='from __main__ import add_to_start_usual_lst', number=10000))

print('Insert element to the start of deque list',
      timeit('add_to_start_deq_lst()', setup='from __main__ import add_to_start_deq_lst', number=10000))


'''
Здесь по замерам выходит:
Insert element to the start of usual list:  0.00016860000000000486
Insert element to the start of deque list 0.0017602000000000034
В данном случае намного быстрее обычный список
'''


def del_elem_usual_lst():
    return my_usual_lst.pop()


def del_elem_deq_lst():
    return my_deq_lst.pop()


print('Delete element from the end of usual list: ',
      timeit('del_elem_usual_lst', setup='from __main__ import del_elem_usual_lst', number=10000))

print('Delete element from the end of deque list: ',
      timeit('del_elem_deq_lst()', setup='from __main__ import del_elem_deq_lst', number=10000))


'''
Здесь по замерам выходит:
Delete element from the end of usual list:  0.00016710000000000336
Delete element from the end of deque list:  0.001484300000000001
В данном случае намного быстрее обычный список
'''


def clear_usual_lst():
    return my_usual_lst.clear()


def clear_deq_lst():
    return my_deq_lst.clear()


print('Clear usual list: ',
      timeit('clear_usual_lst', setup='from __main__ import clear_usual_lst', number=10000))

print('Clear deque list: ',
      timeit('clear_deq_lst()', setup='from __main__ import clear_deq_lst', number=10000))


'''
Здесь по замерам выходит:
Clear usual list:  0.00017730000000000523
Clear deque list:  0.001528599999999998
В данном случае намного быстрее обычный список
'''


'''
Deque показал себя быстрее только в операции добавления элементов в конец списка. Что касается операции добавления 
элемента в начало списка и удаления элемента из списка, то здесь быстрее обычный список. Это довольно странный результат, 
потому что deque и должен быть заточен под операции с началом и концом списков. Что касается сходных встроенных функций
у обоих списков (в данном случае clear), то здесь обычный список выигрывает у deque значительно.   
'''