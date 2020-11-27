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

    # попробовал сделать через namedtuple - с помощью Вашего примера, stackoverflow, хабра и еще кучи безымянных ресурсов получилось


from collections import Counter, namedtuple
import heapq

class Node(namedtuple('Node', ['left', 'right'])):
    # structure of the tree via namedtuple
    def walk(self, code, acc):

        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaves(namedtuple('Leaves', ['char'])):
    # value of the tree's leaves
    def walk(self, code, acc):

        code[self.char] = acc or '0'


def huffman_encode(s):
    # encoding the string via the Huffman's algorithm
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaves(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq_1, count_1, left = heapq.heappop(h)
        freq_2, count_2, right  = heapq.heappop(h)

        heapq.heappush(h, (freq_1 + freq_2, count, Node(left, right)))

        count +=1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def huffman_decode(encoded, code):
    # decoding the string via the Huffman's algorithm
    sx = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ''
                break
    return ''.join(sx)



if __name__ == '__main__':

    str = input('Enter your string: ')
    code = huffman_encode(str)
    encoded = ''.join(code[ch] for ch in str)

    print(huffman_decode(encoded, code))
    print(encoded)




