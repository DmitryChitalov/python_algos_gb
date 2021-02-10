"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import Timer
from random import randint

array = [randint(0,100) for i in range(100)]
# array = [1, 3, 1, 3, 4, 5, 1]


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
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


print(func_1())
print(func_2())
print(func_3())



t1 = Timer('func_1()', globals=globals())
t2 = Timer('func_2()', globals=globals())
t3 = Timer('func_3()', globals=globals())

print("func_1= ", t1.timeit(number=1000), "milliseconds")
print("func_2= ", t1.timeit(number=1000), "milliseconds")
print("func_3= ", t1.timeit(number=1000), "milliseconds")

'''
-------Тесты--------
test 1: number=1000000
array = [randint(0,100) for i in range(100)]
func_1= 75.25720589999999 milliseconds
func_2= 77.3475411 milliseconds
func_3= 74.069953 milliseconds

test 2: number = 100000
func_1=  7.8521403 milliseconds
func_2=  7.921892000000001 milliseconds
func_3=  7.923491400000001 milliseconds

test 3: number = 1000
func_1=  0.080538 milliseconds
func_2=  0.08084069999999999 milliseconds
func_3=  0.08021629999999999 milliseconds

------Анализ---------
Тесты показывают, что  на больших числах быстрее всего показывает себя использование встроенной 
функции max в func_3. 
max - O(n)
Как она устроена под капотом, я не знаю, опираюсь выводом только на тест.

Первый вариант (func_1) работает быстрее, чем второй вариант (func_2), потому что идет чтение из готового списка.
Мы знаем, что чтение из списка - O(1). Нет вставки и удаления, но есть итерация по массиву O(n), поэтому первая 
функция не намного быстрее второй функции (func_2).
for in - O(n)
append - O(1)

Вторая функция самая медленная, потому что использует создание списка внутри функции, итерацию по списку,добавление
в новый список значений и поиск максимального значения через функцию max.
append(добавление в конец) в list  - O(1) 
for in - O(n)
max  - O(n)

Вывод: 2я функция самая долгая, но это заметно только на большом кол-ве тестов. number= 1 000 000

'''