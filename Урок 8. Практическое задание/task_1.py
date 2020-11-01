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

from collections import Counter


def wrapper(count_list):
    """
    Обёртка для code_table, что бы переменная не становилась глобальной
    """
    code_table = dict()

    def tree_huffman(huffman_list, path=''):
        """
        3 этап
        по дереву Хафмана формирует словарь расшифровки
        """
        if not isinstance(huffman_list, tuple):
            code_table[huffman_list] = path
        else:
            tree_huffman(huffman_list[0], path=f'{path}0')
            tree_huffman(huffman_list[1], path=f'{path}1')

    tree_huffman(count_list)
    return code_table


def algorithm_huffman(count_list):
    """
    2 этап
    по алгоритму Хафмана формируем дерево(луковицу) из кортежа
    """
    len_list = len(count_list)
    for _ in range(len_list - 1):
        last_elem = count_list.pop()
        penul_elem = count_list.pop()
        sum_elem = last_elem[1] + penul_elem[1]
        # print(last_elem, penul_elem, sum_elem)
        count_list.append((((last_elem[0]), (penul_elem[0])), sum_elem))
        count_list.sort(key=lambda item: item[1], reverse=True)
        # print(count_list)
    return wrapper(count_list[0][0])


def get_arhive(some_str):
    """
    1 этап
    получает строчку и формирует из неё кортеж частоты символов по убыванию
    """
    count_list = Counter(some_str).most_common()
    return algorithm_huffman(count_list)


abr = get_arhive('abracadabra')
beep = get_arhive('beep boop beer!')
print(abr)      # {'a': '0', 'b': '10', 'd': '1100', 'c': '1101', 'r': '111'}
print(beep)     # {'b': '00', ' ': '010', 'p': '011', '!': '1000', 'r': '1001', 'o': '101', 'e': '11'}
