"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import array
import copy
import numpy as np
from memory_profiler import profile

@profile
def func_1(nums):
    b = copy.deepcopy(nums)
    new_arr = []
    for i in b:
        if i % 2 == 0:
            new_arr.append(i)
    z = copy.deepcopy(new_arr)
    # print(z)
    return z

@profile
def func_1_1(nums):
    b = copy.deepcopy(nums)
    del nums
    new_arr = []
    for i in b:
        if i % 2 == 0:
            new_arr.append(i)
    z = copy.deepcopy(new_arr)
    del i
    del b
    del new_arr
    # print(z)
    return z


@profile
def func_2(nums):
    new_arr = [item for item in range(len(nums)) if nums[item] % 2 == 0]
    z = copy.deepcopy(new_arr)
    # print(z)
    return z

@profile
def func_2_1(nums):
    new_arr = [item for item in range(len(nums)) if nums[item] % 2 == 0]
    z = copy.deepcopy(new_arr)
    del new_arr
    # print(z)
    return z


@profile
def func_2_2(nums):
    new_arr = [item for item in range(0, len(nums), 2)]
    z = copy.deepcopy(new_arr)
    # print(z)
    return z

@profile
def func_2_2_1(nums):
    new_arr = [item for item in range(0, len(nums), 2)]
    z = copy.deepcopy(new_arr)
    del new_arr
    # print(z)
    return z

@profile
def func_voc(nums):
    new_arr = {item : item for item in range(0, len(nums), 2)}
    z = copy.deepcopy(new_arr)
    del new_arr
    # print(z)
    return z

@profile
def func_3(nums):
    new_arr = list(range(0, len(nums), 2))
    z = copy.deepcopy(new_arr)
    # print(z)
    return z

@profile
def func_3_1(nums):
    new_arr = list(range(0, len(nums), 2))
    z = copy.deepcopy(new_arr)
    del new_arr
    # print(z)
    return z

@profile
def func_3_1_numpy(nums):
    new_arr = np.array(range(0, len(nums), 2))
    z = copy.deepcopy(new_arr)
    del new_arr
    # print(z)
    return z

@profile
def func_3_1_array(nums):
    new_arr = array.array('i',range(0, len(nums), 2))
    z = copy.deepcopy(new_arr)
    del new_arr
    # print(z)
    return z


num = list(range(100000))

if __name__ == "__main__":
    func_1(num)
    func_1_1(num)
    func_2(num)
    func_2_1(num)
    func_2_2(num)
    func_2_2_1(num)
    func_3(num)
    func_3_1(num)
    func_voc(num)
    func_3_1_numpy(num)
    func_3_1_array(num)

"""
Задание 1. 
версия Python 3.8
операционная система MacOs Catalina
разрядность вашей Оs 64

Аналитика: (название, начало, завершение)
1) цикл без чистки,26.7,28.3
2) цикл с чисткой,28.3,29.1
3) генератор с условием без чистки,29.1,30.6
4) генератор с условием с чисткой,29.3,26.6
5) генератор без условия без чистки,25.4,26.6
6) генератор без условия с чисткой,25.5,26.6
7) функция без чистки,25.6,26.6
8) функция с чисткой,25.6,26.6
9) генератор словарь с чисткой,25.6,32.9
10) функция numpy с чисткой,31.8,31.8
11) функция array с чисткой,31.8,31,9

вывод: 
1) на примере цикла и генератора с условием заметно, что чистка экономит место.

2) генератор без условия и функция максимально оптимизированы и не увеличивают потребление памяти.
в них чистка роли не играет

3) на примере генерации словаря - использование памяти зависит от объекта

4) сторонние функции также (или более) оптимальны - пример функции numpy и array (попытка захватить задание 2)
"""