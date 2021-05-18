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

import queue

#Узел
class Node:
    def __init__(self, x, k=-1, l=None, r=None, c=''):
        self.freq = x
        self.key = k
        self.left = l
        self.right = r
        self.code = c

    def __lt__(self, otr):
        return self.freq < otr.freq

#Декодер
def huffman_decoder(code_table, data):
    decoder = []
    for s in data:
        for key_1 in code_table:
            if s == key_1:
                decoder.append(code_table[key_1])
    return " ".join(decoder)


#Словарь из символов и количества вхождений
def huffman_code(data):
    freqTable = {}
    nodeList = []
    que = queue.PriorityQueue()
    codeTable = {}

    for n in data:
        if n in freqTable:
            freqTable[n] += 1
        else:
            freqTable[n] = 1

    for k, v in freqTable.items():
        nodeList.append(Node(v, k))
        que.put(nodeList[-1])

    while que.qsize() > 1:
        n1 = que.get()
        n2 = que.get()
        n1.code = '1'
        n2.code = '0'
        nn = Node(n1.freq + n2.freq, l=n1, r=n2);
        nodeList.append(nn);
        que.put(nodeList[-1])

    def bl(p, codestr=[]):
        codestr.append(p.code)
        if p.left:
            bl(p.left, codestr.copy())
            bl(p.right, codestr.copy())
        else:
            codeTable[p.key] = ''.join(codestr)

    bl(nodeList[-1])
#После получения используем декодер
    return huffman_decoder(codeTable, data)




#Пользовательский код
if __name__ == '__main__':

    user_input = input("Введите строку: ")
    huff_list = []
    for i in user_input:
        huff_list.append(i)
    huff_code = huffman_code(huff_list)
    print(huff_code)
