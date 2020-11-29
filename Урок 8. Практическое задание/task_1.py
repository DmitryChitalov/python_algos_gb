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

from collections import Counter, deque


class HaffmanEncoding:

    def __init__(self, text):
        self.text = text
        self.sorting()
        self.binary_tree()
        self.creating_dict()
        self.encoding_dictionary()

    def sorting(self):
        """получаем упорядоденный список"""
        ranked_list = Counter(self.text)
        sorted_elements = deque(sorted(ranked_list.items(), key=lambda item: item[-1]))
        self.sorted_characters = sorted_elements

    def binary_tree(self):
        """строим бинарное дерево"""
        if len(self.sorted_characters) > 1:
            while len(self.sorted_characters) > 1:
                first_el = self.sorted_characters.popleft()
                second_el = self.sorted_characters.popleft()
                new_el = ([first_el[0], second_el[0]], first_el[1] + second_el[1])
                weight_new_el = first_el[1] + second_el[1]
                for i in range(len(self.sorted_characters)):
                    if weight_new_el > self.sorted_characters[i][1]:
                        continue
                    else:
                        self.sorted_characters.insert(i, new_el)
                        break
                else:
                    self.sorted_characters.append(new_el)
        elif len(self.sorted_characters) == 1:
            first_el = self.sorted_characters.popleft()
            self.sorted_characters = deque([([first_el[0], ''], first_el[1])])
        else:
            self.sorted_characters = deque([([], 0)])

    def creating_dict(self):
        """создание словаря с путями"""
        def haffman_code(sorted_list, path=''):
            if len(sorted_list) == 2:
                haffman_code(sorted_list[0], path + '0')
                haffman_code(sorted_list[1], path + '1')
            else:
                self.code_table[sorted_list] = path

        self.code_table = {}
        tree = self.sorted_characters[0]
        if tree[1] > 0:
            haffman_code(tree[0])

    def encoding_dictionary(self):
        """вывод полученных данных"""
        print(f'Исходная строка: {self.text}')
        print(f'Соответвие кодов Хаффмана - символам:\n{self.code_table}', end=' ')
        self.new_code = []
        for i in self.text:
            self.new_code.append(self.code_table[i])
        print(f"\nПолученный код по Хаффману: {''.join(self.new_code)}")


word = "beep boop beer!"

word_1 = HaffmanEncoding(word)

"""Решение сделал через ООП
Опирался на пример с урока, а также варианты решения из интернета.
Код получился объемным, а также на мой взляд, не оптимальным.
Хотел провернуть вариант, при котором получая новый элемент мы вставляем его в старый список и deque сортирует
его снова, таким образом можно было бы обойтись без цикла for для поиска места для вставки.
Но, к сожалению, такое решение не получилось реализовать.

Исходная строка: beep boop beer!
Соответвие кодов Хаффмана - символам:
{'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'} 
Полученный код по Хаффману: 0011111010100001101110101000111110001001
"""
