"""Задание 1. Реализуйте кодирование строки "по Хаффману". У вас два пути: 1)
тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою
версию алгоритма Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения и оптимизации. КОПИПАСТ ПРИМЕРА
ПРИНИМАТЬСЯ НЕ БУДЕТ! 2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход
к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
import heapq  # Очередь с приоритетами
from collections import Counter, namedtuple


# объявляем класс Узел, хранящий информацию о левом и правом потомках
class Node(namedtuple('Node', ['left', 'right'])):
    # метод, позволяющий обходить дерево, начиная от корня и собирать в
    # словарь 'code' символы 0 с левых потомков, символы 1 с правых потомков,
    # объединяя их в строку
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


# объявляем класс Лист, хранящий информацию о символе
class Leaf(namedtuple('Leaf', ['char'])):
    # метод walk для листа добавляет в словарь символ в качестве ключа,
    # и код этого символа в качестве значения
    def walk(self, code, acc):
        code[self.char] = acc or '0'  # '0' для кодирования строки из 1 символа


def huffman_encode(s: str) -> dict:
    # Создаём очередь с приоритетами, где приоритет - это "частота" символа в
    # строке, подсчитанная с помощью Counter, а элемент очереди - это объект
    # класса Leaf (лист), хранящий информацию о символе
    # второй компонент очереди (len(queue_p)) добавлен, чтобы все компоненты
    # очереди были уникальными, на тот случай, если частота двух листьев
    # будет одинаковой, иначе из-за механики очереди с приоритетами может
    # возникнуть ошибка сравнения объектов класса Leaf() и str()
    queue_p = []
    for ch, freq in Counter(s).items():
        queue_p.append((freq, len(queue_p), Leaf(ch)))
    heapq.heapify(queue_p)
    # Достаём из очереди по два элемента с минимальным приоритетом (то есть
    # символ с минимальной частотой) - левый и правый потомки будущего Узла
    count = len(queue_p)
    while len(queue_p) > 1:
        freq_1, _count1, left = heapq.heappop(queue_p)
        freq_2, _count1, right = heapq.heappop(queue_p)
        # Объединяем два "листа" символа в один "узел" и добавляем их обратно
        # в очередь, указав в качестве приоритета суммарную "частоту" символов
        # noinspection PyTypeChecker
        heapq.heappush(queue_p, (freq_1 + freq_2, count, Node(left, right)))
        count += 1

    # В итоге остаётся один Узел, который будет являться "корнем" дерева. С
    # него мы начинаем обходить дерево от корня к листьям с помощью функции walk
    code = {}
    if queue_p:
        [(_freq, count, root)] = queue_p
        root.walk(code, '')
    return code


def main():
    string = input('Enter string: ')
    code = huffman_encode(string)
    encoded = ''.join(code[ch] for ch in string)
    print('Length of a string:', len(encoded),
          '\nNumber of characters:', len(code))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)


if __name__ == '__main__':
    main()

"""
Enter string: abcdabc
Length of a string: 14 
Number of characters: 4
a: 01
b: 10
c: 11
d: 00
01101100011011

Enter string: abracadabra
Length of a string: 23 
Number of characters: 5
a: 0
b: 110
c: 100
d: 101
r: 111
01101110100010101101110

Enter string: ssssssssssssss
Length of a string: 14 
Number of characters: 1
s: 0
00000000000000

Enter string: a
Length of a string: 1 
Number of characters: 1
a: 0
0

Enter string: 
Length of a string: 0 
Number of characters: 0


Если честно, код я писала не сама, а с помощью гугла, но я в нём хорошо 
разобралась, поняла, что, для чего и почему, протестировала и дописала 
комментарии. Код мне очень понравился.
"""