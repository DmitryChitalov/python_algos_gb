"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import copy
from memory_profiler import profile
from collections import deque
import random
my_list = list()
deq_obj = deque("")

nums = list(range(10000))
"""
взял код из урока 4. по результатам замера времени выполнения func_2 практически в два раза быстрее. 
в цикле for идет перебор самих элементов списка непосредственно. Но по выделению памяти обе функции работают одинаково
полагаю потому что размер списка одинаковый. Удаление new_arr практически не дает изменений, вероятно потому что сборщик
в обоих случаях его удаляет. Глубокое копирование не тратит много памяти
В случае копирования данных в конец списка, памяти тратится в два раза меньше, чем в список слева. Наверное под капотом
при этом дважды копируется сам список, для сдвига его влево каждый раз при добавлении данных слева. Отметил, что при
увеличении размера списка, память так же тратится больше, что логично
"""


@profile
def func_1(num):
    new_arr = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            new_arr.append(i)
    y = copy.deepcopy(new_arr)
    del new_arr
    return y


@profile
def func_2(num):
    new_arr = []
    for el in num:
        if el % 2 == 0:
            new_arr.append(el)
    y = copy.deepcopy(new_arr)
    return new_arr


@profile
def append_deq():
    for i in range(1000000):
        deq_obj.append(random.randint(0, 1000))


@profile
def append_left_deq():
    for i in range(1000000):
        deq_obj.appendleft(random.randint(0, 1000))


@profile
def append_deq1():
    for i in range(1000):
        deq_obj.append(random.randint(0, 1000))


@profile
def append_left_deq1():
    for i in range(1000):
        deq_obj.appendleft(random.randint(0, 1000))


if __name__ == "__main__":
    func_1(nums)
    func_2(nums)
    append_deq()
    append_left_deq()
    append_deq1()
    append_left_deq1()
