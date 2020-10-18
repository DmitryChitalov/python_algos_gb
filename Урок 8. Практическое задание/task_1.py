"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter, deque
from timeit import timeit


def rec_convert_to_tree(my_deque, first_el=()) -> {}:
    """ Рекурсивная конвертация дека в древо """
    if len(my_deque) < 1:
        return first_el[0]
    else:
        if first_el:
            for i in range(len(my_deque)):
                if first_el[1] <= my_deque[i][1]:
                    my_deque.insert(i, first_el)
                    break
            else:
                my_deque.insert(i+1, first_el)

        first_el, second_el = my_deque.popleft(), my_deque.popleft()
        union_el = ({0: first_el[0], 1: second_el[0]}, first_el[1] + second_el[1])
    return rec_convert_to_tree(my_deque, union_el)


def rec_coding(tree, code=''):
    """ Рекурсивное создание словаря кодировок """
    if type(tree) == str:
        code_dict[tree] = code
    else:
        rec_coding(tree[0], code=f'{code}0')
        rec_coding(tree[1], code=f'{code}1')


def haffman(str_obj):
    """ кодирование строки "по Хаффману" """
    el_count = Counter(str_obj)  # аналог {x: string.count(x) for x in set(string)}
    # -> Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})

    sorted_el_by_count = deque(sorted(el_count.items(), key=lambda item: item[1]))
    # -> deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
    del el_count
    tree = rec_convert_to_tree(sorted_el_by_count)
    # -> {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    del sorted_el_by_count
    rec_coding(tree)
    del tree


def my_def():
    haffman(my_string)
    print(*(code_dict[i] for i in my_string))  # -> 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001


code_dict = {}
my_string = "beep boop beer!"


print(timeit("my_def()", setup="from __main__ import my_def", number=1_000))

""" За исключением функции rec_coding код написан самостоятельно. 
    Профилировка времени показала результат быстрее чем пример с урока 
"""