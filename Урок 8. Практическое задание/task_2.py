"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
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
        if new_node < self.root:  # частичная проверка для левого значения - оно должно быть меньше родительского

            # если у узла нет левого потомка
            if self.left_child is None:  # здесь нельзя использовать ==, заменил на is.
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                if new_node > self.get_left_child().get_root_val():  # должно быть больше левого дочернего
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child, self.left_child = self.left_child, tree_obj  # здесь можно в одну строчку
                else:
                    print(f"ветка не добавлена, значение узла ({new_node}) должно быть больше "
                          f"значения дочернего ({self.root})")
        else:
            print(f"ветка не добавлена, значение узла ({new_node}) должно быть меньше "
                  f"значения родительского узла ({self.root})")

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node > self.root:  # частичная проверка правого значения - больше родительского, меньше корневого
            # если у узла нет правого потомка
            if self.right_child is None:  # здесь нельзя использовать ==, заменил на is.
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child, self.right_child = self.right_child, tree_obj  # здесь можно в одну строчку
        else:
            print(f"ветка не добавлена, значение узла ({new_node}) должно быть больше родительского узла ({self.root})")

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)

# print(f"создано веток: {BinaryTree.nodes_created}")


print(r.get_root_val())
print(r.get_left_child())
r.insert_left(9)
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(7)
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.get_left_child().insert_left(3)
print(r.get_left_child().get_left_child().get_root_val())
r.get_left_child().insert_left(2)
