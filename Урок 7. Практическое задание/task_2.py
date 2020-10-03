"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
"""
<<<<<<< HEAD
Вывод с увеличением размера массива время сортировки быстро растет,
это сортировка проигрывает функции sorted() при любых размерах массива.

Замер при 100 вызовах массив 5 эл.
  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  900/100    0.001    0.000    0.003    0.000 task_2.py:66(merge_sort)
  
Замер при 1000 вызовах массив 5 эл.
  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
9000/1000    0.010    0.000    0.026    0.000 task_2.py:65(merge_sort)

Замер при 100 вызовах массив 100 эл.
   ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
19900/100    0.017    0.000    0.066    0.001 task_2.py:69(merge_sort)

Замер при 1000 вызовах массив 100 эл.
     ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
199000/1000    0.165    0.000    0.657    0.001 task_2.py:72(merge_sort)

Замер при 100 вызовах массив 1000 эл.
    ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
199900/100    0.176    0.000    0.836    0.008 task_2.py:82(merge_sort)

Замер при 1000 вызовах массив 1000 эл.
     ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
1999000/1000    1.637    0.000    8.050    0.008 task_2.py:82(merge_sort)

##################################################################################
Замер при 1000 вызовах массив 1000 эл. функцией sorted()
     ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
     1000    0.001    0.000    0.105    0.000 task_2.py:91(sort_st)
  
  ################################################################################################
=======
>>>>>>> lesson_7
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
9000/1000    0.009    0.000    0.025    0.000 task_2.py:49(merge_sort)
     1000    0.000    0.000    0.001    0.000 task_2.py:58(sort_st)
     
<<<<<<< HEAD
Я сравнил сортировку слиянием с функцией sorted(), встроенная функция быстрее многократно.
"""
import cProfile
import random
=======
Я сравнил сортировку слиянием с функцией sorted(), встроенная функция быстрее много кратно.
"""
import cProfile
>>>>>>> lesson_7


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def sort_st(list_num):
    return sorted(list_num)


<<<<<<< HEAD
def create_list() -> list:
    return [random.uniform(0, 50) for x in range(1000)]


=======
>>>>>>> lesson_7
def main():
    for _ in range(1000):
        random_list_of_nums = [46.11436617832828, 41.62921998361278, 18.45859540989644,
                               12.128870723745806, 8.025098788570562]
<<<<<<< HEAD
        second_list = create_list()
        print(second_list)
        print(random_list_of_nums)
        print(merge_sort(random_list_of_nums.copy()))
        print(merge_sort(second_list.copy()))
        print(sort_st(random_list_of_nums.copy()))
        print(sort_st(second_list.copy()))
=======
        print(random_list_of_nums)
        print(merge_sort(random_list_of_nums.copy()))
        print(sort_st(random_list_of_nums.copy()))
>>>>>>> lesson_7


# main()
cProfile.run('main()')
