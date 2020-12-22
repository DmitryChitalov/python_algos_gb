"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

companies = {"First" : 100, "Second": 500, "Third" : 250, "Fourth": 785, "Fifth" : 145, "Sixth": 900}
# 1
def first_algorithm(my_dict : dict):
    my_values = list(my_dict.values())   # O(n)
    my_values.sort()   # O(n * log n)
    result = [] # O(1)
    for key, value in my_dict.items():   # O(n)
        if (my_values[0] == value):  # O(1)
            result.append(key)  # O(1)
        if (my_values[1] == value): # O(1)
            result.append(key)  # O(1)
        if (my_values[2] == value):  # O(1)
            result.append(key)   # O(1)
    return result   # O(1)
print("First algorithm: ", first_algorithm(companies)) #Результирующая сложность O(n * log n)

# 2
def second_algorithm(my_dict : dict):
   sorted_list = sorted(my_dict.values()) # O(1)
   result = []  # O(1)
   for key, value in my_dict.items():  # O(n)
       if (sorted_list[0] == value):  # O(1)
           result.append(key)  # O(1)
       if (sorted_list[1] == value):  # O(1)
           result.append(key)  # O(1)
       if (sorted_list[2] == value):  # O(1)
           result.append(key)  # O(1)
   return result  # O(1)
print("Second algorithm: ", second_algorithm(companies)) #Результирующая сложность O(n), т.к воспользовались встроенной ф-ей sorted(iterable)

# 3
def third_algorithm(my_dict : dict):
   sorted_list = sorted(my_dict.values()) # O(1)
   result = []  # O(1)
   for num in sorted_list[:3]:  # O(n^2)
    for key, val in my_dict.items():
        if (num == val): # O(1)
               result.append(key)
   return result
print("Third algorithm: ", third_algorithm(companies)) #Результирующая сложность O(n^2)

"""Вывод: я считаю что самое не оптимальное - это третье решание, т.к max сложность функции O(n^2)
 а самое лучшее решение - Второе, т.к max сложность равна O(n), вследствие того, что использовали встроенную функцию sorted
 сложность которой равна O(1)."""