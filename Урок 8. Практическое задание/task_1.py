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


class BinaryTree:                                                           # Объявляем класс построения дерева
    def __init__(self, root_obj):                                           # C методами вставки и получения потомков
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        self.left_child = new_node

    def insert_right(self, new_node):
        self.right_child = new_node

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child


def build_haffman_tree(string):
    count = Counter(string)                                                 # Счетчик опрделяет частотность символа
    sorted_arr = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_arr) != 1:                                                # Строим дерево
        while len(sorted_arr) > 1:
            weight = sorted_arr[0][1] + sorted_arr[1][1]
            bin_tree = BinaryTree(weight)
            bin_tree.insert_left(sorted_arr.popleft()[0])
            bin_tree.insert_right(sorted_arr.popleft()[0])

            for i, _count in enumerate(sorted_arr):
                if weight > _count[1]:
                    continue
                else:                                                        # Вставляем  элемент
                    sorted_arr.insert(i, (bin_tree, weight))
                    break
            else:                                                            # Добавляем  корневой элемент после
                sorted_arr.append((bin_tree, weight))                        # завершения работы цикла
    else:
        weight = sorted_arr[0][1]
        bin_tree = BinaryTree(weight)
        bin_tree.insert_left(sorted_arr.popleft()[0])
        bin_tree.insert_right(sorted_arr.popleft()[0])
        sorted_arr.append((bin_tree, weight))
    return sorted_arr[0][0]


input_string = "beep boop beer!"

bin_tree = build_haffman_tree(input_string)

create_code_table = dict()


def haffman_code(tree, path=''):                                              # Если элемент не словарь,
    if not isinstance(tree, BinaryTree):                                      # значит мы достигли самого символа
        create_code_table[tree] = path                                        # и заносим его, и его код в словарь

    else:                                                                     # Если словарь, рекурсивно спускаемся вниз
        haffman_code(tree.get_left_child(), path=f'{path}0')
        haffman_code(tree.get_right_child(), path=f'{path}1')                 # по первому и второму значению
                                                                              # (левая и правая ветви).

haffman_code(bin_tree)

for i in input_string:
    print(create_code_table[i], end=' ')
print(f'\n Искомая строка:  {input_string}')

"""
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001 
 Искомая строка:  beep boop beer!
"""
