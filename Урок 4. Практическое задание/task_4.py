"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]
count = Counter(array)


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


def my_f():
    number = max(set(array), key=array.count)
    return number


print(func_1())
print(func_2())
print(my_f())
print(f'Чаще всего встречается число {count.most_common()[0][0]}, '
      f'оно появилось в массиве {count.most_common()[0][1]} раз(а)')

print("func_1")
print(
    timeit(
        'func_1()',
        globals=globals(),
        number=100000))
print("func_2")
print(
    timeit(
        'func_2()',
        globals=globals(),
        number=100000))
print("my_f")
print(
    timeit(
        'my_f()',
        globals=globals(),
        number=100000))
print("counter")
print(
    timeit(
        'count = Counter(array)',
        globals=globals(),
        number=100000))

"""
Самой медленной оказалась func_2 затем func_1 так как там сложность O(N). Самой быстрой по замерам является 
my_f потому что там используются встроенная функция max и множества и я не определял количество сколько раз встречается
число, этого в задании нет написано только определить какие именно число встречается чаще.
Еще я проверил использование Counter из модуля collections его метода most_common он тоже быстрее отработал
чем первые 2 функции.

func_1
0.199444964
func_2
0.22953245899999997
my_f
0.11873128799999999
counter
0.15449868200000005

"""
