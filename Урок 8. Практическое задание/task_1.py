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


class HaffCoder:
    def __init__(self):
        pass

    def encode(self, line):
        tree = self.__built_haff_tree(line)
        code_table = dict()
        self.__fill_code_table(code_table, tree)
        enc_line = "".join(map(lambda el: code_table[el], line))
        return tree, enc_line

    @staticmethod
    def __built_haff_tree(self, line):
        chars = deque(sorted(Counter(line).items(), key=lambda item: item[1]))
        if len(chars) != 1:
            while len(chars) > 1:
                frequency = chars[0][1] + chars[1][1]
                new_node = {0: chars.popleft()[0], 1: chars.popleft()[0]}
                for ind, el in enumerate(chars):
                    if frequency <= el[1]:
                        chars.insert(ind, (new_node, frequency))
                        break
                else:
                    chars.append((new_node, frequency))
        else:
            frequency = chars[0][1]
            new_node = {0: chars.popleft()[0], 1: None}
            chars.append((new_node, frequency))
        return chars[0][0]  # tree

    def __fill_code_table(self, code_table, haff_tree, path=''):
        if not isinstance(haff_tree, dict):
            code_table[haff_tree] = path
        else:
            self.__fill_code_table(code_table, haff_tree[0], path=f'{path}0')
            self.__fill_code_table(code_table, haff_tree[1], path=f'{path}1')


c = HaffCoder()
tree, line = c.encode("beep boop beer!")
print(line)
