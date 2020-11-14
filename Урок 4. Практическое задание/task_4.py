"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit, repeat, default_timer

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


print(func_1())
print(func_2())
print()

print(timeit('func_1()', setup='from __main__ import func_1', number=10000))
print(timeit('func_2()', setup='from __main__ import func_2', number=10000))
print()

'''
Попытка профилизировать через timeit ниже.
Почему-то через передачу частей функции общее время выполнения не равно времени выполнения через функцию timeit().
'''

setup = '''array = [1, 3, 1, 3, 4, 5, 1]'''

statements_1 = [
    'num=0',
    'm=0',
    '''
m=0
for i in array:
    count = array.count(i)
    if count > m:
        m = count
        num = i
'''
]


statements_2 = [
    'new_array = []'
    '''
new_array = []
for el in array:
    count2 = array.count(el)
    new_array.append(count2)
max_2 = max(new_array)
elem = array[new_array.index(max_2)]''',
    'count2 = array.count(0)',
    '''
new_array = []
new_array.append(0)''',
]

print('Профилирование func_1 при помощи timeit:')
for st in statements_1:
    print(repeat(st, setup, default_timer, 3, 10000))
print()

print('Профилирование func_2 при помощи timeit:')
for st in statements_2:
    print(repeat(st, setup, default_timer, 3, 10000))
print()


# Третий, оптимизированный с помощью мемоизации, алгоритм:


def memorize(func):
    def wrapper(i=0, mem={}):
        result = mem.get(i)
        if result is None:
            result = func(i)
            mem[i] = result
        return result

    return wrapper


@memorize
def func_3(i=0, nums_dict={}):
    if i < len(array):
        if nums_dict.get(array[i]) is None:
            nums_dict[array[i]] = 1
        else:
            nums_dict[array[i]] += 1
        return func_3(i + 1)
    else:
        max_count, max_num = 0, 0
        for k in nums_dict.keys():
            if nums_dict[k] > max_count:
                max_count = nums_dict[k]
                max_num = k
        return f'Чаще всего встречается число {max_num}, ' \
               f'оно появилось в массиве {max_count} раз(а)'


print(func_3())
print(f'\nВремя выполнения func_3:')
print(timeit('func_3()', setup='from __main__ import func_3', number=10000))
