bigtxt = """
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

from collections import Counter, deque
from bisect import insort_left

txt = 'A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED'


class Node:
    __slots__ = 'key', 'val', 'left', 'right'

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is None and self.right is None:
            return f'<{self.key}, {self.val}>'
        else:
            return f'<{self.key}, {self.left}, {self.right}>'

    # Весь класс делался ради этого метода. К сожалению,
    # модуль bisect не имеет параметра key, и поэтому
    # не работает со вложенными списками (кортежами).
    # Остальные методы необязательны и сделаны ради
    # удобства использования и отладки
    def __lt__(self, n):
        return self.key < n.key

    def __add__(self, n):
        return Node(self.key + n.key, None, self, n)

    __repr__ = __str__


def build_tree(txt):
    vocab = deque(sorted(Node(n, c) for c, n in Counter(txt).items()))
    while len(vocab) > 1:
        a = vocab.popleft()
        b = vocab.popleft()
        insort_left(vocab, a + b)
    return vocab[0]


tree = build_tree(txt)
print(tree)
# ---
# <46, <20, <10, _>, <10, D>>, <26, <11, A>, <15, <7, E>, <8, <2, C>, <6, B>>>>>
# ---


# n -- дерево, полученное на предыдущем шаге.
# В рекурсивных вызовах это узел дерева.
def fill_dict(n, dicto=None, code=''):
    if dicto is None:
        dicto = {}
    if n.val is not None:
        dicto[n.val] = code
        return dicto
    else:
        fill_dict(n.left, dicto, code + '0')
        fill_dict(n.right, dicto, code + '1')
        return dicto


dicto = fill_dict(tree)
print(dicto)
# ---
# {'_': '00', 'D': '01', 'A': '10', 'E': '110', 'C': '1110', 'B': '1111'}
# ---


def encode(txt):
    tree = build_tree(txt)
    dicto = fill_dict(tree)
    return ''.join(dicto[c] for c in txt), dicto


code, _ = encode(txt)
print(code)
# ---
# 1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001
# ---

# Дальше необязательная часть, которая трансформирует произвольный
# текст в сжатый текст. Из-за необходимости вставлять результат
# в код программы, при этом не переходя в unicode,
# приходится ограничиваться диапазоном 6 бит (64 символа),
# что ухудшает сжатие. Запись в виде binary уменьшает строку
# еще на 25%


class InvalidCode(Exception):
    pass


def decode(txt, dicto):
    revdict = {v: k for k, v in dicto.items()}
    minlen = min(map(len, revdict.keys()))
    maxlen = max(map(len, revdict.keys()))
    ret = []
    idx = 0
    while idx < len(txt):
        # Здесь используется ключевое свойство кодов Хаффмана,
        # ни один символ не является подстрокой другого. Поэтому
        # при чтении 10 мы можем быть уверенными, что это
        # именно символ 10, а не начало символа 1011
        for length in range(minlen, maxlen + 1):
            code = txt[idx:idx + length]
            sym = revdict.get(code)
            if sym:
                ret.append(sym)
                idx += length
                break
        else:
            raise InvalidCode(idx)
    return ''.join(ret)


# Функция переводит строку символов "0" и "1" в текст.
# в этой функции 6 означает 6 бит, 48 добавляем, чтобы
# продвинуть символы в цифро-буквенный диапазон
def code2str(cod, width=64):
    # Последний символ не должен содержать нулей
    cod += '111111'
    ret = ''.join(
        chr(48 + int(cod[i:i + 6], 2))
        for i in range(0, len(cod), 6))
    return '\n'.join(
        ret[i:i + width]
        for i in range(0, len(ret), width))


# Функция переводит текст в строку символов "0" и "1".
def str2code(enctxt):
    encstr = ''.join(enctxt.split('\n'))
    return (
        ''.join(
            f'{(ord(c)-48):06b}'
            for c in encstr[:-1])
        + f'{(ord(encstr[-1])-48):b}')[:-6]


def encode_ascii(txt):
    code, dicto = encode(txt)
    return code2str(code, width=48), dicto


textcode, dicto = encode_ascii(bigtxt)
print(textcode)
# ---
# nG5>[FM5dKjmeOh9iX^WXgH1ke[>UR0oFAB@LG=:JVV]?:@g
# bQ=j]7Ke4?5RSl^Zd;Te<Ma@_Jg_cEhA]kZVhlBJgRka3APE
# k\o=E41RN2FS`7j[a;>knROU]c_cOP]UnEngV64V_[e23UB^
# :g^I41Vo5H]g^:g^H9?JkFM<CfXSPi?Jd>blCLMVHA`?=n<Y
# j?oo_FeSGR1@_lHJ7jH9?JkFNo\QX;4h:][<6nGfgLlg6:[\
# BiNlk;JlaUbmi^nMUS\;mEGT^]X_E1I=]QIo;1FQLVXPmNbe
# B_47HZ2VRjcl\k_j9nFg>o0j_l5FeUlKi^7RCFlG@>[o17_A
# ?`E>YPmhVZ@69h?4HL72Vg]g9WnA0Lkle^4o<dKD@KVA^WZ1
# bYf\_SOO=egc\\K_U\Xa0HWP7PZMF\JS=ica@:4WUSfQi_47
# KoWJaZ>kCl\jV63OGCR3\E1CAMIn6c=X\\o6O2V\I3OO1
# ---

inp = r"""nG5>[FM5dKjmeOh9iX^WXgH1ke[>UR0oFAB@LG=:JVV]?:@g
bQ=j]7Ke4?5RSl^Zd;Te<Ma@_Jg_cEhA]kZVhlBJgRka3APE
k\o=E41RN2FS`7j[a;>knROU]c_cOP]UnEngV64V_[e23UB^
:g^I41Vo5H]g^:g^H9?JkFM<CfXSPi?Jd>blCLMVHA`?=n<Y
j?oo_FeSGR1@_lHJ7jH9?JkFNo\QX;4h:][<6nGfgLlg6:[\
BiNlk;JlaUbmi^nMUS\;mEGT^]X_E1I=]QIo;1FQLVXPmNbe
B_47HZ2VRjcl\k_j9nFg>o0j_l5FeUlKi^7RCFlG@>[o17_A
?`E>YPmhVZ@69h?4HL72Vg]g9WnA0Lkle^4o<dKD@KVA^WZ1
bYf\_SOO=egc\\K_U\Xa0HWP7PZMF\JS=ica@:4WUSfQi_47
KoWJaZ>kCl\jV63OGCR3\E1CAMIn6c=X\\o6O2V\I3OO1"""

print(len(bigtxt), len(inp))
# ---
# 566 486
# ---

# Для расшифровки нужен словарь, для экономии места
# не распечатываем его, а берем как результат функции
def decode_ascii(textcode, dicto):
    code = str2code(textcode)
    return decode(code, dicto)


print(decode_ascii(inp, dicto))
# ---
# Задание 1.
# Реализуйте кодирование строки "по Хаффману".
# У вас два пути:
# 1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
# Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
# и оптимизации.
# КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
# 2) тема понятна? постарайтесь сделать свою реализацию.
# Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
#
# ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
# Но постарайтесь обойтись без них.
# ---
