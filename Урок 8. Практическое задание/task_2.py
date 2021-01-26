"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
"""Доработки: 
Разбил на две части: Классы ('Узел', 'Дерево')
Создал функцию прохода 'по дереву'
На выходе строка вида бинарного дерева {8: {6: {5: {2: -} -} {7: -} -} {12: {10: -} -} -}
"""
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Bin_Tree:
    def __init__(self):
        self.root = None
        self.info = ''

    def store_info(self, string):
        self.info = f"{self.info} {string}"

    def insert_node(self, value):
        new_node = Node(value)
        new_node.data = value
        return new_node

    def get_around(self, j=None):
        if not j:
            j = self.root
        value_left = j.left
        value_right = j.right
        self.store_info('{' + str(j.data) + ':')

        if value_left:
            # self.store_info(f'lf{j.data}')  # Получение строки со вставками (+ строки 29, 33)
                                        # {8: lf8 {6: lf6 {5: lf5 {2: -} -} Rt6 {7: -} -} Rt8 {12: lf12 {10: -} -} -}
            self.get_around(value_left)
        if value_right:
            # self.store_info(f'Rt{j.data}')
            self.get_around(value_right)
        self.store_info('-}')
        return f"{self.info}"


tr1 = Bin_Tree()
tr1.root = tr1.insert_node(8)
tr1.root.left = tr1.insert_node(6)
tr1.root.right = tr1.insert_node(12)
tr1.root.left.left = tr1.insert_node(5)
tr1.root.left.left.left = tr1.insert_node(2)
tr1.root.left.right = tr1.insert_node(7)
tr1.root.right.left = tr1.insert_node(10)
print(tr1.get_around())
