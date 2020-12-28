"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit


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
    count = max([array.count(i), i] for i in array)
    return f'Чаще всего встречается число {count[1]} ,' \
           f'оно появилось в массиве {count[0]} раз(а)'


def func_4():
    max_count = 0
    max_el = 0
    for el in array:
        count = 0
        try:
            for i in range(len(array)):
                array.remove(el)
                count += 1
        except ValueError:
            continue
        finally: # Вот когда бы пригодилось, однако без этого на массиве из одинаковых элементов
            # был не корректный результат
            if max_count == 0 or count >= max_count :
                max_count = count
                max_el = el
    return f'Чаще всего встречается число {max_el} ,' \
           f'оно появилось в массиве {max_count} раз(а)'


if __name__ == '__main__':
    # array = [1, 1, 1, 1]
    array = [1, 3, 5, 1, 3, 4, 5, 1]
    print(func_1())
    print(func_2())
    print(
        timeit(
            'func_1()',
            setup='from __main__ import func_1, array',
            number=10000))
    print(
        timeit(
            'func_2()',
            setup='from __main__ import func_2, array',
            number=10000))
    """
    0.015032399999999994
    0.0198502

    """
    print(func_3())
    print(
        timeit(
            'func_3()',
            setup='from __main__ import func_3, array',
            number=10000))
    """
    пока что-то не быстрее даже второго варианта, но и понятно, почти тоже самое + создаем вложеные списки
    0.0173557
    0.022491300000000006
    0.026707399999999992
    """
    print(func_4())
    print(
        timeit(
            'func_4()',
            setup='from __main__ import func_4, array',
            number=10000))
"""
0.017265500000000003
0.022855700000000007
0.0265253
0.004078999999999999
четвертый вариант оказался быстрее на порядок потому что не смотря на вложеный цикл, вместо квадратичного и линейного 
(как в первых трех вариантах) используется логарифмический алгоритм - длинна массива с каждой итерацией уменьшается
третья версия была проходная, но в четвертой получилось существенно ускориться.
"""