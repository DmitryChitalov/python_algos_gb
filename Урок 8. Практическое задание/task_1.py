from collections import Counter
import heapq


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


def haffman_tree(s):
    """ Функция создания дерева по алгоритму Хаффмана"""
    count = Counter(s)
    queue = []
    for elem, qty in count.most_common()[::-1]:         # сортировка счетчика по возрастанию
        queue.append((qty, len(queue), elem))           # добавление элементов в список (второй элемент - костыль)
    # [(1, 0, 'e'), (1, 1, 'n'), (1, 2, 'o'), (1, 3, 't'), (2, 4, 'd'), (2, 5, 'l'), (3, 6, 'a'), (3, 7, ' ')]

    heapq.heapify(queue)    # создание очереди

    # добавлена переменная l, чтобы убрать элементы left и right из сравнения элементов при их добавлении в очередь
    l = len(queue)

    # Проверка, если строка состоит из одного повторяющего символа.
    if len(queue) != 1:
        while len(queue) > 1:
            qty_1, _l1, left = heapq.heappop(queue)             # извлечение первого эл-та
            qty_2, _l2, right = heapq.heappop(queue)            # извлечение второго

            node = {0: left, 1: right}                          # новый узел
            count_node = qty_1 + qty_2                          # суммирование числа вхождений

            heapq.heappush(queue, (count_node, l,  node))       # добавляем новый узел и число в очередь
            l += 1
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        qty_1, _l1, left = heapq.heappop(queue)             # извлечение первого эл-та
        node = {0: left, 1: None}                           # новый узел
        heapq.heappush(queue, (qty_1, l,  node))       # добавляем новый узел и число в очередь
        l += 1

    # {0: {0: 'a', 1: ' '}, 1: {0: {0: 'd', 1: 'l'}, 1: {0: {0: 'e', 1: 'n'}, 1: {0: 'o', 1: 't'}}}}
    return queue[0][2]


def assign_code(tree):
    """Функция назначения кода на каждую букву  путем рекурсивного прохода по словарю """
    result = dict()

    def out(tree=tree, code=''):
        if not tree or len(tree) < 2:
            result[tree] = code
        else:
            out(tree[0], code=code + str(0))
            out(tree[1], code=code + str(1))

    out(tree)
    return result


def main():
    my_str = 'to land a deal'

    # {'a': '00', ' ': '01', 'd': '100', 'l': '101', 'e': '1100', 'n': '1101', 'o': '1110', 't': '1111'}
    codes_dict = assign_code(haffman_tree(my_str))

    # 1111111001101001101100010001100110000101
    codes_str = str()
    for letter in my_str:
        codes_str += codes_dict[letter]

    # 1111 1110 0110 1001 1011 0001 0001 1001 1000 0101
    encode = ' '.join(codes_str[i:i+4] for i in range(0, len(codes_str), 4))
    print(encode)


if __name__ == "__main__":
    main()