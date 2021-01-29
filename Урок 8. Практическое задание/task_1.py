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
from collections import Counter, namedtuple
import random
import string


class Node(namedtuple("Node", ["left", "right"])):  # Класс промежуточного узла
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):  # Класс конечного листа
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []  # Пустой файл списка для создания очереди приоритета
    for ch, freq in Counter(s).items():  # Записываем в список кортежи, состоящие из символа и частоты вхождения
        h.append((freq, len(h), Leaf(ch)))  # Средний элемент len(h) добавляем, чтобы отработать случаи исключения
    heapq.heapify(h)  # Создаем очередь приоритета

    while len(h) > 1:  # Пока в очереди не останется одного элемента начинаем обход попарно в неубывающем порядке
        count = len(h)
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count + _count1 + _count2 * random.randint(0, 1000), Node(left, right)))
        # Вставляем сумму двух наименьших элементов в очередь средний элемент - для обеспечения работоспособности heap при длинных строках
        # сумма идёт как промежуточный узел
    code = {}  # Пустой кодовый словарь
    if h:
        [(_freq, _count, root)] = h  # корневой элемент
        root.walk(code, "")  # Начинаем обход с корневого элемента
    return code  # Возвращаем кодовый словарь

#Функция декодирования строки Хаффмана:
def huffman_decode(str_enc, code_dict):
    str_dec = []
    letter = []
    str_enc = list(str_enc)
    for i in range(len(str_enc)):
        letter.append(str_enc.pop(0))
        if ''.join(letter) in code_dict.values():
            for k, v in code_dict.items():
                if v == ''.join(letter):
                    str_dec.append(k)
                    letter = []
    return ''.join(str_dec)


def test(n_iter=100):
    for i in range(n_iter):
        str_len = random.randint(0, 128)
        lcl_str = "".join(random.choice(string.ascii_letters) for _ in range(str_len))
        code = huffman_encode(lcl_str)
        encoded = "".join(code[ch] for ch in lcl_str)
        assert huffman_decode(encoded, code) == lcl_str


def main():
    s = input("Please enter the phrase to encode in Huffman: ")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print("Словарь для кодирования:")
    for ch in sorted(code):
        print(f'{ch}:{code[ch]}')
    print(f'Закодированная скрока {s} :{encoded}')
    print(f'Декодированная строка {encoded}: {huffman_decode(encoded, code)}')


if __name__ == '__main__':
    main() #запуск осноговного кода
    test() #запуск процедуры теста
