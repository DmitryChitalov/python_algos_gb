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


class HPackager:
    def __init__(self, data):
        self._data = data

        # Инициализируем двоичное дерево
        self._btree = [HNode(char, f) for char, f in sorted(Counter(data).items(), key=lambda x: x[1], reverse=True)]
        while len(self._btree) > 1:
            node1 = self._btree.pop()
            node2 = self._btree.pop()

            self._append_in_order(node1 + node2)

    # Новый узел добавляем в конец и, пока он не передвинулся в начало
    # или его сосед слева не стал меньше его по частоте - двигаем влево.
    def _append_in_order(self, node):
        idx = len(self._btree)
        self._btree.append(node)
        while idx > 0 and node > self._btree[idx - 1]:
            self._btree[idx], self._btree[idx - 1] = self._btree[idx - 1], self._btree[idx]
            idx -= 1

    def archived_data(self):
        code_table = {}
        self._btree[0].walk(code_table)

        return ' | '.join([code_table[char] for char in self._data])


class HNode:
    def __init__(self, char, freq=0, left=None, right=None):
        self._char = char
        self._freq = freq
        self._left = left
        self._right = right

    def __add__(self, other):
        return HNode(None, self._freq + other._freq, self, other)

    def __str__(self):
        return f'Node freq: {self._freq}' if self._char is None else f'leaf {self._char} freq: {self._freq}'

    def __lt__(self, other):
        return self._freq < other._freq

    def __gt__(self, other):
        return self._freq > other._freq

    # Обходим дерево от корня до листьев. При этом делаем оценку пройденного пути.
    # Как только доходим до листа - дополняем кодовую таблицу.
    def walk(self, code_table, path=''):
        if self._char is None:
            self._left.walk(code_table, path + '0')
            self._right.walk(code_table, path + '1')
        else:
            code_table[self._char] = path


if __name__ == '__main__':
    # '00 11 11 011 010 00 101 101 011 010 00 11 11 1001 1000'
    p = HPackager('beep boop beer!')
    print(p.archived_data())
