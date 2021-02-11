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
"""Хаффман через коллекции"""
from collections import Counter, deque


def haffman_tree(s):
    count_string = Counter(s)
    sorted_deq = deque(sorted(count_string.items(), key=lambda item: item[1]))
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sorted_deq) != 1:
        # Цикл для построения дерева
        while len(sorted_deq) > 1:
            weight = sorted_deq[0][1] + sorted_deq[1][1]
            comb = {0: sorted_deq.popleft()[0],
                    1: sorted_deq.popleft()[0]}

            for i, _count in enumerate(sorted_deq):
                if weight > _count[1]:
                    continue
                else:
                    sorted_deq.insert(i, (comb, weight))
                    break
            else:
                sorted_deq.append((comb, weight))

    else:
        weight = sorted_deq[0][1]
        comb = {0: sorted_deq.popleft()[0], 1: None}
        sorted_deq.append((comb, weight))
    # словарь - дерево
    return sorted_deq[0][0]


code_table = dict()
# tree - {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


# строка для кодирования
s = "beep boop beer!"

haffman_code(haffman_tree(s))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in s:
    print(code_table[i], end=' ')
print()
