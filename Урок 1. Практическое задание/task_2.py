"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
import random


##################################################################
def cmp_digs(a, b):
    if (a > b):
        return False
    return True


##################################################################
def algorithm_1(i_arr, i_max_point):
    final_result = i_max_point
    for counter in range(len(i_arr)):
        print(i_arr[counter])
        if not cmp_digs(final_result, i_arr[counter]):
            final_result = i_arr[counter]
    return final_result


##################################################################
def algorithm_2(i_arr, i_max_point):
    final_result = i_max_point
    for counter in range(len(i_arr)):
        if final_result > i_arr[counter]:
            final_result = i_arr[counter]
    return final_result


# main ##############################################################
max_point = 100000
arr = random.sample(range(max_point * -1, max_point), 7)
print('algorithm_1 = ' + str(algorithm_1(arr, max_point)))
print('algorithm_2 = ' + str(algorithm_2(arr, max_point)))

##################################################################
