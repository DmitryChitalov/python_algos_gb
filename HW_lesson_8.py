# ////////////////////////////////////////////  Task 1  ///////////////////////////////////////////////////////////////

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

import heapq
from collections import Counter, deque
from memory_profiler import profile
import timeit


# -------------------------------------- Вариант 1 --------------------------------------------------------------------

@profile
def huffman_1():
    def huffman_encode(frequency):
        heap = [[wt, [sym, ""]] for sym, wt in frequency.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    txt = input('Введите текст для кодирования: ')
    if len(txt) > 1:
        freq = Counter()
        for ch in txt:
            freq[ch] += 1

        huff = huffman_encode(freq)

        print("Символ\t\tЧастота\t\tКод Хаффмана")
        for ch in huff:
            print(ch[0], "\t\t\t", freq[ch[0]], "\t\t\t", ch[1])

        # for ch in txt:
        encode = ''.join(el[1] for ch in txt for el in huff if ch == el[0])
        print(f'Закодированная строка: {encode}')
    else:
        print('Нечего кодировать.')


# ------------------------------------ Вариант примера с урока --------------------------------------------------------


@profile
def huffman_2():
    def huffman_tree(s):
        # Считаем уникальные символы.
        # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
        count = Counter(s)
        # Сортируем по возрастанию количества повторений.
        # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        # Проверка, если строка состоит из одного повторяющего символа.
        if len(sorted_elements) != 1:
            # Цикл для построения дерева
            while len(sorted_elements) > 1:
                # далее цикл объединяет два крайних левых элемента
                # Вес объединенного элемента (накопленная частота)
                # веса - 2, 4, 4, 7, 8, 15
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                # Словарь из 2 крайних левых элементов, попутно вырезаем их
                # из "sorted_elements" (из очереди).
                # comb - объединенный элемент
                '''
                {0: 'r', 1: '!'}
                {0: {0: 'r', 1: '!'}, 1: 'p'}
                {0: ' ', 1: 'o'}
                {0: 'b', 1: {0: ' ', 1: 'o'}}
                {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
                {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
                '''
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}

                # Ищем место для ставки объединенного элемента
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        # Вставляем объединенный элемент
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    # Добавляем объединенный корневой элемент после
                    # завершения работы цикла

                    sorted_elements.append((comb, weight))
                '''
                deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                deque([(' ', 2), ('o', 2), ('b', 3), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
                deque([('b', 3), ({0: ' ', 1: 'o'}, 4), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
                deque([({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4), ({0: 'b', 1: {0: ' ', 1: 'o'}}, 7)])
                deque([({0: 'b', 1: {0: ' ', 1: 'o'}}, 7), ({0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}, 8)])
                deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
                '''
        else:
            # приравниваемыем значение 0 к одному повторяющемуся символу
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'},
        # 1: 'e'}}, 15)]) {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}} словарь -
        # дерево
        return sorted_elements[0][0]

    code_table = dict()

    # tree - {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    def huffman_code(tree, path=''):
        # Если элемент не словарь, значит мы достигли самого символа
        # и заносим его, а так же его код в словарь (кодовую таблицу).
        if not isinstance(tree, dict):
            code_table[tree] = path
        # Если элемент словарь, рекурсивно спускаемся вниз
        # по первому и второму значению (левая и правая ветви).
        else:
            huffman_code(tree[0], path=f'{path}0')
            huffman_code(tree[1], path=f'{path}1')

    # строка для кодирования
    s = "abracadabra"

    # функция заполняет кодовую таблицу (символ-его код)
    # {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
    huffman_code(huffman_tree(s))

    # code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
    print('\nВариант примера с урока:')
    # выводим коды для каждого символа
    for i in s:
        print(code_table[i], end=' ')
    print()


# huffman_1()
# huffman_2()

print('\nLead time huffman_1(): \t\t', timeit.timeit("huffman_1()", setup="from __main__ import huffman_1", number=1))
print('\nLead time huffman_2(): \t\t', timeit.timeit("huffman_2()", setup="from __main__ import huffman_2", number=1))

