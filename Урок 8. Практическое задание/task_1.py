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
"""
Задачу решал сам, с помощью конспектов и того что видел на последнем уроке при разъяснении дз.
(и немного взял у Хирьянов в плане рекурсии.)
"""
import collections


def counter_symbol(my_line_in: str) -> dict:
    """
    функция получает строку, подсчитывает количество схождений каждого символа и
     возвращяет отсортированный dict
    :param my_line_in: str
    :return: list
    """
    obj = collections.Counter(my_line_in)
    return dict(sorted(obj.items(), key=lambda x: x[1]))


def coder_line(dict_symbol_in: dict) -> collections.deque:
    """
    функция получает словарь, создает очередь и подготавливает ее для дальнейшей обработки
    :param dict_symbol_in: dict
    :return: deque
    """
    deque_symbols = collections.deque(dict_symbol_in.items())
    while len(deque_symbols) > 1:
        first_var = deque_symbols.popleft()
        second_var = deque_symbols.popleft()
        third_var = [first_var, second_var, first_var[-1] + second_var[-1]]
        if len(deque_symbols) == 0:
            deque_symbols.append(third_var)
            break
        for idx, val in enumerate(deque_symbols):
            if idx == len(deque_symbols) - 1:
                deque_symbols.append(third_var)
                break
            if third_var[-1] < val[-1]:
                deque_symbols.insert(idx, third_var)
                break

    return deque_symbols


def create_path(list_haffman_in: list, prefex='', dict_haf=collections.defaultdict(str)) -> collections.defaultdict:
    """
    функция получает подготовленный список с частотами, обрабатывает и возвращяет словарь с кодами символов
    :param list_haffman_in: list
    :param prefex: str
    :param dict_haf: collections.defaultdict
    :return: collections.defaultdict
    """
    if type(list_haffman_in) == int:
        return
    if len(list_haffman_in) == 1:
        dict_haf[list_haffman_in] = prefex[0:-1]
        return dict_haf
    create_path(list_haffman_in[0], prefex + '0')
    create_path(list_haffman_in[1], prefex + '1')
    return dict_haf


if __name__ == '__main__':
    my_line = "beep boop beer!"

    dict_symbol = counter_symbol(my_line)
    print(dict_symbol)
    deque_haffman = coder_line(dict_symbol)
    print(deque_haffman)
    print(create_path(*deque_haffman))
