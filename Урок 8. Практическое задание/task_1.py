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
from operator import itemgetter


class HuffmanCoding(object):
    def __init__(self, str_obj):
        self.str_obj = str_obj
        self.character_code = dict()

    def getting_frequencies(self):
        cnt = Counter(self.str_obj)
        sorted_el = deque(sorted(cnt.items(), key=itemgetter(1)))
        if len(sorted_el) == 1:
            weight = sorted_el[0][1]
            comb = {0: sorted_el.popleft()[0], 1: None}
            sorted_el.append((comb, weight))
        return sorted_el

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


if __name__ == "__main__":

    s = "beep boop beer!"
    HC = HuffmanCoding(s)
    my_tree = HC.binary_tree()
    my_code = HC.haffman_code(my_tree)
    print(f"Количество повторений - {HC.getting_frequencies()}")
    print(f"Дерево - {my_tree}")
    print(f"Кодовая таблица - {my_code}")
    print(f"Результат - {HC.result_str(my_code)}")

