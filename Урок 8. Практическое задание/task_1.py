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


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree_create(_str):
    processed_str = deque(sorted(Counter(_str).items(), key=lambda x: x[1]))
    while len(processed_str) > 1:
        weight = processed_str[0][1] + processed_str[1][1]
        new_node = MyNode(left=processed_str.popleft()[0], right=processed_str.popleft()[0])
        for num, elem in enumerate(processed_str):
            if weight > elem[1]:
                continue
            else:
                processed_str.insert(num, (new_node, weight))
                break
        else:
            processed_str.append((new_node, weight))
    return processed_str[0][0]


sym_table = dict()


def creating_recursion(element, path=''):
    if not isinstance(element, MyNode):
        sym_table[element] = path

    else:
        creating_recursion(element.left, path=f'{path}0')
        creating_recursion(element.right, path=f'{path}1')


my_str = 'Whether you\'re new to programming or an experienced developer, it\'s easy to learn and use Python.'

creating_recursion(tree_create(my_str))

for el in my_str:
    print(f'"{el}": {sym_table[el]}')

"""
Пока очень сложно даётся тема, буду разбираться позже как это работает, в ближайшие дни возможности такой не будет. 
Немного оптимизировал исходный код из конспекта, посмотрел что и как выводится, изменил код по-своему.
"""
