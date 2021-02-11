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
Замер осуществлялся при повторении каждой функции по 10000 (number=10000):

при добавлении в конец разница не очень существенная:
append my_list: 0.014190000000000008 seconds
append my_deque: 0.011119400000000002 seconds 

count тяжеловат. Но отработывает практически одинаково, со списком чуточку быстрее. Возможно просто погрешность.
count my_list: 11.3654591 seconds
count my_deque: 12.311739900000001 seconds

при удалении с конца обычный список справляется с этим в 2 раза быстрее: 
pop from my_list: 0.018775100000000003 seconds
pop from my_deque: 0.03429839999999999 seconds

при добавлении в начало (insert(), appendleft()) deque очень сильно выигрывает! Разница на несколько порядков:
appendleft my_list: 1.7119775000000002 seconds
appendleft my_deque: 0.011185400000000012 seconds

при использовании функции remove() список с этим справляется почти в 2 раза эффективнее. 
подтверждение эффективности случайного доступа при работе со списками
remove my_list: 2.872107400000001 seconds
remove my_deque: 4.3159206999999995 seconds

аналогично разница на несколько порядков при удалении начальных pop(idx = 0), popleft() элементов:
popleft from my_list: 1.0097728 seconds
popleft from my_deque: 0.011180600000000318 seconds

Для работы со списком как с очередью, при необходимости записывать и извлекать начальные элементы 
deque сильно выигрывает.

"""
from collections import deque
from timeit import timeit

my_list = list("Let's play with this text.")
my_deque = deque("Let's play with this text.")
print(my_list)
print(my_deque)


#  добавление текста к list в конец.
def list_append(i_text):
    for el in list(i_text):
        my_list.append(el)
    # print(my_list)


#  добавление текста к deque в конец.
def deque_append(i_text):
    for el in list(i_text):
        my_deque.append(el)
    # print(my_deque)


#  удаление текста с конца list.
def list_pop(stop_el):
    for el in list(my_list)[::-1]:
        if el != stop_el:
            my_list.pop()
        else:
            break
    # print(my_list)


#  удаление текста с конца deque.
def deque_pop(stop_el):
    for el in list(my_deque)[::-1]:
        if el != stop_el:
            my_deque.pop()
        else:
            break
    # print(my_deque)


#  добавление текста к list в начало.
def list_appendleft(i_text):
    for el in list(i_text)[::-1]:
        my_list.insert(0, el)
    # print(my_list)


#  добавление текста к deque в начало.
def deque_appendleft(i_text):
    for el in list(i_text)[::-1]:
        my_deque.appendleft(el)
    # print(my_deque)


#  удаление текста с начала list.
def list_popleft(stop_el):
    for el in list(my_list):
        if el != stop_el:
            my_list.pop(0)
        else:
            break
    # print(my_list)


#  удаление текста с начала deque.
def deque_popleft(stop_el):
    for el in list(my_deque):
        if el != stop_el:
            my_deque.popleft()
        else:
            break
    # print(my_deque)


text = " Enjoy!"
print(f"append my_list: {timeit('list_append(text)', globals=globals(), number=10000)} seconds")
print(f"append my_deque: {timeit('deque_append(text)', globals=globals(), number=10000)} seconds")

#  подсчет количества символов '!' в тексте (после 10000 раз выполненного добавления 'Enjoy!' есть что посчитать )) )
text = '!'
print(f"count my_list: {timeit('my_list.count(text)', globals=globals(), number=10000)} seconds")
print(f"count my_deque: {timeit('my_deque.count(text)', globals=globals(), number=10000)} seconds")

text = '.'
print(f"pop from my_list: {timeit('list_pop(text)', globals=globals(), number=10000)} seconds")
print(f"pop from my_deque: {timeit('deque_pop(text)', globals=globals(), number=10000)} seconds")

text = "Hello! "
print(f"appendleft my_list: {timeit('list_appendleft(text)', globals=globals(), number=10000)} seconds")
print(f"appendleft my_deque: {timeit('deque_appendleft(text)', globals=globals(), number=10000)} seconds")

text = "l"
print(f"remove my_list: {timeit('my_list.remove(text)', globals=globals(), number=10000)} seconds")
print(f"remove my_deque: {timeit('my_deque.remove(text)', globals=globals(), number=10000)} seconds")

text = 'L'
print(f"popleft from my_list: {timeit('list_popleft(text)', globals=globals(), number=10000)} seconds")
print(f"popleft from my_deque: {timeit('deque_popleft(text)', globals=globals(), number=10000)} seconds")


