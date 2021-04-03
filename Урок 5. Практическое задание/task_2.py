"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from collections import deque

HEXES = list('0123456789ABCDEF')
INTS = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15}


# я знаю про int(x, 16), но в изобретении велосипеда
# надо быть последовательным
def hex2int(hex):
    return sum(16**i * INTS[d] for i, d in enumerate(reversed(hex)))


def int2hex(hex, base=16):
    # хотя можно было обойтись reversed(list)
    ret = deque()
    while True:
        if hex == 0:
            break
        ret.appendleft(HEXES[hex % base])
        hex //= base
    return list(ret)


class Hex:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.digits = int2hex(arg)
        elif isinstance(arg, str):
            self.digits = list(arg.upper())
        elif isinstance(arg, list):
            self.digits = [d.upper() for d in arg]
        else:
            raise ValueError("Invalid initialization type")

    def __repr__(self):
        return f'Hex({repr(self.digits)})'

    def __str__(self):
        return ''.join(self.digits)

    def __int__(self):
        return hex2int(self.digits)

    def __add__(self, other):
        return Hex(int(self) + int(other))

    def __mul__(self, other):
        return Hex(int(self) * int(other))


h1 = Hex('A2')
h2 = Hex('C4F')
print(h1 + h2)
print(h1 * h2)
# ---
# CF1
# 7C9FE
# ---

# Если выше была просто необязательная часть, то дальше уже
# полная отсебятина. Теперь калькулятор разбирает целую строчку.
# Создание мини-языка по моему мнению является одним из
# полезнейших упражнений для освоения алгоритмов и
# структур данных. Если бы в geekbrains практиковались
# курсовые работы, я выбрал бы эту тему.

# Пример работы:
# > 7+7
# 7 + 7 = E
# > 7*7
# 7 * 7 = 31
# > dead + beef
# DEAD + BEEF = 19D9C


class HexParser:
    def __init__(self):
        self.digits = []
        self.hex = None

    def __bool__(self):
        return bool(self.digits)

    def __str__(self):
        return str(self.digits)

    def accept(self, c):
        if c in INTS:
            self.digits.append(c)
            return True
        else:
            if bool(self):
                self.hex = Hex(self.digits)
        return False


OPS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}


class OpParser:
    def __init__(self):
        self.sym = None
        self.op = None

    def __bool__(self):
        return self.sym is not None

    def __str__(self):
        return str(self.sym)

    def accept(self, c):
        if (self.sym is None) and (c in OPS):
            self.sym = c
            self.op = OPS[c]
            return True
        return False


def parse(stream, parsers):
    for p in parsers:
        while True:
            try:
                c = stream.popleft()
                if not p.accept(c):
                    stream.appendleft(c)
                    break
            except IndexError:
                p.accept('')
                break


class Calc:
    def __init__(self):
        print('Type "exit" to quit')

    def loop(self, inp):
        if inp == 'exit':
            return False
        # Это грамматика языка, пока лишь последовательность элементов
        grammar = [HexParser(), OpParser(), HexParser()]
        # В настоящем языке должны быть две очереди:
        # символы -> токены -> AST
        # Здесь же только одна очередь
        stream = deque(inp.replace(' ', '').upper())
        parse(stream, grammar)
        h1, op, h2 = grammar
        if all(grammar):
            # Здесь должна быть обработка AST, но у меня пока
            # только обработка последовательности
            print(
                f'{h1.hex} {op.sym} {h2.hex} = '
                + str(Hex(op.op(int(h1.hex), int(h2.hex)))))
        else:
            print("Ошибка в выражении")
        return True


calc = Calc()
while calc.loop(input('> ')):
    pass
