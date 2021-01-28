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


def add_tree(count = 1):
    while True:
        start = input('Чтобы довавить значение надмите "enter", чтобы закончить введите любой символ: ')
        if start == "":
            if count == 1:
                n_root = int(input('Введите корневое значение:'))
                r = BinaryTree(n_root)
                print(r.get_root_val())
                print(r.get_left_child())
                count += 1
            else:
                n_root = int(input('Введите корневое значение:'))
                r.get_right_child().set_root_val(n_root)
                print(r.get_right_child().get_root_val())
            stop = 1
            while True:
                n = int(input('Введите левое значение:'))
                if n_root >= n:
                    r.insert_left(n)
                    print(r.get_left_child())
                    print(r.get_left_child().get_root_val())

                    while stop == 1:
                        n = int(input('Введите правое значение:'))
                        if n_root <= n:
                            r.insert_right(n)
                            print(r.get_right_child())
                            print(r.get_right_child().get_root_val())
                            break
                        else:
                            print(f'Вы ввели маленькое значение, введите значение больше {n_root}.')
                    break
                else:
                    i = input('Вы ввели подходящее значение для правой части. Чтобы довабить егов правую часть введите "+", или чтобы ввести зановаво введите "-": ')
                    if i == "+":
                        r.insert_right(n)
                        print(r.get_right_child())
                        print(r.get_right_child().get_root_val())
                        stop = 0
        else:
            break
    return
add_tree()
