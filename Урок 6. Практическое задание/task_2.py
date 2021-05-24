"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
import sys
from memory_profiler import profile


class BaseOfHumans(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class BaseOfHumansSlots(object):
    __slots__ = ['name', 'age', 'address']

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


@profile(precision=4)
def func_1(name, age, address):
    data = []
    for i in range(100000):
        data.append(BaseOfHumans(name, age, address))
    return data


@profile(precision=4)
def func_2(name, age, address):
    data = []
    for i in range(100000):
        data.append(BaseOfHumansSlots(name, age, address))
    return data


fn1 = func_1("Петя", 32, "Какой-то адрес")
fn2 = func_2("Петя", 32, "Какой-то адрес")
print(sys.getsizeof(fn1), sys.getsizeof(fn2))

"""
Использование модуля itertools уже известно многим (говорили на следующем уроке), я хочу предложить не совсем
фундаментальное, но очень интересное решение, я пойму, если вы не примите это как выполенение задания 2:)

Есть интересная директива __slots__ прописанная в доках по Python, она помогает нам явно объявлять элементы данных
такие как параметры и запрещает использование __dict__ и __weakref__(слабая ссылка) что может существенно сэкономить
память.
На примере видно, что класс с использованием __slots__ во второй функции экономит память почти в 3 раза.
учитывая, что мы имеем список с боллее 100тыс элементов. Но такой подход нельзя использовать, если мы хотим
в дальнейшем добавлять поля в наш список не изменяя класс. У всего есть свои минусы.. 

Вывод без директивы __slots__:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28  20.1680 MiB  20.1680 MiB           1   @profile(precision=4)
    29                                         def func_1(name, age, address):
    30  20.1680 MiB   0.0000 MiB           1       data = []
    31  38.2227 MiB   0.0000 MiB      100001       for p in range(100000):
    32  38.2227 MiB  18.0547 MiB      100000           data.append(BaseOfHumans(name, age, address))
    33  38.2227 MiB   0.0000 MiB           1       return data

Вывод c директивой:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36  38.2344 MiB  38.2344 MiB           1   @profile(precision=4)
    37                                         def func_2(name, age, address):
    38  38.2344 MiB   0.0000 MiB           1       data = []
    39  45.1484 MiB   0.0000 MiB      100001       for p in range(100000):
    40  45.1484 MiB   6.9141 MiB      100000           data.append(BaseOfHumansSlots(name, age, address))
    41  45.1484 MiB   0.0000 MiB           1       return data
    
При этом sys.getsizeof показывает нам одинаковый размер: 
без директивы: 824464
с директивой:  824464
"""
