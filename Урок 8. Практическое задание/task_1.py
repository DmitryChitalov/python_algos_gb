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


class Heap:
    def __init__(self):
        self.arr = []

    def sift_up(self):
        x = len(self.arr) - 1
        y = (x - 1) // 2
        while self.arr[y] > self.arr[x]:
            self.arr[x], self.arr[y] = self.arr[y], self.arr[x]
            x = y
            if x:
                y = (x - 1) // 2
            else:
                break

    def sift_down(self):
        n = len(self.arr)
        x = 0
        while 2 * x + 1 <= n - 1:
            y = x
            if self.arr[2 * x + 1] < self.arr[y]:
                y = 2 * x + 1
            if 2 * x + 2 <= n - 1 and self.arr[2 * x + 2] < self.arr[y]:
                y = 2 * x + 2
            if x == y:
                break
            else:
                self.arr[x], self.arr[y] = self.arr[y], self.arr[x]
                x = y

    def insert(self, x):
        self.arr.append(x)
        self.sift_up()

    def extract_min(self):
        if len(self.arr) == 1:
            return self.arr.pop()
        elif len(self.arr) > 1:
            x = self.arr[0]
            self.arr[0] = self.arr.pop()
            self.sift_down()
            return x

    def make_min(self):
        return self.arr[0]

    def get_len(self):
        return len(self.arr)


def huffman_encode(string):
    queue = Heap()
    tree = {}
    binary_code = ''
    for i, j in Counter(string).items():
        queue.insert((j, i))
        tree[i] = ''
    n = queue.get_len()
    if n == 1:
        tree[queue.make_min()[1]] = '0'
    for _ in range(n + 1, 2 * n):
        m1 = queue.extract_min()
        m2 = queue.extract_min()
        if len(m1[1]) == 1 and len(m2[1]) == 1:
            tree[m1[1]] = '1' + tree[m1[1]]
            tree[m2[1]] = '0' + tree[m2[1]]
        elif len(m1[1]) == 1:
            tree[m1[1]] = '0' + tree[m1[1]]
            for j in m2[1]:
                tree[j] = '1' + tree[j]
        elif len(m2[1]) == 1:
            tree[m2[1]] = '0' + tree[m2[1]]
            for j in m1[1]:
                tree[j] = '1' + tree[j]
        else:
            for j in m1[1]:
                tree[j] = '0' + tree[j]
            for j in m2[1]:
                tree[j] = '1' + tree[j]
        queue.insert((m1[0] + m2[0], m1[1] + m2[1]))
    for i in string:
        binary_code += tree[i]

    return binary_code, tree


def decode(binary_code, tree):
    string = ''
    tree = {j: i for i, j in tree.items()}
    keys = tree.keys()
    k = ''
    for i in binary_code:
        k += i
        if k in keys:
            string += tree[k]
            k = ''
    return string


if __name__ == '__main__':
    a = huffman_encode('abacabad')
    print(a[0])
    print(decode(a[0], a[1]))
