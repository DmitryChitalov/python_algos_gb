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


def list_append(el_count):
    my_list = []
    for i in range(el_count):
        my_list.append(i)
    return my_list


def list_insert(el_count):
    my_list = []
    for i in range(el_count):
        my_list.insert(0, i)
    return my_list


def deque_append(el_count):
    my_deque = deque()
    for i in range(el_count):
        my_deque.append(i)
    return my_deque


def deque_append_left(el_count):
    my_deque = deque()
    for i in range(el_count):
        my_deque.appendleft(i)
    return my_deque


def bench_list_append(el_count):
    action = f"list_append({el_count})"
    setup = "from __main__ import list_append"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_deque_append(el_count):
    action = f"deque_append({el_count})"
    setup = 'from __main__ import deque_append'
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_list_insert(el_count):
    action = f"list_insert({el_count})"
    setup = "from __main__ import list_insert"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def bench_deque_append_left(el_count):
    action = f"deque_append_left({el_count})"
    setup = "from __main__ import deque_append_left"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


def determinate_fastest(time_list, time_deque, operation, el_count):
    if time_list < time_deque:
        print(
            f"При {operation} на {el_count} list работает быстрее чем deque. \
\ttimelist: {time_list} < timedeque: {time_deque}")
    else:
        print(
            f"При {operation} на {el_count} deque работает быстрее чем list. \
\ttimedeque: {time_deque} < timelist: {time_list}")


def main():
    pass
    try:

        time_list_append_100 = bench_list_append(100)
        time_deque_append_100 = bench_deque_append(100)
        determinate_fastest(time_list_append_100, time_deque_append_100, "append", 100)

        time_list_append_1000 = bench_list_append(1000)
        time_deque_append_1000 = bench_deque_append(1000)
        determinate_fastest(time_list_append_1000, time_deque_append_1000, "append", 1000)

        time_list_append_3000 = bench_list_append(3000)
        time_deque_append_3000 = bench_deque_append(3000)
        determinate_fastest(time_list_append_3000, time_deque_append_3000, "append", 3000)

        time_list_insert_100 = bench_list_insert(100)
        time_deque_append_left_100 = bench_deque_append_left(100)
        determinate_fastest(time_list_insert_100, time_deque_append_left_100, "append_left", 100)

        time_list_insert_1000 = bench_list_insert(1000)
        time_deque_append_left_1000 = bench_deque_append_left(1000)
        determinate_fastest(time_list_insert_1000, time_deque_append_left_1000, "append_left", 1000)

        time_list_insert_3000 = bench_list_insert(3000)
        time_deque_append_left_3000 = bench_deque_append_left(3000)
        determinate_fastest(time_list_insert_3000, time_deque_append_left_3000, "append_left", 3000)

        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
При append на 100 deque работает быстрее чем list. 	timedeque: 0.037638803994923364 < timelist: 0.04685223200067412
При append на 1000 deque работает быстрее чем list. 	timedeque: 0.40373821899993345 < timelist: 0.40387488000123994
При append на 3000 list работает быстрее чем deque. 	timelist: 1.3292514970016782 < timedeque: 1.372686820999661
При append_left на 100 deque работает быстрее чем list. 	timedeque: 0.03774408099707216 < timelist: 0.06639325700234622
При append_left на 1000 deque работает быстрее чем list. 	timedeque: 0.40302266999788117 < timelist: 1.5470125589999952
При append_left на 3000 deque работает быстрее чем list. 	timedeque: 1.4026272550036083 < timelist: 10.463681144996372

Process finished with exit code 0


Вывод при вставке в конец, на малом количестве элементов лучше работает deque, а на больше лучше работает list.
При вставке а начало, deque работает лучше чем list.
"""