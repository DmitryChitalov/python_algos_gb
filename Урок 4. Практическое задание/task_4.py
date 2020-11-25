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


def bech_func(func):
    action = f"{func.__name__}()"
    setup = f"from __main__ import {func.__name__}"
    number = 10000
    return timeit(action, setup, number=number, globals=globals())


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
    num_set = set(array)
    elem = max([[array.count(x), x] for x in num_set])
    return f'Чаще всего встречается число {elem[1]}, ' \
           f'оно появилось в массиве {elem[0]} раз(а)'


def main():
    pass
    try:
        print(func_1())
        print(func_2())
        print(func_3())
        print(bech_func(func_1))
        print(bech_func(func_2))
        print("Мой вариант")
        print(bech_func(func_3))
        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
0.011214403999474598
0.014229111999156885
Мой вариант
0.012922896999953082

Удалось сделать вариант второй по скорости. Функция set - создало множество с уникальными значениями из списка. 
Но приведение списка к уникальным значениям тоже занимает время.
"""