"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""
"""
Доработкой может быть, например, балансирование дерева при добавлении элементов для поддержания 
минимальной глубины (и, соответственно, минимального времени поиска). В этом случае не нужно 
указывать в какой узел добавляется элемент - узел будет выбираться автоматически

Добавлена функция вставки, автоматически выбирающая узел для вставки по хешу объекта со следующим алгоритмом:
1 - если хеш значения меньше ключа в текущем узле - для вставки выбирается левое поддерево
    - если левый потомок пуст - вставляем узел
2 - иначе для вставки выбирается правое поддерево
    - если правый потомок пуст - вставляем узел
3 - рекурсивный вызов вставки в выбранное поддерево 

функции поиска узла в дереве, обхода дерева, и функция, возвращающая максимальную глубину (количество уровней) дерева 
"""
import random

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        self.key = hash(root_obj)

    # добавить левого потомка
    def insert_left(self, new_node):
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
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

def insert_bal(tree, new_node):
    if hash( new_node ) < tree.key:
        if tree.left_child is None:
            tree.left_child = BinaryTree(new_node)
        else: insert_bal(tree.left_child, new_node)
    else:
        if tree.right_child is None:
            tree.right_child = BinaryTree(new_node)
        else: insert_bal(tree.right_child, new_node)

def find_node(tree, val):
    if tree.key == hash(val):
        return tree
    if hash(val) < tree.key:
        if tree.left_child is None: return None
        return find_node( tree.left_child, val )
    if tree.right_child is None: return None
    return find_node(tree.right_child, val)

def print_tree(node):
    print(str(node.key))
    if node.left_child is None and node.right_child is None:
        print('leaf')
    if not node.left_child is None:
        print('left')
        print_tree(node.left_child)
    if not node.right_child is None:
        print('right')
        print_tree(node.right_child)

def find_depth(tree):
    if tree is None: return 0
    left_max = 1 + find_depth(tree.left_child)
    right_max = 1 + find_depth(tree.right_child)
    if left_max > right_max: return left_max
    return right_max

r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

k = random.randint(0, 49)
val = 0
for i in range(50):
    val = random.randint(0, 100)
    insert_bal( r, val )
    if i == k: k = val + 100

print_tree( r )
d = find_depth( r )
print(f'depth {d}')

node = None
k = random.randint(0, 100)
print(f'Search node with value { k }')
node = find_node( r, k )
if node is None:
    print(f'Node with value { k } not found, inserting in tree')
    insert_bal(r, k)
else: print(f'Node {node.key}')