"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit


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
    counter = max(
        i for i in array if array.count(i) == max(map(array.count, array)))
    return f'Чаще всего встречается число {counter}'


print(func_1())
print(func_2())
print(func_3())

print('Замер func_1: ')
print(
    timeit(
        "func_1()",
        globals=globals(),
        number=1000))

print('Замер func_2: ')
print(
    timeit(
        "func_2()",
        globals=globals(),
        number=1000))

print('Замер func_3: ')
print(
    timeit(
        "func_3()",
        globals=globals(),
        number=1000))

"""
уменьшить время исполнения задачи не удалось, в том числе,
прибегая к встроенным
функциям map. Это связано с тем, что map применят передаваемую
ему аргументом функцию ->
к каждому элементу по принципу итератора, тем самым увеличивая время работы.
Наиболее удачным - явлется первое исполнение функции
"""
