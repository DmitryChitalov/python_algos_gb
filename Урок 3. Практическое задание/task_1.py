"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


"""
Задание 1.
Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time, random

def decor_timing(func):
    def timing(*args, **kwargs):
        start_time=time.time()
        func(*args, **kwargs)
        end_time=time.time()
        return end_time-start_time
    return timing

@decor_timing
def fill_dict(key, elem):
    v_dict[key] = elem
    return

@decor_timing
def fill_list(elem):
    v_list.append(elem)
    return

@decor_timing
def max_dict_el():
    v_max=max(v_dict.values())
    return

@decor_timing
def max_list_el():
    v_max=max(v_list)
    return

def print_result(v_delta, title_str):
    print(f"{title_str} {v_delta}")
    return

print ("ждем окончания расчетов....")
print(("---------------------------"))
v_dict = dict()
v_list = list()
delta_dict=0
delta_list=0
max_el=9999999
for i in range(max_el):
    v_elem=random.random()*100
    delta_list +=fill_list(v_elem)
    delta_dict +=fill_dict(i,v_elem)

print_result(delta_list, "заполнение списка  заняло:")
print_result(delta_dict, "заполнение словаря заняло:")
print("Заполнение словаря дольше списка, саязано с необходимости искать хэш ключа")

# теперь делаем операции со списком и словарем
print("------------------ операции ------------------ ")

print_result(max_list_el(), "поиск максимального значения в списке  заняло:")
print_result(max_dict_el(), "поиск максимального значения в словаре заняло:")

#print(sum_dict_el())
#print(sum_list_el())

"""
n=0
res_list=1
v_time_list.append(time.time())
while n<len(v_list):
    res_list=res_list+v_list[n]
    n+=1
v_time_list.append(time.time())
n=1
res_dict=1
v_time_dict.append(time.time())
while n<len(v_dict)+1:
    res_dict=res_dict+v_dict[n]
    n+=1
v_time_dict.append(time.time())
print_result(delta_dict, "сумма элементов словаря заняла:")
print_result(delta_list, "сумма элементов  списка заняла:")
""" 