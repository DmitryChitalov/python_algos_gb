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
from task_2 import BinaryTree
from collections import Counter, deque


def get_tree(in_string):
    count_dict = Counter(in_string)
    my_deq = deque(sorted(count_dict.items(), key=lambda item: item[1]))
    if len(my_deq) != 1:
        while len(my_deq) > 1:
            # print(my_deq[0][1],my_deq[1][1])
            weight = my_deq[0][1] + my_deq[1][1]
            # new_tree = BinaryTree(weight)
            # new_tree.insert_left(my_deq[0][0])
            # new_tree.insert_right(my_deq[1][0])
            # my_deq.popleft()
            # my_deq.popleft() # как-то надо индекс/вес передавать помимо обьекта...
            block = {0: my_deq.popleft()[0], 1: my_deq.popleft()[0]}
            for numb, elem in enumerate(my_deq):
                if weight > elem[1]:
                    continue
                else:
                    my_deq.insert(numb, (block, weight))
                    break
            else:
                my_deq.append((block, weight))
    else:
        weight = my_deq[0][1]
        block = {0: my_deq.popleft()[0], 1: None}
        my_deq.append((block, weight))
    return my_deq[0][0]


coder_page = {}


def get_code(tree, code = ''):
    if type(tree) != dict:
        coder_page[tree] = code
    else:
        get_code(tree[0], code = code + '0')
        get_code(tree[1], code = code + '1')
    return coder_page


if __name__ == '__main__':
    s = 'my test string'
    # s = "beep boop beer!"
    # print(get_tree(s))
    c = get_code(get_tree(s))
    print(' '.join([c.get(i) for i in s]))

# что-то с классом моим не то... с деревом вроде понятно и с Хаффманом более-менее, а с ООП надо еще разбираться
