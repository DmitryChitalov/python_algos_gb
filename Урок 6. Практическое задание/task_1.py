"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from pympler import asizeof
# import sys
# from memory_profiler import profile

"""  Пример 1  """

lst = range(100)
#@profile
def add_value(list_obj):
    new_lst = []
    for i in list_obj:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst
print(add_value(lst))            

#@profile
def add_value_2(list_obj):
    gen = (i for i in list_obj if i%2==0)
    return gen

# if __name__ == '__main__':
#     min_value(lst)

# if __name__ == '__main__':
#     min_value_2(lst)

print(asizeof.asizeof((add_value(lst)))) # 2120 bytes
print(asizeof.asizeof((add_value_2(lst)))) # 464 bytes

""" Первая замереная функция min_value(lst) занимает 2120 bytes памяти, более оптимизированная функция min_value_2(lst)
    с использованием генераторного выражения занимает 464 bytes памяти, что в 4 раза меньше, чем использование цикла for, 
    это связано с тем, что генераторное выражение возвращает итератор, по-одному, в момент обращения, а не список. """


""" Пример 2 """

class MyClass_slot(object):
    __slots__ = ['firstname', 'lastname']
    def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
    def name_ret(self):
        return f'{self.firstname} : {self.lastname}'

class MyClass_not_slot(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.firstname = firstname
    def name_ret(self):
        return f'{self.firstname} : {self.lastname}'


print(asizeof.asizeof((MyClass_slot('Mark', 'Avrelii')))) # 168 bytes
print(asizeof.asizeof(MyClass_not_slot('Mark', 'Avrelii'))) # 400 bytes

""" Использование метода __slots__ действительно уменьшает размер хранимых в памяти данных, и это видно по замерам. 
    Это связано с тем, что при вызове атрибута __slots__ словарь __dict__ создаваться не будет, именно за счёт этого 
    и экономится память"""