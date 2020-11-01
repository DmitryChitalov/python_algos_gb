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
#
#
#
# str_elem_count = Counter(str)
# print(str_elem_count)
# sorted_elems = list(sorted(str_elem_count.items(), key=lambda item: item[1]))
# print(sorted_elems)
# if len(sorted_elems) != 1:
#     while len(sorted_elems) > 1:
#         knot = sorted_elems[0][1] + sorted_elems[1][1]
#
#
# print(tmp)
# #min(str_elem_count.values()).
# #print(list(min(str_elem_count.values())))

# Символы входного алфавита образуют список свободных узлов.

# Каждый лист имеет вес, который может быть равен либо вероятности, либо количеству вхождений символа в сжимаемое сообщение.
# Выбираются два свободных узла дерева с наименьшими весами.

# Создается их родитель с весом, равным их суммарному весу.

# Родитель добавляется в список свободных узлов, а два его потомка удаляются из этого списка.

# Одной дуге, выходящей из родителя, ставится в соответствие бит 1, другой — бит 0.
# Битовые значения ветвей, исходящих от корня, не зависят от весов потомков.

# Шаги, начиная со второго, повторяются до тех пор, пока в списке свободных узлов
# не останется только один свободный узел. Он и будет считаться корнем дерева.

class TreeNode:
    def __init__(self, val):
        self.val = val
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return f"TreeNode, val = {self.val}"

    def __repr__(self):
        return f"(TreeNode, val = {self.val})"

    def set_left(self, node):
        self.left_child = node

    def set_right(self, node):
        self.right_child = node

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def get_val(self):
        return self.val



any_str = 'qqqqwweeerrrttooooooooooop'  #'At first I saw don Juan simply as a rather peculiar man who knew a great deal about peyote and who spoke Spanish remarkably well.'

str_elem_count = Counter(any_str)
print(str_elem_count)
sorted_elems = sorted(str_elem_count.items(), key=lambda item: item[1], reverse=True)
print(sorted_elems)
for i, elem in enumerate(sorted_elems):
    sorted_elems[i] = TreeNode(elem)
print(sorted_elems)

# def get_cntr(node):

#     return node.get_val()[1]

while len(sorted_elems) > 1:
    right_node = sorted_elems.pop()
    left_node = sorted_elems.pop()
    r_val = right_node.get_val()
    l_val = left_node.get_val()
    new_val = (r_val[0]+l_val[0], r_val[1]+l_val[1])
    new_node = TreeNode(new_val)
    new_node.set_right(right_node)
    new_node.set_left(left_node)
    sorted_elems.append(new_node)
    sorted_elems.sort(key=lambda node: node.get_val()[1], reverse=True)
    # sorted_elems.sort(key=get_cntr, reverse=True)

# print(sorted_elems)


def tree_print(node: TreeNode, dct, code=""):
    # print(code + " " + str(node.get_val()))
    left_child = node.get_left()
    right_child = node.get_right()
    if left_child is not None:
        tree_print(left_child, dct, code+"0")
    if right_child is not None:
        tree_print(right_child, dct, code+"1")
    if left_child is None and right_child is None:
        dct[node.get_val()[0]] = code

dct = {}
tree_print(sorted_elems[0], dct)
print(dct)
