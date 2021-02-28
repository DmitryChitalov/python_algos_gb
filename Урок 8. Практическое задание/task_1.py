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


class Haffman:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_tree(st):
    st_count = Counter(st)

    if len(st_count) <= 1:
        node = Haffman(None)

        if len(st_count) == 1:
            node.left = Haffman([key for key in st_count][0])
            node.right = Haffman(None)

        st_count = {node: 1}

    while len(st_count) != 1:
        node = Haffman(None)
        sptl = st_count.most_common()[:-3:-1]

        if isinstance(sptl[0][0], str):
            node.left = Haffman(sptl[0][0])
        else:
            node.left = sptl[0][0]

        if isinstance(sptl[1][0], str):
            node.right = Haffman(sptl[1][0])
        else:
            node.right = sptl[1][0]

        del st_count[sptl[0][0]]
        del st_count[sptl[1][0]]
        st_count[node] = sptl[0][1] + sptl[1][1]

    return [key for key in st_count][0]


def get_code(root, codes=dict(), code=''):
    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def coding(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


def decoding(string, codes):
    res = ''
    i = 0
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


my_string = input('Введите строку для кодирования: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Кодировка: {codes}')

coding_str = coding(my_string, codes)
print('Закодированная строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)
