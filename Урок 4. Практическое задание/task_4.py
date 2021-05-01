"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
from timeit import Timer

array = [1, 3, 1, 3, 4, 5, 1]

# Создадим 3 функцию. В которой цикл будет идти по уникальным значениям списка. А не по всем, и даже тем, которые
# повторяются. При длинных списках это сократит время подсчета. При коротких разница не велика.
def func_3():
    # Создадим свой список с уникальными значениями входного списка
    uniq_array = list(set(array))

    m = 0
    num = 0

    # И проверяем каждое уникальное значение на количество его вхождения в исходном списке.
    for i in uniq_array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

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


t1 = Timer("func_1","from __main__ import func_1")
t2 = Timer("func_2","from __main__ import func_2")
t3 = Timer("func_3","from __main__ import func_3")

print(func_1(),t1.timeit(number=1000000))
print(func_2(),t2.timeit(number=1000000))
print(func_3(),t3.timeit(number=1000000))
