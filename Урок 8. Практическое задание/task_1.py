"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".

У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ БУДЕТ!

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter, deque


def huffman_tree(value):
    # Считаем уникальные символы.
    count = Counter(value)
    # Сортируем по возрастанию количества повторений.

    sorted_items = deque(sorted(count.items(), key=lambda item: item[1]))
    # Проверка, состоит-ли строка из одного повторяющего символа.

    if len(sorted_items) != 1:
        # Цикл для построения дерева
        while len(sorted_items) > 1:
            # далее цикл объединяет два крайних левых элемента
            # Вес объединенного элемента (накопленная частота)
            weight = sorted_items[0][1] + sorted_items[1][1]

            # удалям их из "sorted_items" (из очереди).
            # combined_element - объединенный элемент
            combined_element = {0: sorted_items.popleft()[0],
                                1: sorted_items.popleft()[0]}

            # Ищем место для вставки объединенного элемента
            for el, _count in enumerate(sorted_items):
                if weight > _count[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    sorted_items.insert(el, (combined_element, weight))
                    break
            else:
                # Добавляем объединенный корневой элемент после завершения работы цикла
                sorted_items.append((combined_element, weight))
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sorted_items[0][1]
        combined_element = {0: sorted_items.popleft()[0], 1: None}
        sorted_items.append((combined_element, weight))
    return sorted_items[0][0]


code_table = dict()


def huffman_algorithm(tree, path=''):
    # Если элемент не словарь, значит мы достигли крайнего символа
    # и заносим его, и его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        huffman_algorithm(tree[0], path=f'{path}0')
        huffman_algorithm(tree[1], path=f'{path}1')


# строка для кодирования
val = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
huffman_algorithm(huffman_tree(val))

# выводим код для каждого символа
for v in val:
    print(code_table[v], end=' ')
print()

val = 'Проверка кода на другом примере!'
huffman_algorithm(huffman_tree(val))
for v in val:
    print(code_table[v], end=' ')
print()
