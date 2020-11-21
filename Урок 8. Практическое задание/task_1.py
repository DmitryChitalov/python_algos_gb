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


class Haffman:
    def __init__(self, new_string):  # новая строка, которая будет кодироваться
        self.new_string = new_string

    def str_count_deque(self):  # метод класса, который подсчитывает количество элементов в строке
        new_string_list = list(self.new_string)
        count_dict = {i: new_string_list.count(i) for i in set(new_string_list)}
        # sorted_values = sorted(count_dict.values())  # Сортировка значений
        sorted_count_deque = deque(sorted(count_dict.items(), key=lambda item: item[1]))
        # sorted_count_dict = {}
        # for i in sorted_values:
        #     for k in count_dict.keys():
        #         if count_dict[k] == i:
        #             sorted_count_dict[k] = count_dict[k]
        return sorted_count_deque

    def binary_tree(self, sorted_count_deque):  # метод класса, составляющий дерево из элементов
        # if len(sorted_count_deque) == 1:
        #     cur_prior = sorted_count_deque[0][1]
        #     new_knot = {0: sorted_count_deque.popleft()[0], 1: None}
        #     sorted_count_deque.append((new_knot, cur_prior))
        #     return sorted_count_deque[0][0]
        # cur_prior = sorted_count_deque[0][1] + sorted_count_deque[1][1] ####  TypeError: unsupported operand type(s) for +: 'dict' and 'int'
        # new_knot = {0: sorted_count_deque.popleft()[0],
        #             1: sorted_count_deque.popleft()[0]}
        # for i, prior in enumerate(sorted_count_deque):
        #     if cur_prior > prior[1]:
        #         continue
        #     else:
        #         sorted_count_deque.insert(i, (cur_prior, new_knot))
        #         break
        # else:
        #     sorted_count_deque.append((new_knot, cur_prior))
        # return self.binary_tree(sorted_count_deque)

        if len(sorted_count_deque) != 1:
            while len(sorted_count_deque) > 1:
                cur_priority = sorted_count_deque[0][1] + sorted_count_deque[1][1]
                new_knot = {0: sorted_count_deque.popleft()[0],
                            1: sorted_count_deque.popleft()[0]}
                for i, prior in enumerate(sorted_count_deque):
                    if cur_priority > prior[1]:
                        continue
                    else:
                        sorted_count_deque.insert(i, (new_knot, cur_priority))
                        break
                else:
                    sorted_count_deque.append((new_knot, cur_priority))
        else:
            cur_priority = sorted_count_deque[0][1]
            new_knot = {0: sorted_count_deque.popleft()[0], 1: None}
            sorted_count_deque.append((new_knot, cur_priority))
        return sorted_count_deque[0][0]


    def haffman_code(self, tree, path='', code_table={}):
        ''' взял из примера'''

        # Если элемент не словарь, значит мы достигли самого символа
        # и заносим его, а так же его код в словарь (кодовую таблицу).
        if not isinstance(tree, dict):
            code_table[tree] = path
        # Если элемент словарь, рекурсивно спускаемся вниз
        # по первому и второму значению (левая и правая ветви).
        else:
            s.haffman_code(tree[0], path=f'{path}0')
            s.haffman_code(tree[1], path=f'{path}1')


text = 'beep boop beer!'
s = Haffman(text)
k = s.str_count_deque()
t = s.binary_tree(k)
print(t)
print(s.haffman_code(t))
