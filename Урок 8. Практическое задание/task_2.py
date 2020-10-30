"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""


class LeftNodeError(Exception):
    pass


class RightNodeError(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # self.is_valid(root_obj)

    '''
    Сдесь была идея написать валидатор который делает валидацию, на самом уроке сразу увидел 
    Как реализовать проверку через метод добавления потомка, но хотелось сделать более красиво.
    Такой валидатор скорее всего можно написать если в инициализаторе потомки будут заданны сразу,
    но это нарушит саму суть бинарного дерева. Попробую чуть позже реализовать. 
    '''

    # def is_valid(self, root):
    #     if self.left_child is None:
    #         pass
    #     elif self.left_child > root:
    #         raise IndexError('Left branch can\'t bigger then binary tree root')
    #     if self.right_child is None:
    #         pass
    #     elif self.right_child < root:
    #         raise IndexError('Right branch can\'t smaller then binary tree root. ')

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # Если нету проверяем что-бы левый потомок не был больше корня
            if new_node > self.root:
                # Если новый потомок больше корня выбрасываем ошибку
                raise LeftNodeError('Left branch can\'t bigger then binary tree root')
            else:
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
        if self.right_child is None:
            # Если нету проверяем что-бы правый потомок был блольше корня
            if new_node < self.root:
                # В протинвом случаи выбрасываем ошибку
                raise RightNodeError('Right branch can\'t smaller then binary tree root. ')
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            else:
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


if __name__ == '__main__':
    try:
        r = BinaryTree(8)
        print(r.get_root_val())
        print(r.get_left_child())
        r.insert_left(6)
        print(r.get_left_child())
        print(r.get_left_child().get_root_val())
        r.insert_right(7)
        print(r.get_right_child())
        print(r.get_right_child().get_root_val())
        r.get_right_child().set_root_val(16)
        print(r.get_right_child().get_root_val())
    except LeftNodeError as e:
        print(f'Left branch error: {e}')
    except RightNodeError as e:
        print(f'Right branch error: {e}')
    except Exception as e:
        print('Unknowing error, our team will fix ASAP')
