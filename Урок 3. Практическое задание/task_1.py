"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте функциию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        func(args[0])
        end = time.time()
        print(f'[***] Время выполнения: {end - start} секунд.')

    return wrapper


@benchmark
def append_and_sorted_my_list(n):
    my_list = [i for i in range(1, n)]
    my_list.reverse()
    # print(my_list)


@benchmark
def append_and_sorted_my_dict(n):
    my_dict = {a: 100 + a for a in range(n)}
    sorted(my_dict.items(), key=lambda kv: kv[1])
    # print(my_dict)


append_and_sorted_my_list(10000000)
append_and_sorted_my_dict(10000000)
# [***] Время выполнения: 0.47553086280822754 секунд. - список, создание и сортировка у списка быстрее
# [***] Время выполнения: 2.922943353652954 секунд. - словарь
