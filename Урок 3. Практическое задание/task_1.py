"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


def benchmark(func):
    import time

    def wrapper(*args, **kwarg):
        start = time.time()
        func(*args, **kwarg)
        end = time.time()
        print('[*] Execution time: {} sec'.format(end - start))

    return wrapper


@benchmark
def list_add(in_list,  in_key):
    print('List of ' + str(in_key) + ' elements fill')
    for i in range(in_key):
        in_list.append( str(i) )

@benchmark
def dict_add(in_dict, in_key):
    print('Dictionary of ' + str(in_key) + ' elements fill')
    for i in range(in_key):
        in_dict[ i ] = str(i)

@benchmark
def dict_get(in_dict):
    print('Dictionary of ' + str(len(in_dict)) + ' elements retrieve')
    for i in in_dict:
        v_elem = in_dict[ i ]

@benchmark
def list_get(in_list):
    print('List of ' + str(len(in_list)) + ' elements retrieve')
    for i in in_list:
        v_elem = in_list.pop()

v_list = []
v_dict = {}

dict_add(v_dict, 10000000)
list_add(v_list, 10000000)

dict_get(v_dict)
list_get(v_list)

"""
Dictionary of 1000000 elements fill
[*] Execution time: 0.2469193935394287 sec
List of 1000000 elements fill
[*] Execution time: 0.23491907119750977 sec
Dictionary of 1000000 elements retrieve
[*] Execution time: 0.0349888801574707 sec
List of 1000000 elements retrieve
[*] Execution time: 0.03598833084106445 sec
На больших количествах элементов скорость выполнения операций добавления и обращения к элементу различается очень незначительно.
Из этого можно сделать вывод что скорее всего, для внутреннего представление списка и словаря используется один и тот же механизм
"""