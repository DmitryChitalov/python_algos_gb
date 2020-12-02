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


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


# def func_3(arr):
#     max_count = 0
#     el = 0
#     j = 0
#
#     @memoize
#     def recur(j):
#         if j == len(arr):
#             return
#         else:
#             if arr[j] > recur(j + 1):
#                 max_count += 1
#                 el = arr[j]
#             return recur(j)
#
#     recur(j)
#     return f'Чаще всего встречается число {el}, ' \
#            f'оно появилось в массиве {max_count} раз(а)'


print(func_1())
print(func_2())
# print(func_3(array))

print('Результат первой функции - ',
      timeit(
          "func_1()",
          setup='from __main__ import func_1, array',
          number=10000))

print('Результат второй функции - ',
      timeit(
          "func_2()",
          setup='from __main__ import func_2, array',
          number=10000))
