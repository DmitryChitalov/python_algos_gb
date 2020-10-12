"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time
import random

def time_check(func):
    def timech_func(num):
        start_time = time.time()
        func(num)
        end_time = time.time()
        print(end_time - start_time)
        return func(num)
    return timech_func


@time_check
def list_creator(num: int) -> list:
    return [(f'test_key{itr}', itr) for itr in range(0, num)]

data1 = []
data1 = list_creator(3000000) # --> 0.7024750709533691 для миллиона итерация


@time_check
def dict_creator(num: int):
    test_dict = {}
    for itr in range(0, num):
        test_dict[f'test_key{itr}'] = itr
    return test_dict

data2 = dict_creator(3000000) # --> 1.4749236106872559 для миллиона итераций


test_num = random.randint(0, 1000000)
start_time = time.time()
print(data1.index((f'test_key{test_num}', test_num), 0, 1000000))
end_time = time.time()

print(f'Print list result = {end_time - start_time}')

start_time = time.time()
print(data2[f'test_key{test_num}'])
end_time = time.time()

print(f'Print dict result = {end_time - start_time}')
print(type(data1))

"""
Данные функции написаны по единому шаблону, на каждой итерации добавляется по паре значений,
первое в роли ключа, второе в роли значения. Для списка добавление происходит быстрее, однако,
при необходимости поиска и возврата значения список значительно уступает словарю.
Причина такой разницы - хеширование элементов при создании для ускорения поиска. 
"""