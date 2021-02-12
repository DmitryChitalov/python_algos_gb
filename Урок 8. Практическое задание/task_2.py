"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class InvalidNodeNumber(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # Проверим корреткность new_node
        if new_node >= self.root:
            raise InvalidNodeNumber
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # Проверим корреткность new_node
        if new_node <= self.root:
            raise InvalidNodeNumber
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        # Проверим корреткность obj
        if self.right_child != None:
            if obj <= self.left_child.root:
                raise InvalidNodeNumber
        if self.left_child != None:
            if obj >= self.left_child.root:
                raise InvalidNodeNumber

        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # Высота дерева
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left_child)
            rheight = self.height(node.right_child)

            if lheight > rheight:
                return (lheight + 1)
            else:
                return (rheight + 1)


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
# r.insert_left(40) # получим ошибку
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
# r.insert_right(6) # тоже получим ошибку
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

print(f"Высота дерева - {r.height(r)}\n")

# реализуем дерево из методички
t = BinaryTree(8)
t.insert_left(4)
t.insert_right(12)

print("Создадим дерево из методички")
t.get_left_child().insert_left(2)
t.get_left_child().insert_right(6)
t.get_right_child().insert_left(10)
t.get_right_child().insert_right(14)

t.get_left_child().get_left_child().insert_left(1)
t.get_left_child().get_left_child().insert_right(3)

t.get_left_child().get_right_child().insert_left(5)
t.get_left_child().get_right_child().insert_right(7)

t.get_right_child().get_left_child().insert_left(9)
t.get_right_child().get_left_child().insert_right(11)

t.get_right_child().get_right_child().insert_left(13)
t.get_right_child().get_right_child().insert_right(15)

print(f"Высота дерева - {t.height(t)}")
