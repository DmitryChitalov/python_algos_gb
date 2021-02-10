"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""


class BinaryTree:
    def __init__(self, source):
        self.source = source
        self.nodes = []
        self.table = dict()
        self.make_nodes_from_str()  # создаем массив нод - листьев
        self.make_tree()  # создаем дерево из листьев
        self.make_table(self.nodes[0])  # получаем таблицу кодирования.

    def make_nodes_from_str(self):
        nodes = []
        source = self.source[:]
        for el in source:
            count = source.count(el)
            if count:
                new_node = Node(el, count)
                BinaryTree.insert_node(nodes, new_node)
                source = source.replace(el, '')
        self.nodes = nodes

    def make_tree(self):
        while len(self.nodes) > 1:
            right = self.nodes.pop()
            left = self.nodes.pop()
            new_node = Node(letter=left.letter + right.letter, freq=right.freq + left.freq)
            """для узла имя необязательно, так нагляднее при визуализации происходящего"""
            new_node.is_leaf = False
            new_node.left_child = left
            new_node.right_child = right
            BinaryTree.insert_node(self.nodes, new_node)
            #  print(self.nodes)

    @staticmethod
    def insert_node(nds, nd):
        ind = 0
        for n in nds:
            if n.freq < nd.freq:
                break
            ind += 1
        nds.insert(ind, nd)

    def make_table(self, node, dc=''):
        if node.is_leaf:
            self.table.update({node.letter: dc})
        else:
            self.make_table(node.right_child, dc + '0')
            self.make_table(node.left_child, dc + '1')

    def print_codes(self):
        for i in str:
            print(self.table[i], end=' ')


class Node:
    def __init__(self, letter=None, freq=None):
        self.letter = letter
        self.freq = freq
        self.is_leaf = True
        self.right_child = None
        self.left_child = None

    def __str__(self):
        if self.is_leaf:
            return f'  {self.letter}:{self.freq}'
        return f'  {self.letter}:{self.freq}' + self.right_child.__str__() + self.left_child.__str__()

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    str = 'beep boop beer!'
    b = BinaryTree(str)
    print(str)
    b.print_codes()


"""
Результат:

beep boop beer!
00 11 11 011 010 00 101 101 011 010 00 11 11 1001 1000 

Реализация с использованием ООП.
методы __str__ и __repr__ перегружены для визуализации происходящих преобразований


"""