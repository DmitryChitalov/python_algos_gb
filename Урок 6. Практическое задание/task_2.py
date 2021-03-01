"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
"""
1. Подсчета квадратов всех чисел в диапозоне до 100000000
1.1 При помощи вызова функции, которая добавляет каждый новый результат в список и возвращает этот список
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   116     21.1 MiB     21.1 MiB           1   @profile
   117                                         def square():
   118     21.1 MiB      0.0 MiB           1       m1 = memory_usage()
   119    699.9 MiB    678.8 MiB           1       cubes = check_even(range(100000000))
Использовано 1218.00390625 Mb памяти.

1.2 Тот же самый функционал, но с использованием генератора.
Использовано 0.0078125 Mb памяти. 
Превосходство очевидно! На ~ 10**5 порядков. 

Несколько способов описаны в 1ой задаче.


2. Использование внешних файлов и построчное чтение и запись вместо создания списков и словарей в памяти.
2.1 Построчное чтение, фильтрация и непосредственная запись необходимых данных в файл.
    Readline_writeline: Использовано 1.08984375 Mb памяти.
    Используется библиотека csv:

Readline_writeline: Использовано 1.15625 Mb памяти.
    
2.2 Используется регулярные выражения.
    Read_write_re: Использовано 0.05859375 Mb памяти.

Read_write_re: Использовано 0.01171875 Mb памяти.  Меня удивил данный результат. 
Получается, что регулярные выражения расходуют память эффективнее.

2.3 Возьмем одну десятую оригинального файла (7000 строк) и считаем его целиком. 
    Запишем в список и отфильтруем этот список. Подходящие строки внесем в новый список. 
    Из отфильтрованного списка перенесем строки в файл.
    Использовано 2.62109375 Mb памяти.
    Т.е. для сравнения полученное число надо еще умножить на 10.
    Итого порядка 26.2109375 Mb


"""


import csv
import re
from memory_profiler import profile
from memory_profiler import memory_usage


@profile
def readline_writeline(file_name: str):
    """
        Считываем построчно файл и записываем новый уже отфильтрованный.
        Я сформирую списко товаров для "IT"
    """
    try:
        m1 = memory_usage()
        with open(file_name, "r", encoding="utf-8") as animal_shop:
            line_counter = 0
            reader = csv.reader(animal_shop)  # csv.reader - генератор
            with open(f"it_{file_name}", "w", encoding='utf-8', newline='') as animal_shop_it:

                for row in reader:
                    if line_counter == 0:
                        animal_shop_it = csv.writer(animal_shop_it,
                                                    delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                        animal_shop_it.writerow(row)
                    if row[6] == 'IT':
                        animal_shop_it.writerow(row)
                    line_counter += 1
        m2 = memory_usage()
        print(f"Readline_writeline: Использовано {m2[0] - m1[0]} Mb памяти.")
    except IOError:
        print("Проверьте наличие файла")
        exit()

@profile
def read_write_re(file_name: str):
    """
        Считываем построчно файл и записываем новый уже отфильтрованный.
        Я сформирую списко товаров для "IT"
    """
    try:
        m1 = memory_usage()
        animal_shop = open(file_name, "r", encoding="utf-8")
        animal_shop_it = open(f"it__{file_name}", "w", encoding='utf-8', newline='')
        line_counter = 0
        for row in animal_shop:
            if line_counter == 0:
                animal_shop_it.write(row)
            if re.search("IT", row) is not None:
                animal_shop_it.write(row)
            line_counter += 1
        animal_shop.close()
        animal_shop_it.close()
        m2 = memory_usage()
        print(f"Read_writeline: Использовано {m2[0] - m1[0]} Mb памяти.")
    except IOError:
        print("Проверьте наличие файла")
        exit()


@profile
def read_write(file_name: str):
    """
        Считываем построчно файл и записываем новый уже отфильтрованный.
        Я сформирую список товаров для "IT"
    """
    data_list = []
    data_list_filtered = []
    try:
        m1 = memory_usage()
        animal_shop = open(file_name, "r", encoding="utf-8")
        line_counter = 0
        here = 0
        data_list.append(animal_shop.read(2097152))
        for row in data_list:
            if line_counter == 0:
                data_list.append(row)
            if re.search("IT", row) is not None:
                data_list_filtered.append(row)
            line_counter += 1
        animal_shop.close()
        animal_shop_it = open(f"it_fragment_{file_name}", "w", encoding='utf-8', newline='')
        for el in data_list_filtered:
            animal_shop_it.write(el)
        animal_shop_it.close()
        m2 = memory_usage()
        print(f"Использовано {m2[0] - m1[0]} Mb памяти.")
    except IOError:
        print("Проверьте наличие файла")
        exit()


def check_even(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num*num)

    return even

@profile
def square():
    m1 = memory_usage()
    check_even(range(100000000))
    m2 = memory_usage()
    print(f"Использовано {m2[0] - m1[0]} Mb памяти.")


# с использованием генераторов:
def check_even_yield(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


# @profile
def square_generators():
    m1 = memory_usage()
    check_even_yield(range(100000000))
    m2 = memory_usage()
    print(f"Использовано {m2[0] - m1[0]} Mb памяти.")


readline_writeline("animal_products.csv")
read_write_re("animal_products.csv")
read_write("animal_products_fragment.csv")
square()
square_generators()
