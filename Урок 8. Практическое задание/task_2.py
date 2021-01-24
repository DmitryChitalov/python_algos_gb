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


r = BinaryTree(8)
r.insert_left(4)
r.insert_left(1)
r.insert_right(6)  # Некорректная вставка (Значение меньше корневого)
r.insert_right(25)
r.insert_left(12)   # Некорректная вставка (Значение больше корневого)
r.insert_right(14)
r.insert_right(20)
r.insert_right(13)
r.insert_left(7)
r.insert_left(5)

print("Корень: ")
print(r.get_root_val())

print("Левая ветвь: ")
print(r.get_left_child().root)
print(r.get_left_child().get_left_child().root)
print(r.get_left_child().get_right_child().root)
print(r.get_left_child().get_right_child().get_right_child().root)
print(r.get_left_child().get_right_child().get_left_child().root)

print("Правая ветвь: ")
print(r.get_right_child().root)
print(r.get_right_child().get_left_child().root)
print(r.get_right_child().get_left_child().get_right_child().root)
print(r.get_right_child().get_left_child().get_right_child().get_right_child().root)
print(r.get_right_child().get_left_child().get_right_child().get_left_child().root)

"""
Доработал реализацию вставки узлов для элементов бинарного дерева:
1) Теперь, при попытке вставки элемента со значением меньше корневого в правую ветвь, он будет перенаправлен в левую ветвь,
. Точно такое же поведение сделал для элемента со значением больше корневого.
2) Доработал методы insert_left и insert_right, посредством  последователных и вложенных конструкций if ... else ...
Вывод: ПОлучилось автоматизировать вставку любых элементовв бинарное дерево, даже если мы заносим некорректные значения,
то элемент будет перенаправлен в противоположную ветвь.

Результат работы программы:

Корень: 
8
Левая ветвь: 
4
1
6
7
5
Правая ветвь: 
25
12
14
20
13
"""