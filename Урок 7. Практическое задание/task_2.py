"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

'''
Разобрался что за метод такой сортировки методом слияния. Он состоит из трех основных моментов. Первое это поделить
список, второе отсортировать поделенные списки, и третье это объеденить все обратно в один список.
Прочитал в интернете что можно делать в 2 направления от общего к частному и наоборот. 
Решил сделать 2 способом разобрал все по 2 элемента (если нечетный то один элемент
ждет окончания сортировки) и потом отсортировал все двухзначные массивы и начал их склеивать. Код получился немного
сложний и витеиватый (нужно делать рефакторинг, и он выполняется медленее по замерам чем код из урока (5000 элементов))
функция преподавателя
0.026293039321899414
моя функция
0.20119905471801758
У меня получилось много вложенных циклов, можно поменять на рекурсию и добавить встроенные функции, 
но я итак на это потратил слишком много времени, главное что суть уяснил, поэтому рефакторить не буду.
'''
import random


def func_decor(f):
    import time

    def control_time(n):
        start_val = time.time()
        f(n)
        end_val = time.time()
        return end_val - start_val

    return control_time


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


# моя сортировка слиянием
# 1 стадия: делим список на элементы по 2
def divide_list(array):
    double_array = [array.pop(), array.pop()]
    return double_array


# 2 стадия сортируем маленькие двухмерные массивы
def sort_func(array):
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]
    return array


# 3 стадия соединяем маленькие массивы в один список
def merge_func(array):
    # создаем вспомогательные элементы
    double_list = []
    sorted_double_list = []
    sorted_array = []
    odd_el = None
    # если длинна списка нечетное число то временно убираем один элемент
    if len(array) % 2 != 0:
        odd_el = array.pop()
    # определяем количество двухзначных подмассивов
    i = len(array) / 2
    # разбиваем исходный список на список из списков двухзначных массивов (1 стадия)
    while i != 0:
        double_list.append(divide_list(array))
        i -= 1
    # сортируем двухзначные массивы (2 стадия)
    for j in double_list:
        sorted_double_list.append(sort_func(j))
    # начинаем заполнения отсортированного списка с последних элементов двухзначного массива
    last_el = sorted_double_list.pop()
    sorted_array.append(last_el[0])
    sorted_array.append(last_el[1])
    # устанавливаем счетчик цикла
    n = i = 0
    while n < len(sorted_double_list):
        # вводим дополнительную переменную для выхода из внутреннего списка
        a = True
        # устанавливаем счетчик элементов для перебора с конца списка
        j = len(sorted_array) - 1
        while a:
            # проверяем если последний элемент проверяемого двухзначного массива меньше или равен первому
            # элементу отсортированного списка значит все два элемента двухзначного массива распологаются
            # в голове отсортированного списка
            if sorted_double_list[i][1] <= sorted_array[0]:
                sorted_array.insert(0, sorted_double_list[i][1])
                sorted_array.insert(0, sorted_double_list[i][0])
                a = False
            else:
                # иначе проверяем если первый элемент больше чем последний элемент отсортированного списка
                # то двухзначный массив встает в хвост отсортированного списка
                if sorted_double_list[i][0] > sorted_array[j]:
                    sorted_array.append(sorted_double_list[i][0])
                    sorted_array.append(sorted_double_list[i][1])
                    a = False
                # иначе проверяем если второй элемент проверяемого двухзначного списка больше чем крайний
                # элемент отсортированого списка то мы его помещаем за этим элементом
                elif sorted_double_list[i][1] > sorted_array[j]:
                    sorted_array.insert(j + 1, sorted_double_list[i][1])
                    # после начинаем перебирать искать где расположить первый элемент двухзначного массива
                    while a:
                        if sorted_double_list[i][0] <= sorted_array[0]:
                            sorted_array.insert(0, sorted_double_list[i][0])
                            a = False
                            break
                        elif sorted_double_list[i][0] > sorted_array[j]:
                            sorted_array.insert(j + 1, sorted_double_list[i][0])
                            a = False
                            break
                        else:
                            j -= 1
                else:
                    j -= 1

        n += 1
        i += 1
    # если количество элементов в исходном списке нечетное число то после сбора отсортированного списка
    # мы ищем куда вставить последний элемент
    if odd_el is not None:
        i = 0
        while i < len(sorted_array):
            if odd_el <= sorted_array[0]:
                sorted_array.insert(0, odd_el)
                break
            elif odd_el >= sorted_array[len(sorted_array) - 1]:
                sorted_array.append(odd_el)
                break
            elif odd_el < sorted_array[i]:
                sorted_array.insert(i, odd_el)
                break
            else:
                i += 1
    return sorted_array


orig_list = [random.randint(0, 50) for _ in range(5000)]
# оригинальный список
# print(orig_list[:])
# список отсортированый моей сортировкой
# print(merge_func(orig_list[:]))

f1 = func_decor(merge_sort)
f2 = func_decor(merge_func)
print('функция преподавателя')
print(f1(orig_list[:]))
print('моя функция')
print(f2(orig_list[:]))
