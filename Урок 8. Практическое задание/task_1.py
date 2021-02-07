"""
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
from collections import Counter


class HafTree:
    """
    Класс дерева для алгоритма Хаффмана
    """
    def __init__(self, val, name):
        self.val, self.name = val, name
        self.left, self.right = None, None

    def add_left(self, obj):
        self.left = obj

    def add_right(self, obj):
        self.right = obj


def haf_build_tree(string):
    """
    Класс для создания дерева алгоритма Хаффмана по входной строке

    :param string: Входная строка
    :return: Указатель на корень дерева алгоритма Хаффмана
    """
    cnt = list(Counter(string).items())
    cnt = sorted(cnt, key=lambda x: x[1])

    # cnt - список из листьев будущего дерева
    cnt = [HafTree(elem[1], elem[0]) for elem in cnt]
    root = None

    # если слишком короткое сообщение
    if len(cnt) == 1:
        return cnt[0]

    # Создаем новые поддеревья по буквам строки в цикле
    # На каждой итерации схлопываем 2 элемента списка cnt в один и добавляем к дереву
    # В конце root будет являться корнем общего дерева, а длина списка cnt будет = 1
    while len(cnt)-1:
        root = HafTree(cnt[0].val + cnt[1].val, cnt[0].name + cnt[1].name)
        root.add_left(cnt[0])
        root.add_right(cnt[1])

        cnt = cnt[1:]
        cnt[0] = root
        cnt = sorted(cnt, key=lambda x: x.val)

    return root


def get_haf_code(rt):
    """
    Функция для рекурсивного обхода дерева алгоритма Хаффмана
    И получения кодов символов

    :param rt: ссылка на корень дерева
    :return: список словарей {буква: код}
    """
    res = []

    def rec_go_haf(root, code=''):
        """
        Рекурсивная функция обхода
        """
        nonlocal res

        # если дошли до листьев
        if not root.left or not root.right:
            res.append({root.name: code})
            return
        # иначе - идем дальше (лево - 0, право - 1)
        rec_go_haf(root.left, code + '0')
        rec_go_haf(root.right, code + '1')

    # обработка случая, когда в сообщении только одна буква
    if rt.left is None or rt.right is None:
        return [{rt.name: '0'}]

    rec_go_haf(rt)
    return res


def main(string):
    return get_haf_code(haf_build_tree(string))


if __name__ == '__main__':
    print(main(input('Введите строку для анализа: ')))


