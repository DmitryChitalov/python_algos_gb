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


class Crypter:

    def __init__(self, text):
        self.source_text = text
        self.__counter()
        self.__bi_tree()
        self.__haffman_encode()
        self.__text_encode()

    def __counter(self):
        """
        Метод создает очередь с количеством символов в тексте, отсортированную по возрастанию
        """
        self.count_chars = deque(sorted([(k, v) for k, v in Counter(self.source_text).items()], key=lambda x: x[1]))

    def __bi_tree(self):
        """
        Метод создает бинарное дерево
        """
        self.bi_tree = self.count_chars.copy()
        if len(self.bi_tree) > 1:
            while len(self.bi_tree) > 1:
                n1 = self.bi_tree.popleft()
                n2 = self.bi_tree.popleft()
                node = ([n1[0], n2[0]], n1[1] + n2[1])
                for i in range(len(self.bi_tree)):
                    if node[1] > self.bi_tree[i][1]:
                        continue
                    else:
                        self.bi_tree.insert(i, node)
                        break
                else:
                    self.bi_tree.append(node)
        elif len(self.bi_tree) == 1:
            n1 = self.bi_tree.popleft()
            self.bi_tree = deque([([n1[0], ''], n1[1])])
        else:
            self.bi_tree = deque([([], 0)])

    def __haffman_encode(self):
        """
        Метод создает словарь с кодом каждого символа
        """
        def recurs(st, c=''):
            if len(st) == 2:
                recurs(st[0], c + '0')
                recurs(st[1], c + '1')
            else:
                self.encode_table[st] = c
        self.encode_table = {}
        tree = self.bi_tree[0]
        if tree[1] > 0:
            recurs(tree[0])

    def __text_encode(self):
        """
        Метод создает список из закодированных символов текста
        """
        self.encode_text = []
        for c in self.source_text:
            self.encode_text.append(self.encode_table[c])

    def statistic(self):
        """
        Вывод всех значений
        """
        print(f"\nИсходная строка: {self.source_text}")
        print(f"Количество символов: {self.count_chars}")
        print(f"Бинарное дерево: {self.bi_tree}")
        print(f"Таблица кодов: {self.encode_table}")
        print(f"Закодированный текст: {' '.join(self.encode_text)}")


###################################
# Инициализация и шифрование строки
c1 = Crypter('')
c1.statistic()

c2 = Crypter('p')
c2.statistic()

c3 = Crypter('beep boop beer!')
c3.statistic()

c4 = Crypter('beep ping deep pong!')
c4.statistic()
