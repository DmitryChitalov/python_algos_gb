"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit
from random import randint


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_12():
    # Новая функция
    # Модифицируется 1-я функция, как более быстрая (из двух). Для исключения повторов используется set
    m = 0
    num = 0
    for i in set(array):
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_3():
    # Новая функция
    # Для обработки массива используется словарь. Ключи количество повторов в массиве
    # Для исключения повторов используется set
    new_dict = {(array.count(i)): i for i in set(array)}
    amount = max(new_dict.keys())

    return f'Чаще всего встречается число {new_dict.get(amount)}, ' \
           f'оно появилось в массиве {amount} раз(а)'

def func_4():
    # Новая функция
    m = max(array, key=array.count)
    return f'Чаще всего встречается число {m}, ' \
           f'оно появилось в массиве {array.count(m)} раз(а)'

# array = [1, 3, 1, 3, 4, 5, 1]
# array = [randint(1, 20) for i in range(1000)]
array = [randint(1, 50) for i in range(1000)]

# print(func_1())
# print(func_2())
# print(func_3())
# print(func_4())
"""Первый замер: проход маленький массив, 1 000 000 раз. Время в комментариях 
Второй замер: проход 'случайный' массив 1000 элементов, 1000 раз"""
print("func_1()", timeit.timeit("func_1()", setup="from __main__ import func_1", number=1000))      # 2.8  26.5
print("func_12()", timeit.timeit("func_12()", setup="from __main__ import func_12", number=1000))   # 2.4  0.5
print("func_2()", timeit.timeit("func_2()", setup="from __main__ import func_2", number=1000))      # 3.8  26.9
print("func_3()", timeit.timeit("func_3()", setup="from __main__ import func_3", number=1000))      # 3.4  0.5
print("func_4()", timeit.timeit("func_4()", setup="from __main__ import func_4", number=1000))      # 26.7


"""Использование 'исключения повторов' при помощи set() сокращает время исполнения программы с большими массивами
Использование словаря не увеличивает время исполнения
Первый проход
func_1() 2.7518312
func_12() 2.4734234
func_2() 3.8129836
func_3() 3.514714999999999
func_4() 3.1001267000000006

Второй проход 
func_1() 26.5886584
func_12() 1.3718912000000003
func_2() 26.9914937
func_3() 1.3608831000000023
func_4() 26.793642600000005
"""
