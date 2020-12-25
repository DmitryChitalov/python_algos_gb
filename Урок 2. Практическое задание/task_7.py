"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# вот честно, решил бы так, ну самое лучше решее, но через рекурсию ниже
def tree(n):
    first = [el for el in range(n)]
    second = n * (n + 1) / 2
    return first == second


def task_7(n, first=0, second=1):
    if first == second:
        print(f'Равно: {first}, {second}')
    elif first < second:
        task_7(n, first + 1, n * (n + 1) / 2)


task_7(3)
