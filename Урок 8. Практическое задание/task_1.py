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



РЕШЕНИЕ С ПРИМЕНЕНИЕМ ООП.
"""
from collections import Counter, deque


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        self.left_child = new_node

    # добавить правого потомка
    def insert_right(self, new_node):
        self.right_child = new_node

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


def haffman_tree(s):
    count = Counter(s)
    sorted_arr = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_arr) != 1:
        # Цикл для построения дерева
        while len(sorted_arr) > 1:
            weight = sorted_arr[0][1] + sorted_arr[1][1]
            bin_tree = BinaryTree(weight)
            bin_tree.insert_left(sorted_arr.popleft()[0])
            bin_tree.insert_right(sorted_arr.popleft()[0])

            for i, _count in enumerate(sorted_arr):
                if weight > _count[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    sorted_arr.insert(i, (bin_tree, weight))
                    break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла

                sorted_arr.append((bin_tree, weight))
    else:
        weight = sorted_arr[0][1]
        bin_tree = BinaryTree(weight)
        bin_tree.insert_left(sorted_arr.popleft()[0])
        bin_tree.insert_right(sorted_arr.popleft()[0])
        sorted_arr.append((bin_tree, weight))
    return sorted_arr[0][0]


s = "beep boop beer!"

bin_tree = haffman_tree(s)

code_table = dict()


def haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, BinaryTree):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree.get_left_child(), path=f'{path}0')
        haffman_code(tree.get_right_child(), path=f'{path}1')


haffman_code(bin_tree)
for i in s:
    print(code_table[i], end=' ')
print()
