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
    def __init__(self, string):
        self.code = self.compute_code(self.get_tree(string))

    def encode(self, string):
        res = ''
        for symbol in string:
            res += self.code[symbol]
        return res

    def decode(self, string):
        res = ''
        i = 0
        while i < len(string):
            for el in self.code:
                if string[i:].find(self.code[el]) == 0:
                    res += el
                    i += len(self.code[el])
        return res

    def get_code(self):
        return self.code

    @classmethod
    def compute_code(cls, root, codes=dict(), code=''):
        if root is None:
            return
        if isinstance(root.value, str):
            codes[root.value] = code
            return codes
        cls.compute_code(root.left, codes, code + '0')
        cls.compute_code(root.right, codes, code + '1')
        return codes

    @staticmethod
    def get_tree(string):
        string_count = Counter(string)
        if len(string_count) <= 1:
            node = Node(None)
            if len(string_count) == 1:
                node.left = Node([key for key in string_count][0])
                node.right = Node(None)
            string_count = {node: 1}
        while len(string_count) != 1:
            node = Node(None)
            tail = string_count.most_common()[:-3:-1]
            if isinstance(tail[0][0], str):
                node.left = Node(tail[0][0])
            else:
                node.left = tail[0][0]
            if isinstance(tail[1][0], str):
                node.right = Node(tail[1][0])
            else:
                node.right = tail[1][0]
            del string_count[tail[0][0]]
            del string_count[tail[1][0]]
            string_count[node] = tail[0][1] + tail[1][1]
        return [key for key in string_count][0]


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


my_string = input('Введите строку для сжатия: ')
haffman = Haffman(my_string)
print(f'Шифр: {haffman.get_code()}')

encoded_str = haffman.encode(my_string)
print('Сжатая строка: ', encoded_str)

decoded_str = haffman.decode(encoded_str)
print('Исходная строка: ', decoded_str)

if my_string == decoded_str:
    print('Успешно!')
else:
    print('Ошибка!')
