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


def tree_of_haffman(string_to_code):
    count = Counter(string_to_code)
    freq_sorted_symbols = list(sorted(count.items(), key=lambda item: item[1]))
    if len(freq_sorted_symbols) != 1:
        while len(freq_sorted_symbols) > 1:
            heft = freq_sorted_symbols[0][1] + freq_sorted_symbols[1][1]
            comb_el = {0: freq_sorted_symbols.pop(0)[0],
                       1: freq_sorted_symbols.pop(0)[0]}
            for i, _count in enumerate(freq_sorted_symbols):
                if heft > _count[1]:
                    continue
                else:
                    freq_sorted_symbols.insert(i, (comb_el, heft))
                    break
            else:
                freq_sorted_symbols.append((comb_el, heft))
    else:
        heft = freq_sorted_symbols[0][1]
        comb_el = {0: freq_sorted_symbols.popleft()[0], 1: None}
        freq_sorted_symbols.append((comb_el, heft))
    return freq_sorted_symbols[0][0]


trans_table = dict()


def code_of_haffman(bush, pathway=''):
    if not isinstance(bush, dict):
        trans_table[bush] = pathway
    else:
        code_of_haffman(bush[0], pathway=pathway + '0')
        code_of_haffman(bush[1], pathway=pathway + '1')


phrase = "abracadabra"
# phrase = "beep boop beer!"
code_of_haffman(tree_of_haffman(phrase))

for symbols in phrase:
    print(trans_table[symbols], end=' ')
print()

'''
Идею кодирования понял (в том числе увидел, что несмотря на разную длину закодированных символов, они всё же взаимно 
устроены таким образом, что строку возможно раскодировать даже не зная длины очередного символа).
Немного переделал приведённый вами алгоритм.
'''
