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
        if new_node > self.root:
            self.insert_right(new_node)
            return
        if self.left_child == None:
                self.left_child = BinaryTree(new_node)
        else:
            if new_node > self.left_child.root:
                self.left_child.insert_right(new_node)
            else:
                self.left_child.insert_left(new_node)

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            self.insert_left(new_node)
            return
        if self.right_child == None:
                self.right_child = BinaryTree(new_node)
        else:
            if new_node > self.right_child.root:
                self.right_child.insert_right(new_node)
            else:
                self.right_child.insert_left(new_node)

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


three_b = BinaryTree(8)
three_b.insert_left(4)
three_b.insert_left(1)
three_b.insert_right(6)  # Некорректная
three_b.insert_right(25)
three_b.insert_left(12)   # Некорректная 
three_b.insert_right(14)
three_b.insert_right(20)
three_b.insert_right(13)
three_b.insert_left(7)
three_b.insert_left(5)

print("Корень: ")
print(three_b.get_root_val())

print("Левая ветвь: ")
print(three_b.get_left_child().root)
print(three_b.get_left_child().get_left_child().root)
print(three_b.get_left_child().get_right_child().root)
print(three_b.get_left_child().get_right_child().get_right_child().root)
print(three_b.get_left_child().get_right_child().get_left_child().root)

print("Правая ветвь: ")
print(three_b.get_right_child().root)
print(three_b.get_right_child().get_left_child().root)
print(three_b.get_right_child().get_left_child().get_right_child().root)
print(three_b.get_right_child().get_left_child().get_right_child().get_right_child().root)
print(three_b.get_right_child().get_left_child().get_right_child().get_left_child().root)

"""
Доработал реализацию вставки узлов для элементов бинарного дерева:
Теперь, при попытке вставки элемента со значением меньше корневого в правую ветвь, он будет перенаправлен в левую ветвь,
Аналогично работает и для элемента со значением больше корневого.
+
Методы insert_left и insert_right, с поп if ... else ...

Вывод: Плучилось автоматизировать вставку любых элементовв бинарное дерево, даже если мы заносим некорректные значения,
то элемент будет перенаправлен в противоположную ветвь.

"""