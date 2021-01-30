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


class BinTreeNode:
    __slots__ = ['value', 'code', 'left', 'right']

    def __init__(self, value, code=1, left=None, right=None):
        self.value = value
        self.code = code
        self.left = left
        self.right = right


def get_rates(orig_st):
    rates_dic = {}
    for el in orig_st:
        if el not in rates_dic.keys():
            rates_dic[el] = orig_st.count(el)
    return dict(sorted(rates_dic.items(), key=lambda x: x[1], reverse=1))


def grow_tree(seed):
    rates = get_rates(seed)
    while len(rates.keys()) > 1:
        left = rates.popitem()
        right = rates.popitem()
        cur_value = left[1] + right[1]
        if not isinstance(left[0], type('str')):
            left[0].code = 0
        if not isinstance(right[0], type('str')):
            right[0].code = 1
        new_node = BinTreeNode(cur_value, '', BinTreeNode(left[0], 0) if isinstance(left[0], type('str')) else left[0],
                               BinTreeNode(right[0], 1) if isinstance(right[0], type('str')) else right[0])
        rates[new_node] = cur_value
        rates = dict(sorted(rates.items(), key=lambda x: x[1], reverse=1))
    return list(rates.keys())[0]


def encode_el(tree, search_item, code=''):
    cur_code = code + str(tree.code)
    if search_item == tree.value:
        code = str(code) + str(tree.code)
        return code
    elif tree.left is None and tree.right is None:
        return ''
    else:
        if tree.left is not None:
            code = encode_el(tree.left, search_item, str(cur_code))
        if tree.right is not None:
            code = str(code) + encode_el(tree.right, search_item, str(cur_code))
    return code


def show_tree(tree):
    if tree.left is None and tree.right is None:
        print(tree.value, tree.code, sep=' ')
    else:
        if tree.left is not None:
            print(tree.value, tree.code, sep=' ')
            show_tree(tree.left)
        if tree.right is not None:
            print(tree.value, tree.code, sep=' ')
            show_tree(tree.right)
    return


def decode_el(tree, coded_el):
    if tree.left is None and tree.right is None:
        return tree.value
    else:
        if coded_el[0] == '1':
            return decode_el(tree.right, coded_el[1:])
        else:
            return decode_el(tree.left, coded_el[1:])


def encode(st, tree):
    lst = []
    for el in st:
        lst.append(encode_el(tree, el))
    return lst


def decode(st, tree):
    lst = []
    for el in st:
        lst.append(decode_el(tree, el))
    return ''.join(lst)


if __name__ == '__main__':
    my_st = 'beep boop beer!'
    my_tree = grow_tree(my_st)
    # print(my_tree)
    # show_tree(my_tree)
    my_coded_st = encode(my_st, my_tree)
    print(f'{my_st} = {my_coded_st}')
    print(f'{my_coded_st} = {decode(my_coded_st, my_tree)}')
