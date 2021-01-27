"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import Timer
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):  # O(n)
        if nums[i] % 2 == 0:  # O(1)
            new_arr.append(i)  # O(1)
    return new_arr


def fun_2(nums):
    new_arr = []
    while len(nums) > 0:
        if nums[-1] % 2 == 0:
            new_arr.append(nums[-1])
            nums.pop()
        elif nums[-1] % 2 != 0:
            nums.pop()
    return new_arr


# num = [1, 2, 3, 4, 5, 6]
num = [randint(0, 100) for i in range(100)]

# print(func_1(num))
# print(fun_2(num))
func_1(num)
fun_2(num)

#
t1 = Timer("func_1(num)", globals=globals())
print("func_1= ", t1.timeit(number=1), "milliseconds")
#
t2 = Timer("fun_2(num)", globals=globals())
print("fun_2=  ", t2.timeit(number=1), "milliseconds")

"""
Анализ:
Ф-я func_1 работает на 0,007 секунд дольше, чем fun_2.
Обе ф-и представляют собой цикл, однако в fun_2 мы не инетируемся по всему массиву,
а всегда берем самый последний элемент, благодаря этому сложность становится O(1),а не O(n).

В list - append() и pop()(для последнего элемента) = O(1) , как и чтение любого элемента в списке.
Т.к мы удаляем всегда только последний элемент, то мы не выходим за сложность O(1) (потому что не итерируемся),
и общая сложность для fun_2 по прежнему остается O(1).
Лучше всего это видно при number = 1 (число повторов теста):
number = 1 (num = [randint(0, 100) for i in range(10000000)])
func_1=  2.4999999999053557e-06 milliseconds
fun_2=   8.000000004670937e-07 milliseconds

number = 1 (num = [randint(0, 100) for i in range(100)])
func_1=  1.1999999999998123e-06 milliseconds
fun_2=   4.999999999987653e-07 milliseconds

Для большого кол-ва тестов разница всегда равна 0.07 либо 0.007 и тд.
number = 1000000 
func_1=  0.17255619999999983 milliseconds
fun_2=   0.10199770000000008 milliseconds

И скорей всего тут все-таки в секундах, а не миллисекундах.

"""
