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
import collections

# Сделал свой алгоритм формирования двоичного дерева
text = 'Мой дядя самых лучших правил!'
counter_text = sorted(collections.Counter(text).items(), key=lambda item: item[1])

while len(counter_text) > 1:
    new_cell = {0: counter_text[0][0], 1: counter_text[1][0]}, counter_text[0][1] + counter_text[1][1]
    counter_text.pop(0)
    counter_text.pop(0)
    counter_text.append(new_cell)
    counter_text = sorted(counter_text, key=lambda item: item[1])

code_table = dict()

print(f'Двоичное дерево: {counter_text}')


def haffman_code(tree, path=''):
# Поменял условие isistance
    if isinstance(tree, str):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


haffman_code(counter_text[0][0])
for k, i in code_table.items():
    print(f'"{k}": {i}')


