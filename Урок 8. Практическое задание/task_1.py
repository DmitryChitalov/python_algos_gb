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


class Tree:
    def __init__(self, any_deque=deque(), any_dict={}):
        self.dict = any_dict
        self.deque = any_deque
        self.dict_for_code = {}

    # Изначально планировал сделать класс для каждой пары буква-частота и добавлять его в deq
    def insert_node(self, node):
        self.deque.appendleft(node)

    def get_dict(self):
        while len(self.deque) > 1:
            left = self.deque.popleft()
            right = self.deque.popleft()
            frequency = left[1] + right[1]

            self.dict = {0: left[0],
                         1: right[0]}

            for index, value in enumerate(self.deque):
                if index == len(self.deque) - 1:
                    self.deque.insert(index + 1, (self.dict, frequency))
                    break
                elif frequency > value[1]:
                    continue
                else:
                    self.deque.insert(index, (self.dict, frequency))
                    break
            if not self.deque:
                self.deque.append((self.dict, frequency))
                break

    def get_encoded(self, random_dict={}, path=''):
        if not isinstance(random_dict, dict):
            my_tree.dict_for_code[random_dict] = path
        else:
            my_tree.get_encoded(random_dict[0], path=f'{path}0')
            my_tree.get_encoded(random_dict[1], path=f'{path}1')

# Рудимент, к сожалению
class Node:
    def __init__(self, node):
        self.node = node


my_tree = Tree()

str_to_code = "beep boop beer!"
str_like_dict = Counter(str_to_code)
reversed_list_in_deque = deque(sorted(str_like_dict.items(), key=lambda item: item[1]))

my_tree = Tree(reversed_list_in_deque)

# Пережиток от классов, хотел таким образом сделать deq по возрастанию,
# но метод items почему-то возвращает первым элементом пару ('b', 3), а не ('e', 4) из словаря Counter
# for key, value in str_like_dict.items():
#     new_node = Node((key, value))
#     my_tree.insert_node(new_node.node)

my_tree.get_dict()
print(my_tree.dict)

my_tree.get_encoded(my_tree.dict)
print(my_tree.dict_for_code)

for letter in my_tree.dict_for_code:
    print(my_tree.dict_for_code[letter], end=' ')

"""
Итоговая строка отличается от примера на уроке т.к. 
при заполнении deque по частоте элемент ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4)
встает не перед ('e', 4), а после
"""
