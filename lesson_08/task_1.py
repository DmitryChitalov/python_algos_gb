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

# Реализация рассмотренного на уроке алгоритма через ООП


from collections import Counter
from collections import deque


# Вместо словарей будем использовать класс Tree (ничего лишнего, только узлы и потомки)
class Tree:

    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None


class HoffmanCode:

    def __init__(self, string):
        # строка, которую будем кодировать
        self.string = string
        # создаём отсортированную по частоте символов очередь из кортежей (символ, частота)
        # приватный атрибут, внешний доступ к нему не нужен
        self.__order = deque(sorted(Counter(string).items(), key=lambda x: x[1]))
        # заполняем дерево (приватный метод, внешний доступ к нему не нужен)
        self.__tree = self.__fill_tree()  # приватный атрибут, внешний доступ к нему не нужен
        # создаём и заполняем таблицу соответствия символов и кодов
        self.code_table = dict()
        self.__fill_code_table(self.__tree)  # (приватный метод, внешний доступ к нему не нужен)

        # получили экземпляр класса, где можно обратиться к кодируемой строке и таблице кодов

    def __fill_tree(self):
        # заполняем дерево по тому же принципу, что и в решении без ООП, но только вместо словарей
        # будут объекты класса Tree и в итоге мы соберём один объект этого класса
        while len(self.__order) > 1:
            # берём два крайних левых элемента очереди
            left = self.__order.popleft()
            right = self.__order.popleft()
            # и формируем из них дерево, у корня (узла) которого будет значение суммы частот элементов
            node = Tree(left[1] + right[1])
            # и потомками будут элементы без их частот - деревья и символы
            node.left_child = left[0]
            node.right_child = right[0]
            # выбираем, куда вставить дерево:
            for idx, element in enumerate(self.__order):
                if element[1] < node.root:
                    continue
                else:
                    self.__order.insert(idx, (node, node.root))
                    break
            else:
                self.__order.append((node, node.root))  # добавляем итоговый элемент
        return self.__order[0][0]  # возвращаем получившееся дерево

    def __fill_code_table(self, tree, value=''):
        # рекурсивно заполняем таблицу кодов по принципу:
        # если аргумент tree - символ (строка), добавляем в словарь кодов эту строку и получившееся кодовое значение,
        # если аргумент tree не символ (то есть дерево), берём его потомков и передаём их в функцию,
        # а к передаваемому вместе с потомками кодовому значению добавляем 0 или 1
        if isinstance(tree, str):
            self.code_table[tree] = value
            return
        self.__fill_code_table(tree.left_child, f'{value}0')
        self.__fill_code_table(tree.right_child, f'{value}1')

    def encode(self):
        # формируем строку из кодов символов с помощью генератора
        result = (self.code_table[letter] for letter in self.string)
        return ' '.join(result)


if __name__ == '__main__':

    str_1 = HoffmanCode('beep boop beer!')
    str_2 = HoffmanCode('We are the champions, my friend!')

    print(str_1.encode())
    for key, val in str_1.code_table.items():
        print(key, val)

    print()

    print(str_2.encode())
    for key, val in str_2.code_table.items():
        print(key, val)
