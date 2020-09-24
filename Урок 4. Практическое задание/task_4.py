"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
import random as rd


# array = [1, 3, 1, 3, 4, 5, 1]
array = [rd.randint(1, 10) for i in range(100)]


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


def func_3():
    """
    Написанная мной функция func_3() работает в 6-7 раз быстрее предыдущих двух, но только если
    в списоке не содержится много уникальных чисел.
    Объясню подробнее, например если в мы будет передавать список длинной 1000 элементов с числами от 1 до 10,
    то моя функция будет работать быстрее. Ведь мы можем сгенерировать только 10 разных чисел, поэтому множество
    new_array = set(array) будет небольшое и количество вызовов .count() будет оставаться меньше 10-ти.
    Но если передаваемый список длинной 1000 элементов будет содержать числа генерируемые от 1 до 1000, то функция
    будет работать также, а в некоторых случаях и медленнее чем предыдущие.
    """
    m = 0
    num = 0
    # Получаем только уникальные числа.
    new_array = set(array)
    for new_el in new_array:
        count = array.count(new_el)
        if count > m:
            m = count
            num = new_el
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())

result_1 = timeit("func_1()", "from __main__ import func_1", number=1000)
result_2 = timeit("func_2()", "from __main__ import func_2", number=1000)
result_3 = timeit("func_3()", "from __main__ import func_3", number=1000)

print()
print(f'Результат func_1(): {result_1}')
print(f'Результат func_2(): {result_2}')
print(f'Результат func_3(): {result_3}')
