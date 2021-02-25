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
"""
C 3ей попытки, полностью самостоятельно. Самой приятно, что наконец получилось! )
"""


from collections import Counter


class Node:

    value: tuple
    left_child: tuple
    right_child: tuple

    def __init__(self, children: []):
        if len(children) == 1:
            self.value = children[0]
            self.left_child = None
            self.right_child = None
        else:
            self.left_child = children[0]
            # print(type(self.left_child), self.left_child)
            self.right_child = children[1]
            # print(type(self.right_child), self.right_child)
            node_name = f"{children[0][0].get_value()[0]}{children[1][0].get_value()[0]}"
            self.value = (node_name, children[0][1]+children[1][1])

    def __str__(self):
        return f"Node {self.value} with left_child {self.left_child} and right_child {self.right_child}"

    def get_value(self):
        return self.value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


# Заменяем переданный counter на новый состоящий из node без детей.
def counter_modification(simple_counter):
    obj_counter = Counter()

    for el, value in simple_counter.items():
        temp_tuple = (el, value)
        leaf_node = Node([temp_tuple])
        obj_counter[leaf_node] = value

    return obj_counter


# создаем дерево
def haffman_tree(array_weight: Counter):

    next_children = array_weight.most_common()[:-3:-1]
    next_node = Node(next_children)
    # print(type(next_node), next_node)

    for el in next_children:
        # print(type(el[0]), el[0])
        array_weight[el[0]] = 0  # обнуляем "вес" взятых элементов.

    array_weight[next_node] = next_node.get_value()[1]
    array_weight += Counter()  # удаляем нулевые элементы
    # print(array_weight)

    if len(array_weight) == 1:
        return next_node

    return haffman_tree(array_weight)


def tree_parser(node: Node, bi_code: str):

    if node.get_left_child() is None:
        print(node.get_value()[0], bi_code)
        letter_code[node.get_value()[0]] = bi_code
        return node.get_value()[0], bi_code

    return tree_parser(node.get_left_child()[0], f"{bi_code}0"), tree_parser(node.get_right_child()[0], f"{bi_code}1")


my_str = "beep boop beer!?"

# найдем частотность букв используя коллекцию counter. weight - сколько раз буква встречается.
letter_weight_dict = Counter(my_str)
print(letter_weight_dict)
# получаем корневой node. С двумя детьми, каждый из которых в свою очередь имеет своих детей и т.д.
root_node = haffman_tree(counter_modification(letter_weight_dict))

print(type(root_node), root_node)
letter_code = {}
print("Код для каждой буквы: ")
tree_parser(root_node, "")
print(letter_code)
