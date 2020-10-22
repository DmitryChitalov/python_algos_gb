"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

"""
Нашёл интерстный инструмент, recordclass он основан не на __slot__ как все что встречалось до него а на цикличиском
сборщике мусора. Ещё там в этой статье был вариант через Cython, но с ним у меня как-то не сложилось)
"""

import sys
from recordclass import dataobject


class Pooint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


ob = Pooint(1, 2, 3)
print(sys.getsizeof(ob))


class Point(dataobject):
    x: int
    y: int
    z: int


ob_1 = Point(1, 2, 3)
print(sys.getsizeof(ob_1))