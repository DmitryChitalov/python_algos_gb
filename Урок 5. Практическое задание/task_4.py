"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import collections
import time


def time_delta(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper

my_dict = {}
o_dict = collections.OrderedDict()


@time_delta
def fill_in(any_dict):
    for i in range(100):
        any_dict[i] = i*2
        i += 1
    return any_dict


@time_delta
def dict_update(any_dict):
    any_dict.update({'0': '2', '1': '4', '2': '6'})
    return any_dict


@time_delta
def dict_pop(any_dict):
   any_dict.pop('0')
   any_dict.pop('1')
   any_dict.pop('2')
   return any_dict


#print(fill_in(my_dict))
print(dict_update(my_dict))
print(dict_pop(my_dict))
print(fill_in(my_dict))


#print(fill_in(o_dict))
print(dict_update(o_dict))
print(dict_pop(o_dict))
print(fill_in(o_dict))

'''Время выполнения всех функций +- одинаковое, все-таки ordered dict создавался не для улучшения показателей времени
У МЕНЯ ВОПРОС!!!
Первый принт в каждом блоке закомментирован, если его раскомментировать, то ничего не будет работать )))
Я не понимаю почему , тк все функции возвращают словарь, по идее все изменения должны сохраняться в порядке
написания кода '''
