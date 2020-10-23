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
############################ Итог ###################################
По проведенным замерам можно увидеть что обычная вставка элемента в конец списка заметно быстрее выполняется в дэке, 
вставка в начало списка немного быстрее чем вставка в листе insert(0,x), 
иногда время равно но в среднем все таки дэк быстрее,
удаление(remove) на много быстрее через дэк, а удаление первого элемента через popleft и pop(0) приблезительно 
одинаковое время затрачивают, но все же дэк немного быстрее
В общем, дэк отлично економит время работы с массивами

"""

import random
from timeit import repeat


arr = [random.randint(2, 100) for i in range(100) if i % 2 == 0]
copy_arr = arr.copy()

# ##############################################################
# ##### вставка в список через дэк #####
# ##### вставка в конец списка(дэка) #####
stmt1 = """
from collections import deque

append_deque1 = deque()
for i in copy_arr:
		append_deque1.append(i)
"""
# ##### вставка в начало списка #####
stmt1_2 = """
from collections import deque

append_deque2 = deque()
for i in copy_arr:
	append_deque2.appendleft(i)
	"""
# ##### удаление из дэка(remove) #####
stmt3 = """
from collections import deque
deq_arr = deque(copy_arr)
for i in copy_arr:
	deq_arr.remove(i)
	"""
# ##### удаление из дэка(.popleft())#####
stmt4 = """
from collections import deque
deq_arr = deque(copy_arr)
for i in copy_arr:
	deq_arr.popleft()
	"""

# ####################################################################################################
# ##### вставка в список(list) #####
# ##### вставка в конец списка #####
stmt2 = """
append_list1 = list()
for i in copy_arr:
	append_list1.append(i)
"""
# ##### ставка в начало списка #####
stmt2_2 = """
append_list2 = list()
for i in copy_arr:
	append_list2.insert(0, i)
	"""
# ##### удаление из списка #####
stmt2_3 = """
list_arr = copy_arr.copy()
for i in copy_arr:
	list_arr.remove(i)
	"""
stmt2_4 = """
list_arr = copy_arr.copy()
for i in copy_arr:
	list_arr.pop(0)
	"""

print("_"*100)
print("list append: ", repeat(stmt2, 'from __main__ import copy_arr', repeat=4,  number=10000))
print("deque append: ", repeat(stmt1, 'from __main__ import copy_arr', repeat=4, number=10000))
print("_"*100)
print("list insert: ", repeat(stmt2_2, 'from __main__ import copy_arr', repeat=4, number=10000))
print("deque appendleft: ", repeat(stmt1_2, 'from __main__ import copy_arr', repeat=4, number=10000))
print("_"*100)
print("remove from deque: ", repeat(stmt3, 'from __main__ import copy_arr', repeat=4, number=10000))
print("remove from list: ", repeat(stmt2_3, 'from __main__ import copy_arr', repeat=4, number=10000))
print("_"*100)
print("popleft() from deque: ", repeat(stmt4, 'from __main__ import copy_arr', repeat=4, number=10000))
print("pop() first el from list: ", repeat(stmt2_4, 'from __main__ import copy_arr', repeat=4, number=10000))
print("_"*100)

