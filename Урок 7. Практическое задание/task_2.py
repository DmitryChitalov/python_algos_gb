"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random



def get_arr(l):
    # return [random.randint(0, 50) for i in range(l)]
    return [random.uniform(0,50) for i in range(l)]

def my_sort(arr):
    if len(arr) >= 2:
        delimiter = len(arr) // 2
        left = my_sort(arr[:delimiter])
        right = my_sort(arr[delimiter:])
        return merger(left, right)
    else:
        return arr[:]

def merger(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
        # if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result






if __name__ == '__main__':
    test_arr = get_arr(10)
    print(test_arr)
    print(my_sort(test_arr))