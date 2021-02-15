# Python 3.8.0 win 64x
# Lesson_4 Task_1 (создание списка четных чисел)

from timeit import timeit
from sys import getsizeof
from pympler import asizeof
from numpy import array


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in nums if i % 2 == 0]


my_lst = [i for i in range(10000)]

# мы уже знаем, что функц_2 выполняется в 2 раза быстрее функц_1, теперь сравним затраты памяти
print('\nfunc_1:')
print(getsizeof(func_1(my_lst)))  # 21516
print(asizeof.asizeof(func_1(my_lst)))  # 101520
print('\nfunc_2:')
print(getsizeof(func_2(my_lst)))  # 21516
print(asizeof.asizeof(func_2(my_lst)))  # 101520


# getsizeof и asizeof показывает одинковый объём памяти при разном времени выолнении  2.455 и 1.09641
# т.к. func_2 быстрее, будем оптимизировать её

# 3. Используйте NumPy
def func_3(nums):
    return array([i for i in nums if i % 2 == 0])


print('\nfunc_3:')
print(getsizeof(func_3(my_lst)))  # 21516 > 20048
print(asizeof.asizeof(func_3(my_lst)))  # 101520 > 20056


# 5. map reduce filter, нам подходит filter
def func_4(num):
    return num % 2 == 0


print('\nfunc_4:')
print(getsizeof(list(filter(func_4, my_lst))))  # 21516 > 20404
print(asizeof.asizeof(list(filter(func_4, my_lst))))  # 101520 > 100408, незначительное уменьшение памяти

# объединим 3 и 4 функции
print('\nfunc_5:')
print(getsizeof(array(list(filter(func_4, my_lst)))))  # 21516  >  20404 > 20048 > 20048
print(asizeof.asizeof(array(list(filter(func_4, my_lst)))))  # 101520 > 100408 > 20056 > 20056
# по памяти итоговый результат по отношению к функ_3 не изменился


# есть предположение, что увеличится скорость выполнения функций
print('\nfunc_1:', timeit("func_1(my_lst)", globals=globals(), number=2000))  # 2.2896826999999997
print('func_2:', timeit("func_2(my_lst)", globals=globals(), number=2000))  # 1.2148656999999998
print('func_3:', timeit("func_3(my_lst)", globals=globals(), number=2000))  # 1.6719293
print('func_4:', timeit("list(filter(func_4, my_lst))", globals=globals(), number=2000))  # 1.8841035999999995
print('func_5:', timeit("array(list(filter(func_4, my_lst)))", globals=globals(), number=2000))  # 2.5027344000000005

""" Выводы:
1. При решении задач необходимо смотреть не только на объём занимаемой памяти, но и на время выполнения функции,
т.к. оптимизация работы по памяти может существенно увеличить время выполения функции
func_5 память 20048 20056 время 2.5027344000000005
func_2 память 21516 101520 время 1.2148656999999998

2. Одинаковый объём занимаемой памяти не значит одинаковое время выполнения функций
func_3 20048 20056 1.6719293
func_5 20048 20056 2.5027344000000005

3. Функция filter даёт несущественную экономию по памяти, но существенную прибавку по времени
func_2 21516 101520 1.2148656999999998
func_4 20404 100408 1.8841035999999995

4. Излишняя оптимизация может не уменьшить объём памяти, но существенно увеличить время работы функции
Если воспользоватьс сразу двумя способами оптимизации filter и numpy array
мы не получим двойную экономию памяти, но получим существенное увеличеине времени
func_3 20048 20056 1.6719293
func_5 20048 20056 2.5027344000000005  что даже дольше рекурсии

Итог:
самой быстрой функцией стала func_2
 21516 101520 1.09641 но и памяти занимает достаточно много

Самой оптимальной по памяти стала func_3 за счет применения модуля numpy array
 20048 20056 1.6574896 с увеличением вреени примерно в 1,5 раза
"""
