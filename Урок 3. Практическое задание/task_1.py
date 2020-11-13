"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import time

def dict_maker(user_dict, max_counter, user_count):
    user_key = random.randrange(0, 100)
    user_val= random.randrange(0, 50)
    if max_counter == user_count:
        print(user_dict)
    else:
        user_dict[user_key] = user_val
        user_count = user_count - 1
        dict_maker(user_dict, max_counter, user_count)


def list_maker(user_list, max_counter, user_count):
    user_numeral = random.randrange(0, 100)
    if max_counter == user_count:
        print(user_list)
    else:
        user_list.append(user_numeral)
        user_count = user_count - 1
        list_maker(user_list, max_counter, user_count)





start_time = time.time()
user_dict = {}
max_counter = 0
user_count = 900
dict_maker(user_dict, max_counter, user_count)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
user_list = []
max_counter = 0
user_count = 900
list_maker(user_list, max_counter, user_count)
end_time = time.time()
print(end_time - start_time)

"""Как я понимаю, модуль учитывает нагрузку цп, ибо иногда функция отрабатывается за 0 секунд,
иногда словарь обрабатывается быстрее, иногда медленнее"""