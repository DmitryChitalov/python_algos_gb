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

import collections as cl


class HardTree:
    def __init__(self, my_string):
        self.my_string = my_string
        self.codes = {}

    def __str__(self):
        return ' '.join([self.codes[symb] for symb in self.my_string])

    @staticmethod
    def my_sort(my_string):
        new_dict = {}
        for symb in my_string:
            new_dict[symb] = new_dict.get(symb, 0) + 1
        return cl.deque(sorted(new_dict.items(), key=lambda el: el[1]))

    def hf_tree(self):
        sorted_els = HardTree.my_sort(self.my_string)
        # Проверяем количество уникальных символов.
        if len(sorted_els) > 1:
            while len(sorted_els) - 1:
                new_length = sorted_els[0][1] + sorted_els[1][1]
                new_el = {0: sorted_els.popleft(
                )[0], 1: sorted_els.popleft()[0]}
                # Ищем место для ставки объединенного элемента
                for idx, tmp_c in enumerate(sorted_els):
                    if not tmp_c[1] < new_length:
                        sorted_els.insert(idx, (new_el, new_length))
                        break
                else:
                    sorted_els.append((new_el, new_length))
        else:
            new_length = sorted_els[0][1]
            comb = {0: sorted_els.popleft()[0], 1: None}
            sorted_els.append((comb, new_length))
        return sorted_els[0][0]

    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.codes[tree] = path
        else:
            self.haffman_code(tree[0], f'{path}0')
            self.haffman_code(tree[1], f'{path}1')


# Создаем новое дерево.
new_tree = HardTree("beep boop beer!")
# Получаем таблицу.
codes = new_tree.haffman_code(new_tree.hf_tree())
# Выводим информацию.
print(new_tree)

"""
Для меня эта тема оказалось достаточно тяжелой, поэтому пытался разобраться, опираясь на пример
с урока. Старался реализовать дерево с помощью ООП, попутно максимально используя его возможности.
Сделал перегрузку метода __str__(), чтобы для вывода на экран достаточно было вызвать функцию print().
"""