""" Результаты выполнения программы:

huffman_1():

Введите текст для кодирования: abracadabra
Символ		Частота		Код Хаффмана
a 		 5 		 0
r 		 2 		 10
b 		 2 		 110
c 		 1 		 1110
d 		 1 		 1111
Закодированная строка: 01101001110011110110100

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    26     15.9 MiB     15.9 MiB           1   @profile
    27                                         def huffman_1():
    28     15.9 MiB      0.0 MiB           2       def huffman_encode(frequency):
    29     15.9 MiB      0.0 MiB           8           heap = [[wt, [sym, ""]] for sym, wt in frequency.items()]
    30     15.9 MiB      0.0 MiB           1           heapq.heapify(heap)
    31     15.9 MiB      0.0 MiB           5           while len(heap) > 1:
    32     15.9 MiB      0.0 MiB           4               lo = heapq.heappop(heap)
    33     15.9 MiB      0.0 MiB           4               hi = heapq.heappop(heap)
    34     15.9 MiB      0.0 MiB           8               for pair in lo[1:]:
    35     15.9 MiB      0.0 MiB           4                   pair[1] = '0' + pair[1]
    36     15.9 MiB      0.0 MiB          14               for pair in hi[1:]:
    37     15.9 MiB      0.0 MiB          10                   pair[1] = '1' + pair[1]
    38     15.9 MiB      0.0 MiB           4               heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    39     15.9 MiB      0.0 MiB          11           return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]),
                                                                                                                    p))
    40                                         
    41     15.9 MiB      0.0 MiB           1       txt = input('Введите текст для кодирования: ')
    42     15.9 MiB      0.0 MiB           1       if len(txt) > 1:
    43     15.9 MiB      0.0 MiB           1           freq = Counter()
    44     15.9 MiB      0.0 MiB          12           for ch in txt:
    45     15.9 MiB      0.0 MiB          11               freq[ch] += 1
    46                                         
    47     15.9 MiB      0.0 MiB           1           huff = huffman_encode(freq)
    48                                         
    49     15.9 MiB      0.0 MiB           1           print("Символ\t\tЧастота\t\tКод Хаффмана")
    50     15.9 MiB      0.0 MiB           6           for ch in huff:
    51     15.9 MiB      0.0 MiB           5               print(ch[0], "\t\t", freq[ch[0]], "\t\t", ch[1])
    52                                         
    53                                                 # for ch in txt:
    54     15.9 MiB      0.0 MiB          80           encode = ''.join(el[1] for ch in txt for el in huff if ch == 
                                                                                                                el[0])
    55     15.9 MiB      0.0 MiB           1           print(f'Закодированная строка: {encode}')
    56                                             else:
    57                                                 print('Нечего кодировать.')

Lead time huffman_1(): 		 6.5401006


huffman_2():

Вариант примера с урока:
0 111 10 0 1100 0 1101 0 111 10 0 

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     15.9 MiB     15.9 MiB           1   @profile
    64                                         def huffman_2():
    65     15.9 MiB      0.0 MiB           2       def huffman_tree(s):
    66                                                 # Считаем уникальные символы.
    67                                               # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
    68     15.9 MiB      0.0 MiB           1           count = Counter(s)
    69                                                 # Сортируем по возрастанию количества повторений.
    70                                                 # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), 
                                                                                                    ('b', 3), ('e', 4)])
    71     15.9 MiB      0.0 MiB          11           sorted_elements = deque(sorted(count.items(), key=lambda item: 
                                                                                                            item[1]))
    72                                                 # Проверка, если строка состоит из одного повторяющего символа.
    73     15.9 MiB      0.0 MiB           1           if len(sorted_elements) != 1:
    74                                                     # Цикл для построения дерева
    75     15.9 MiB      0.0 MiB           5               while len(sorted_elements) > 1:
    76                                                         # далее цикл объединяет два крайних левых элемента
    77                                                         # Вес объединенного элемента (накопленная частота)
    78                                                         # веса - 2, 4, 4, 7, 8, 15
    79     15.9 MiB      0.0 MiB           4                   weight = sorted_elements[0][1] + sorted_elements[1][1]
    80                                                         # Словарь из 2 крайних левых элементов, попутно вырезаем
    81                                                         #  их из "sorted_elements" (из очереди).
    82                                                         # comb - объединенный элемент
    83                                                         '''
    84                                                         {0: 'r', 1: '!'}
    85                                                         {0: {0: 'r', 1: '!'}, 1: 'p'}
    86                                                         {0: ' ', 1: 'o'}
    87                                                         {0: 'b', 1: {0: ' ', 1: 'o'}}
    88                                                         {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
    89                                                         {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1:
                                                                                                '!'}, 1: 'p'}, 1: 'e'}}
    90                                                         '''
    91     15.9 MiB      0.0 MiB           8                   comb = {0: sorted_elements.popleft()[0],
    92     15.9 MiB      0.0 MiB           4                           1: sorted_elements.popleft()[0]}
    93                                         
    94                                                         # Ищем место для ставки объединенного элемента
    95     15.9 MiB      0.0 MiB           6                   for i, _count in enumerate(sorted_elements):
    96     15.9 MiB      0.0 MiB           4                       if weight > _count[1]:
    97     15.9 MiB      0.0 MiB           2                           continue
    98                                                             else:
    99                                                                 # Вставляем объединенный элемент
   100     15.9 MiB      0.0 MiB           2                           sorted_elements.insert(i, (comb, weight))
   101     15.9 MiB      0.0 MiB           2                           break
   102                                                         else:
   103                                                             # Добавляем объединенный корневой элемент после
   104                                                             # завершения работы цикла
   105                                         
   106     15.9 MiB      0.0 MiB           2                       sorted_elements.append((comb, weight))
   107     15.9 MiB      0.0 MiB           2                   '''
   108                                                         deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), 
                                                                                        ('o', 2), ('b', 3), ('e', 4)])
   109                                                         deque([(' ', 2), ('o', 2), ('b', 3), ({0: {0: 'r', 1: 
                                                                                        '!'}, 1: 'p'}, 4), ('e', 4)])
   110                                                         deque([('b', 3), ({0: ' ', 1: 'o'}, 4), ({0: {0: 'r', 1: 
                                                                                        '!'}, 1: 'p'}, 4), ('e', 4)])
   111                                                         deque([({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4), 
                                                                                    ({0: 'b', 1: {0: ' ', 1: 'o'}}, 7)])
   112                                                         deque([({0: 'b', 1: {0: ' ', 1: 'o'}}, 7), ({0: {0: {0: 
                                                                                    'r', 1: '!'}, 1: 'p'}, 1: 'e'}, 8)])
   113                                                         deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: 
                                                                            {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
   114                                                         '''
   115                                                 else:
   116                                                     # приравниваемыем значение 0 к одному повторяющемуся символу
   117                                                     weight = sorted_elements[0][1]
   118                                                     comb = {0: sorted_elements.popleft()[0], 1: None}
   119                                                     sorted_elements.append((comb, weight))
   120                                                 # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1:
                                                                                    {0: {0: {0: 'r', 1: '!'}, 1: 'p'},
   121                                                 # 1: 'e'}}, 15)]) {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: 
                                                                        {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}} словарь -
   122                                                 # дерево
   123     15.9 MiB      0.0 MiB           1           return sorted_elements[0][0]
   124                                         
   125     15.9 MiB      0.0 MiB           1       code_table = dict()
   126                                         
   127                                             # tree - {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: 
                                                                                                '!'}, 1: 'p'}, 1: 'e'}}
   128     15.9 MiB      0.0 MiB          10       def huffman_code(tree, path=''):
   129                                                 # Если элемент не словарь, значит мы достигли самого символа
   130                                                 # и заносим его, а так же его код в словарь (кодовую таблицу).
   131     15.9 MiB      0.0 MiB           9           if not isinstance(tree, dict):
   132     15.9 MiB      0.0 MiB           5               code_table[tree] = path
   133                                                 # Если элемент словарь, рекурсивно спускаемся вниз
   134                                                 # по первому и второму значению (левая и правая ветви).
   135                                                 else:
   136     15.9 MiB      0.0 MiB           4               huffman_code(tree[0], path=f'{path}0')
   137     15.9 MiB      0.0 MiB           4               huffman_code(tree[1], path=f'{path}1')
   138                                         
   139                                             # строка для кодирования
   140     15.9 MiB      0.0 MiB           1       s = "abracadabra"
   141                                         
   142                                             # функция заполняет кодовую таблицу (символ-его код)
   143                                             # {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': 
                                                                                                    '101', 'e': '11'}
   144     15.9 MiB      0.0 MiB           1       huffman_code(huffman_tree(s))
   145                                         
   146                                             # code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': 
                                                                                        '1001', 'p': '101', 'e': '11'}
   147     15.9 MiB      0.0 MiB           1       print('\nВариант примера с урока:')
   148                                             # выводим коды для каждого символа
   149     15.9 MiB      0.0 MiB          12       for i in s:
   150     15.9 MiB      0.0 MiB          11           print(code_table[i], end=' ')
   151     15.9 MiB      0.0 MiB           1       print()

Lead time huffman_2(): 		 0.012901900000000133


ВЫВОД:
    Моя реализация программы - huffman_1() по скорости выполнения оказалась намного медленнее по-времени, чем пример с 
    урока (0.012 секунд против 6.54). 
    Возможно, нужно было использовать deque вместо heapq?
"""

# ////////////////////////////////////////////  Task 2  ///////////////////////////////////////////////////////////////

"""
Задание 2.**

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v and node.l is not None:
            self._find(val, node.l)
        elif val > node.v and node.r is not None:
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


print('\n\n', 10 * '/', 'Task 2', 10 * '/')

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
print(tree.find(10))
tree.deleteTree()
tree.printTree()
