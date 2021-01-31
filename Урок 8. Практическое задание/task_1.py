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
my_string = 'my turtle is slowest from turtles'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return f'{self.left}{self.right}'


# Функция, реализующая кодирование "по Хаффману"
def huffman_code_tree(my_node, bin_string=''):
    if type(my_node) is str:
        return {my_node: bin_string}
    (left, right) = my_node.children()
    data = dict()
    data.update(huffman_code_tree(left, bin_string + '0'))
    data.update(huffman_code_tree(right, bin_string + '1'))
    return data


# Вычисление частоты
freq = {}
for symbol in my_string:
    if symbol in freq:
        freq[symbol] += 1
    else:
        freq[symbol] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, item1) = nodes[-1]
    (key2, item2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, item1 + item2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffman_code = huffman_code_tree(nodes[0][0])
my_huffman_code = str()

for symbol, _ in freq:
    print(symbol, huffman_code[symbol])
    my_huffman_code += huffman_code[symbol]


def encrypt(string, length):
    return ' '.join(string[i:i + length] for i in range(0, len(string), length))


print(f'Входная строка: "{my_string}"')
print(f'Входная строка в бинарном виде: {encrypt(my_huffman_code, 4)}')
