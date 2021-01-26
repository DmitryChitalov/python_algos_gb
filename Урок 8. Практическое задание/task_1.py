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


class Bin_Tree:
    def __init__(self, dict_counter, dict_storage=None):
        self.dict_storage = ({} if dict_storage is None else dict_storage)
        self.dict_c = dict_counter
        self.tuple_work = sorted(dict_counter.items(), key=lambda item: item[1])

    def paste_storage(self, elem_tuple, pref):
        for i in elem_tuple:
            self.dict_storage[i] = self.dict_storage.setdefault(i, (i,)) + (pref,)

    def reduction(self):
        if len(self.tuple_work) > 1:
            power_node = self.tuple_work[0][-1] + self.tuple_work[1][-1]

            self.paste_storage(self.tuple_work[0][0], 0)
            self.paste_storage(self.tuple_work[1][0], 1)

            name_node = f"{self.tuple_work[0][0]}{self.tuple_work[1][0]}"
            self.dict_c = dict(self.tuple_work[2:])    # Новый (обновленный) словарь
            del self.tuple_work
            self.dict_c[name_node] = power_node
            # print(self.dict_c, f"{name_node}:{power_node}")    # s = "Beep boop beer!"
            """Вставка принта выдаст промежуточные словари и новые элементы в них 
            {'p': 2, ' ': 2, 'o': 2, 'b': 3, 'e': 4, 'r!': 2} r!:2
            {'o': 2, 'r!': 2, 'b': 3, 'e': 4, 'p ': 4} p :4
            {'b': 3, 'e': 4, 'p ': 4, 'or!': 4} or!:4
            {'p ': 4, 'or!': 4, 'be': 7} be:7
            {'be': 7, 'p or!': 8} p or!:8
            {'bep or!': 15} bep or!:15
            """

            new_node = Bin_Tree(self.dict_c, self.dict_storage)
            new_node.reduction()

        return {k: ''.join([str(j) for j in v[1:]]) for k, v in self.dict_storage.items()}

def str_encoding(string=None):
    # string = input("Введите строку ")
    test_dict = Counter(string.lower())
    test_class = Bin_Tree(test_dict)
    dict_total = test_class.reduction()
    # print(dict_total)
    print(string)
    print(*[dict_total[i] for i in string.lower()])


s = "Beep boop beer!"     # 00 10 10 001 101 00 011 011 001 101 00 10 10 0111 1111
# s = "Красная краска"    # 00 110 01 011 0111 01 1111 010 00 110 01 011 00 01
str_encoding(s)
