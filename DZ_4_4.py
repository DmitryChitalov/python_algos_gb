"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


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
    num = array[0]
    max_frq = 1
    for i in range(len(array) - 1):
        frq = 1
        for k in range(i + 1, len(array)):
            if array[i] == array[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = array[i]
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {max_frq} раз(а)'


def func_4():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


elapsed_func_1 = (timeit.timeit("func_1()",
                                setup="from __main__ import func_1",
                                number=100000)) * 10
elapsed_func_2 = (timeit.timeit("func_2()",
                                setup="from __main__ import func_2",
                                number=100000)) * 10
elapsed_func_3 = (timeit.timeit("func_3()",
                                setup="from __main__ import func_3",
                                number=100000)) * 10
elapsed_func_4 = (timeit.timeit("func_4()",
                                setup="from __main__ import func_4",
                                number=100000)) * 10
print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(f"Время с циклом func_1 - {elapsed_func_1}")
print(f"Время с циклом func_2 - {elapsed_func_2}")
print(f"Время с циклом в цикле func_3 - {elapsed_func_3}")
print(f"Время с функцией в одну строку max func_4 - {elapsed_func_4}")

# -----------------------------ВЫВОДЫ------------------------------------
# Ну вообщем я потратил на эту задачу около 3 часов, пытаясь найти что то
# быстрее чем func_1. В интернете самый простой и быстрый способ считается
# вариант в одну строку func_4. НО! По какой-то причине у меня замер идёт
# дольше чем с циклом func_1. Может я что то неправильно замеряю!?
