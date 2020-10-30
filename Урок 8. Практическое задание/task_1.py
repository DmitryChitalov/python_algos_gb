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
from heapq import heappush, heappop, heapify
from collections import Counter

def huffman_code(string):
    heap = [[weight, [symbol, '']] for symbol, weight in string.items()]
    heapify(heap)
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        for couple in left[1:]:
            couple[1] += '0'
        for couple in right[1:]:
            couple[1] += '1'
        heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heappop(heap)[1:], key=lambda x: (len(x[-1]), x))

text = "Пробная строка для кодирования."
print(text)
string = Counter(text)
code_table = huffman_code(string)
print(f'Символ  Вес  Код Хаффмана')
for el in code_table:
    print(f'{el[0]:^6}  {string[el[0]]:^3}  {el[1]:^12}')