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
from random import randint

list_upto_hund1 = [randint(1, 100) for i in range(100)]
list_upto_th1 = [randint(1, 100) for i in range(1000)]

list_upto_hund2 = [randint(1, 1000) for i in range(100)]
list_upto_th2 = [randint(1, 1000) for i in range(1000)]


def append_list(in_list):
    for val in in_list:
        output_list.append(val)


def append_queue(in_list):
    for val in in_list:
        output_deque.append(val)


def pop_list_item():
    output_list.pop()


def pop_queue_item():
    output_deque.pop()


def get_list_item():
    output = output_list[50]


def get_queue_item():
    output = output_deque[50]


output_list = []
output_deque = deque()
print("Значения до 100")
print("\t\t\t\tlist")
print("timeit функции append_list: "
    f"{timeit(f'append_list({list_upto_hund1})', setup='from __main__ import append_list', number=100000)}")
print("timeit функции pop_list_item: "
    f"{timeit(f'pop_list_item()', setup='from __main__ import pop_list_item', number=100000)}")
print("timeit функции get_list_item: "
    f"{timeit(f'get_list_item()', setup='from __main__ import get_list_item', number=100000)}")
print("\t\t\t\tqueue")
print("timeit функции append_queue: "
    f"{timeit(f'append_queue({list_upto_hund1})', setup='from __main__ import append_queue', number=100000)}")
print("timeit функции pop_queue_item: "
    f"{timeit(f'pop_queue_item()', setup='from __main__ import pop_queue_item', number=100000)}")
print("timeit функции get_queue_item: "
    f"{timeit(f'get_queue_item()', setup='from __main__ import get_queue_item', number=100000)}")
print("\nБольшее число элементов")
print("\t\t\t\tlist")
print("timeit функции append_list: "
    f"{timeit(f'append_list({list_upto_hund2})', setup='from __main__ import append_list', number=100000)}")
print("timeit функции pop_list_item: "
    f"{timeit(f'pop_list_item()', setup='from __main__ import pop_list_item', number=100000)}")
print("timeit функции get_list_item: "
    f"{timeit(f'get_list_item()', setup='from __main__ import get_list_item', number=100000)}")
print("\t\t\t\tqueue")
print("timeit функции append_queue: "
    f"{timeit(f'append_queue({list_upto_hund2})', setup='from __main__ import append_queue', number=100000)}")
print("timeit функции pop_queue_item: "
    f"{timeit(f'pop_queue_item()', setup='from __main__ import pop_queue_item', number=100000)}")
print("timeit функции get_queue_item: "
    f"{timeit(f'get_queue_item()', setup='from __main__ import get_queue_item', number=100000)}")
output_list = []
output_deque = deque()
print("\n\n\nЗначения до 1000")
print("\t\t\t\tlist")
print("timeit функции append_list: "
    f"{timeit(f'append_list({list_upto_th1})', setup='from __main__ import append_list', number=100000)}")
print("timeit функции pop_list_item: "
    f"{timeit(f'pop_list_item()', setup='from __main__ import pop_list_item', number=100000)}")
print("timeit функции get_list_item: "
    f"{timeit(f'get_list_item()', setup='from __main__ import get_list_item', number=100000)}")
print("\t\t\t\tqueue")
print("timeit функции append_queue: "
    f"{timeit(f'append_queue({list_upto_th1})', setup='from __main__ import append_queue', number=100000)}")
print("timeit функции pop_queue_item: "
    f"{timeit(f'pop_queue_item()', setup='from __main__ import pop_queue_item', number=100000)}")
print("timeit функции get_queue_item: "
    f"{timeit(f'get_queue_item()', setup='from __main__ import get_queue_item', number=100000)}")
print("\nБольшее число элементов")
print("\t\t\t\tlist")
print("timeit функции append_list: "
    f"{timeit(f'append_list({list_upto_th2})', setup='from __main__ import append_list', number=100000)}")
print("timeit функции pop_list_item: "
    f"{timeit(f'pop_list_item()', setup='from __main__ import pop_list_item', number=100000)}")
print("timeit функции get_list_item: "
    f"{timeit(f'get_list_item()', setup='from __main__ import get_list_item', number=100000)}")
print("\t\t\t\tqueue")
print("timeit функции append_queue: "
    f"{timeit(f'append_queue({list_upto_th2})', setup='from __main__ import append_queue', number=100000)}")
print("timeit функции pop_queue_item: "
    f"{timeit(f'pop_queue_item()', setup='from __main__ import pop_queue_item', number=100000)}")
print("timeit функции get_queue_item: "
    f"{timeit(f'get_queue_item()', setup='from __main__ import get_queue_item', number=100000)}")

# Значения до 100
# 				list
# timeit функции append_list: 1.3685614000000002
# timeit функции pop_list_item: 0.019053399999999998
# timeit функции get_list_item: 0.012942999999999927
# 				queue
# timeit функции append_queue: 0.9300314999999999
# timeit функции pop_queue_item: 0.0162713000000001
# timeit функции get_queue_item: 0.014555499999999721
#
# Большее число элементов
# 				list
# timeit функции append_list: 1.4047172000000003
# timeit функции pop_list_item: 0.02466609999999969
# timeit функции get_list_item: 0.02318409999999993
# 				queue
# timeit функции append_queue: 1.0401719000000003
# timeit функции pop_queue_item: 0.015892599999999923
# timeit функции get_queue_item: 0.024617700000000298
#
#
#
# Значения до 1000
# 				list
# timeit функции append_list: 13.468822999999999
# timeit функции pop_list_item: 0.018161100000000374
# timeit функции get_list_item: 0.012499599999998168
# 				queue
# timeit функции append_queue: 9.843903599999997
# timeit функции pop_queue_item: 0.016239199999997567
# timeit функции get_queue_item: 0.01407689999999917
#
# Большее число элементов
# 				list
# timeit функции append_list: 31.0991185
# timeit функции pop_list_item: 0.02483840000000015
# timeit функции get_list_item: 0.017655900000001168
# 				queue
# timeit функции append_queue: 10.389413400000002
# timeit функции pop_queue_item: 0.016710800000012682
# timeit функции get_queue_item: 0.014487899999991782

# Вывод: по результатам работы можно сделать вывод, что queue однозначно работает лучше для заполнения списка при любом
# раскладе, поп также эффективнее чем для списка, гет +- одинаковый. Доступ к отдельным элементам у списка быстрее, но
# не сильно значительно. При увеличении количества элементов и их размера - гет у списка становится гораздо хуже.
