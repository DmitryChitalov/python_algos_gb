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


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class HaffmanTree:
    __codes: dict
    __tree: deque
    __string: str

    @property
    def codes(self) -> dict:
        return self.__codes

    def __init__(self, string: str):
        self.__string = string
        self.__codes = dict()
        self.__create_tree(string)
        self.__initialize_codes_recursive(self.__tree)

    def __create_tree(self, string: str):
        deque_of_chars = deque(sorted(Counter(string).items(), key=lambda el: el[1]))
        while len(deque_of_chars) > 1:
            weight = deque_of_chars[0][1] + deque_of_chars[1][1]
            current_node = Node(deque_of_chars.popleft()[0], deque_of_chars.popleft()[0])
            for current_deque_index, item in enumerate(deque_of_chars):
                if weight <= item[1]:
                    deque_of_chars.insert(current_deque_index, (current_node, weight))
                    break
            else:
                deque_of_chars.append((current_node, weight))
        self.__tree = deque_of_chars[0][0]

    def __str__(self):
        return ''.join(self.__codes[char] for char in self.__string)

    def __initialize_codes_recursive(self, node_or_element=None, path=''):
        if isinstance(node_or_element, Node):
            self.__initialize_codes_recursive(node_or_element.left, f'{path}0')
            self.__initialize_codes_recursive(node_or_element.right, f'{path}1')
        else:
            self.__codes[node_or_element] = path


print(HaffmanTree("beep boop beer!"))
