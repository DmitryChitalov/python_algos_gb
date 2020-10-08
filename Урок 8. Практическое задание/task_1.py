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


class HuffmanCoding:
    def __init__(self, str_obj):
        self.str_obj = str_obj
        self.character_code = dict()

    def getting_frequencies(self):
        cnt = Counter(self.str_obj)
        return deque(sorted(cnt.items(), key=lambda el: el[1]))

    def binary_tree(self):
        res_tree = HuffmanCoding.getting_frequencies(self)
        for _ in range(len(res_tree) - 1):
            sum_frequency = res_tree[0][1] + res_tree[1][1]
            res = {0: res_tree.popleft()[0],
                   1: res_tree.popleft()[0]}
            for i, cnt in enumerate(res_tree):
                if sum_frequency > cnt[1]:
                    continue
                else:
                    res_tree.insert(i, (res, sum_frequency))
                    break
            else:
                res_tree.append((res, sum_frequency))
        return res_tree[0][0]

    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.character_code[tree] = path
        else:
            HuffmanCoding.haffman_code(self, tree[0], path=f'{path}0')
            HuffmanCoding.haffman_code(self, tree[1], path=f'{path}1')
        return self.character_code

    def result_str(self, table_dict):
        res = ''
        for el in self.str_obj:
            res += table_dict[el] + ' '
        return res


s = "beep boop beer!"
HC = HuffmanCoding(s)
table = HC.haffman_code(HC.binary_tree())
print(HC.result_str(table))

"""
Придумал свой вариант решения через ООП, но в основе лежит Ваш алгоритм.

Вопрос к Вашему коду:
    Возможно я что-то недопонял, но из Вашего кода нижеуказанное можно вообще убрать.
        else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
    # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    # словарь - дерево
"""
