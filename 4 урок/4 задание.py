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

from collections import Counter
def func_3():
    count = Counter(array)
    b = max(count.values())
    c = {k:v for k, v in count.items() if v == b}
    s = list(c.keys())
    v = list(c.values())
    return f'Чаще всего встречается число {s[0]}, ' \
           f'оно появилось в массиве {v[0]} раз(а)'

print(f'{func_1()} и заняло времени: {timeit("func_1()", setup = "from __main__ import func_1", number = 100000)}')
print(f'{func_2()} и заняло времени: {timeit("func_2()", setup = "from __main__ import func_2", number = 100000)}')
print(f'{func_3()} и заняло времени: {timeit("func_3()", setup = "from __main__ import func_3", number = 100000)}')

# Исходя из данных замеров мы видим, что самая быстрая функция первая.
# У меня к сожалению не получилось сделать функцию более быстрой, а только наоборот мое решение более сложное