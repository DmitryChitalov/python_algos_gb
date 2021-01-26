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
"""
Решение взято из урока,
тема сложная, зашла не с первого раза, если бы не следующий курс реализовал бы все на ООП
Алгоритм разобрал, вроде всё понятно
Спасибо за отличный курс, было интересно!
"""

from collections import Counter, deque


def haffman_tree(s):
    # Считаем уникальные символы.
    count = Counter(s)
    # Сортируем по возрастанию количества повторений.
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sorted_elements) != 1:
        # Цикл для построения дерева
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
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

    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    # словарь - дерево
    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
haffman_code(haffman_tree(s))


# выводим коды для каждого символа
for i in s:
    print(code_table[i], end=' ')
print()