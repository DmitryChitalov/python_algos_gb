"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def bech_func1(runs_count):
    pass
    action = "func_1(num_list)"
    setup = "from __main__ import func_1"
    excetion_time = timeit(action, setup, number=runs_count, globals=globals())
    return excetion_time


def get_even_index_list(nums):
    pass
    even_index_list = [i for i in range(len(num_list)) if nums[i] % 2 == 0]
    return even_index_list


def bench_func2(runs_count):
    pass
    action = "get_even_index_list(num_list)"
    setup = "from __main__ import get_even_index_list, num_list"
    excetion_time = timeit(action, setup, number=runs_count, globals=globals())
    return excetion_time


def get_even_index_list_insert(nums):
    pass
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.insert(0, i)
    return new_arr


def do_test(int_range, runs_count):
    pass
    global num_list
    num_list = list(range(0, int_range))

    execution_time_func1 = bech_func1(runs_count)
    execution_time_func2 = bench_func2(runs_count)

    print(
        f"""Результаты замеров для поиска индексов элементов четных чисел в списке,
на {len(num_list)} элементов при {runs_count} колличестве последовательных запусков.
простым перебором с добавлением в конец списка  \t{execution_time_func1}
""", end="")
    print(f"перебором с использование генераторных выражений \t{execution_time_func2}")
    print()


def do_my_test():
    pass
    a = list(range(0, 1000))
    b = a
    c = a.append(1)
    print(f" id(a) == id(b)): {a is b}")
    print(f" id(a) == id(c)): {a is c}")


def main():
    pass
    try:
        test_ranges = [10, 100, 1000, 10000]
        runs_count = 1000
        for test_range in test_ranges:
            do_test(test_range, runs_count)
        print("\nПрограмма завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()
    # do_my_test()

"""
Результаты замеров для поиска индексов элементов четных чисел в списке,
на 10 элементов при 1000 колличестве последовательных запусков.
простым перебором с добавлением в конец списка  	0.0009458629974687938
перебором с использование генераторных выражений 	0.000995725000393577

Результаты замеров для поиска индексов элементов четных чисел в списке,
на 100 элементов при 1000 колличестве последовательных запусков.
простым перебором с добавлением в конец списка  	0.007057002003421076
перебором с использование генераторных выражений 	0.005908021998038748

Результаты замеров для поиска индексов элементов четных чисел в списке,
на 1000 элементов при 1000 колличестве последовательных запусков.
простым перебором с добавлением в конец списка  	0.07091732699700515
перебором с использование генераторных выражений 	0.05964205499913078

Результаты замеров для поиска индексов элементов четных чисел в списке,
на 10000 элементов при 1000 колличестве последовательных запусков.
простым перебором с добавлением в конец списка  	0.7032426690020657
перебором с использование генераторных выражений 	0.5862731549968885

Вывод:    
Самый эффективный метод - генераторное выражение, потому как оно выполняется 1 раз, а код внутри нее оптимизируется 
и сразу вернеться готовый список. В данном случае добавление элемента в конец списка происходит на уровне C/C++, и 
перевыделения памяти под переменную там не происходит. Выделяется новая область памяти, и в последнюю ноду списка 
вставляется ссылка на эту новую область. 

Менее эффективный метод данный в примере - это с использованием метода append - добавление в конец списка. 
Выполняя этот код, интерпритатор каждый раз создает новый список, с внесенным изменением 
(добавленным в конец списка элементом). 

"""
