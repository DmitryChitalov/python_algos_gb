"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
def check(alg):
    """
    Декоратор для подсчета времени исполнения алгоритма.
    """
    def check_time(*args):
        import time
        start = time.time()
        res = alg(*args)
        print(f'Время выполнения: {time.time() - start}')
        return res
    return check_time

@check
def filling_for(object, filler):
    """
    Функция заполнения объекта значениями из переданного итерируемого объекта.
    :param object: list/dict
    :param filler: iter
    :return: list/dict
    """
    if type(object) is list:
        for i in filler:
            object.append(i)
    elif type(object) is dict:
        for i in filler:
            object[i] = True
    else:
        print('Переданный объект не может быть обработан.')
    return object

@check
def filling_gen(object, filler):
    """
    Функция заполняет список/словарь с использованием генераторов.
    :param object: list/dict
    :param filler: iter
    :return: list/dict
    """
    if type(object) is list:
        [i for i in filler]
    elif type(object) is dict:
        {i: True for i in filler}
    else:
        print('Переданный объект не может быть обработан.')
    return object

@check
def filling_alt(object, filler):
    """
    Альтернативные методы заполнения списка и словаря.
    :param object: list/dict
    :param filler: iter
    :return: list/dict
    """
    if type(object) is list:
        for i in filler:
            object.insert(i, True)
    elif type(object) is dict:
        object = object.fromkeys(filler, True)
    else:
        print('Переданный объект не может быть обработан.')
    return object

@check
def operate(object, n):
    import random
    object[random.randint(0, n)]
    object[random.randint(0, n)] = False
    del(object[random.randint(0, n)])

if __name__ == '__main__':
    length = 9999
    print('Заполняем список в цикле for...')
    filling_for([], range(length))
    print('Заполняем словарь в цикле for...')
    filling_for({}, range(length))
    print('Используем генератор списка...')
    filling_gen([], range(length))
    print('Используем генератор словаря...')
    filling_gen({}, range(length))
    print('Используем альтернативный метод списка...')
    trial_list = filling_alt([], range(length))
    print('Используем альтернативный метод словаря...')
    trial_dict = filling_alt({}, range(length))
    print('Проверим операции над списком...')
    operate(trial_list, length)
    print('Проверим операции над словарем...')
    operate(trial_dict, length)
"""
Выводы: самый быстрый способ (из представленных) заполнения словаря
сравним по скорости с самым медленным способом заполнения списка. Такая
разница в скорости обусловлена накладными расходами на хеширование,
которые несёт словарь, и которые отсутствуют в списке. В противовес
этому словарь значительно превосходит список в скорости поиска, т.к.
сложность . 
"""