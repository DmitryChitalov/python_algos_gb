"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


class BinaryTree:
    """Класс взял полностью из задания 2, т.к. основная цель не написание класса
    Добавил только новое поле element - хранит символ узла, если есть
    """
    def __init__(self, root_obj, element=""):
        # корень
        self.root = root_obj
        # символ
        self.element = element
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = new_node
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = new_node
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = new_node
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = new_node
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child


def haffman_tree(my_str):
    """
    Построение бинароного дерева Хаффмана на основе класса.
    Подразумевается, что каждый символ - это тоже узел, только без веток.
    """
    str_dict = Counter(my_str)
    str_sorted_dict = deque(sorted(str_dict.items(), key=lambda item: item[1]))
    sorted_list = []

    # Создадим список узлов без веток для каждой буквы
    for i in str_sorted_dict:
        sorted_list.append(BinaryTree(i[1], i[0]))

    if len(sorted_list) != 1:
        # Если в списке больше одного символа, то начнем строить дерево.
        # Иначе вернем первый элемент
        while len(sorted_list) > 1:
            # Берем первых два элемента и делаем из них узел с сумарным весом
            weight = sorted_list[0].root + sorted_list[1].root
            ttt = BinaryTree(weight)
            # Логика класса такова, что при добавлении нового узла в одну из веток, существующий узел в этой ветке
            # станет веткой нового узла. Что позволяет сделать код построения дерева довольно лаконичным
            ttt.insert_left(sorted_list.pop(0))
            ttt.insert_right(sorted_list.pop(0))

            # Вставим полученный узел на свое место, в соответствии с root
            for idx, val in enumerate(sorted_list):
                if val.root < ttt.root:
                    continue
                sorted_list.insert(idx, ttt)
                break
            else:
                # Если вставить не получилось, то добавляем в конец
                sorted_list.append(ttt)

    res = sorted_list[0]

    return res


codes = dict()


def haffman_code(tree: BinaryTree, my_str=""):

    # Если нет и левой ветки и правой, то мы достигли самого символа
    if tree.left_child == None and tree.right_child == None:
        if my_str == "":
            # Если в самом первом узле нет веток, то выведем 0
            codes[tree.element] = "0"
        else:
            codes[tree.element] = my_str

    # Если ветки есть, то спускаемся по ним. Проверяем, что ветки есть, т.к. может быть только одна
    else:
        if tree.left_child != None:
            haffman_code(tree.get_left_child(), my_str=f'{my_str}0')
        if tree.right_child != None:
            haffman_code(tree.get_right_child(), my_str=f'{my_str}1')


str_1 = "beep boop beer!"
str_2 = "b"
t = haffman_tree(str_1)
haffman_code(t)

# выводим коды для каждого символа
for i in str_1:
    print(codes[i], end=' ')
print()
