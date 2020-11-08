"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать,
можно так профилировать и есть ли 'подводные камни'
"""
from pympler import asizeof
from sys import getsizeof


class BasicClass:
    """
    В обычной ситуации в Python в объекты можно добавлять
    новые атрибуты вне описания класса
    """
    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y


BC_OBJ = BasicClass(5, 6)
print(BC_OBJ.__dict__)
print(asizeof.asizeof((BC_OBJ)))
BC_OBJ.param_z = 7
print(BC_OBJ.__dict__)
print(asizeof.asizeof((BC_OBJ)))



class BasicClass:
    __slots__ = ['param_x', 'param_y']
    def __init__(self, param_x, param_y):
        self.param_x = param_x
        self.param_y = param_y

BC_OBJ = BasicClass(5, 6)
print(BC_OBJ.__slots__)
print(asizeof.asizeof(BC_OBJ))
# BC_OBJ.param_z = 7
print(BC_OBJ.__slots__)

