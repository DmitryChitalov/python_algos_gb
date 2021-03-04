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


def haffman(s):
    count = Counter(s)
    elements_sorted = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(elements_sorted) != 1:
        while len(elements_sorted) > 1:
            weight = elements_sorted[0][1] + elements_sorted[1][1]
            comb = {0: elements_sorted.popleft()[0],
                    1: elements_sorted.popleft()[0]}
            for i, numb in enumerate(elements_sorted):
                if weight > numb[1]:
                    continue
                else:
                    elements_sorted.insert(i, (comb, weight))
                    break
            else:
                elements_sorted.append((comb, weight))
    else:
        weight = elements_sorted[0][1]
        comb = {0: elements_sorted.popleft()[0], 1: None}
        elements_sorted.append((comb, weight))
    return elements_sorted[0][0]


code_table = dict()


def haffman_code(tree, path=''):

    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


def show_coding(a):
    haffman_code(haffman(a))
    print(f'Coded phrase:\n{a}')
    print('Code:')
    for i in a:
        print(code_table[i], end=' ')


phrase = "Haffman algorithm is the best"


show_coding(phrase)

