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
import sys


def haffman_tree_creat(s):
    count_elements = Counter(s)
    deque_els = deque(sorted(count_elements.items(), key=lambda item: item[1]))
    if len(deque_els) != 1:
        while len(deque_els) > 1:
            summary_weight = deque_els[0][1] + deque_els[1][1]
            united_elements = {0: deque_els.popleft()[0],
                               1: deque_els.popleft()[0]}
            for i, _count in enumerate(deque_els):
                if summary_weight > _count[1]:
                    continue
                else:
                    deque_els.insert(i, (united_elements, summary_weight))
                    break
            else:
                deque_els.append((united_elements, summary_weight))
    else:
        summary_weight = deque_els[0][1]
        united_elements = {0: deque_els.popleft()[0], 1: None}
        deque_els.append((united_elements, summary_weight))
    return deque_els[0][0]


def haffman_code(tree, return_line=''):
    if isinstance(tree, dict):
        haffman_code(tree[0], return_line=f'{return_line}0')
        haffman_code(tree[1], return_line=f'{return_line}1')
    else:
        code_table[tree] = return_line


code_table = dict()
# s = "beep boop beer!"
s = input("Введите строку для декодирования: ")
#print(sys.getsizeof(s))

haffman_code(haffman_tree_creat(s))

print("Закодированная строка выглядит так: ", end=' ')
for i in s:
    print(code_table[i], end=' ')
print()
#print(sys.getsizeof(code_table))
#Понимаю что размер нужно считать не массива, а битовых значений.
