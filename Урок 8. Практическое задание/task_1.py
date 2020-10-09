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
from collections import deque, Counter
res_table = dict()


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree(s):
    count_s = Counter(s)
    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))
    while len(sorted_s) > 1:
        weight = sorted_s[0][1] + sorted_s[1][1]
        leaf = Node(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])
        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (leaf, weight))
                break
        else:
            sorted_s.append((leaf, weight))
    return sorted_s[0][0]


def encode(tree, path=''):
    if not isinstance(tree, Node):
        res_table[tree] = path
        print(path)
    else:
        encode(tree.left, path=f'{path}0')
        encode(tree.right, path=f'{path}1')

string_to_code = "test"
get_tree = tree(string_to_code)
encode(get_tree)

for v, i in res_table.items():
    print(f'{v}  =  {i}')

"""
Добрый день ! Не смог придумать улучшений к вашему коду по кодировке Хаффмана с словарем,
поэтому добавил в ваше решение элементы ООП.
Долго бился с декодировкой, очевидно, что для корректной расшифровки необходимо передать второй стороне
словарь сформированный при кодировании. Так как возможны различные варианты нахождений в строке символов
 с одинаковой степенью вероятности(), а так же левые и правые листья можно нумеровать как 
 1 и 0 так и  0 и 1, что так же приведет к невозможности декодировки.
"""