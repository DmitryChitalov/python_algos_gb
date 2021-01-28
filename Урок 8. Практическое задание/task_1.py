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


class Huffman_converter:
    def __init__(self, input_str):
        self.input_str = input_str

    def __str__(self):
        return self.convert(self.input_str)

    def __my_count(self, my_str):
        return Counter(my_str).most_common()[::-1]

    def __tree_build(self, lst):
        self.code_dict = dict()
        while len(lst) > 1:
            for ind in range(2):
                if len(lst[ind][0]) == 1:
                    self.code_dict[lst[ind][0]] = str(ind)
                else:
                    for i in lst[ind][0]:
                        self.code_dict[i] = str(ind) + self.code_dict.get(i)
            name = lst[0][0] + lst[1][0]
            count = lst[0][1] + lst[1][1]
            del lst[:2]
            lst.append(tuple([name, count]))
            lst = sorted(lst, key=lambda cnt: cnt[1])

    def convert(self, input_str):
        my_list = self.__my_count(input_str)
        self.__tree_build(my_list)
        code = ''
        for i in input_str:
            code += self.code_dict.get(i) + ' '
        return code[:-1]


print(Huffman_converter('lllallhhhao'))
print(Huffman_converter('beep boop beer!'))
print(Huffman_converter('jjjjyyyyhh'))
