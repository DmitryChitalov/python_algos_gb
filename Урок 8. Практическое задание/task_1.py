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

class HuffmanCode:
    def __init__(self):
        self.__root, self.__left, self.__right = None, None, None
        self._soil, self.__total_dict = {}, {}
        self._str_copy, self.__output = '', ''

    def analyze(self, data):
        self.__data = data
        self.__symb_counter = {}
        self._str_copy = data[:]
        for j in self.__data:
            self.__c = 0
            for i in self.__data:
                if j == i:
                    self.__c += 1
            self.__symb_counter[j] = self.__c
        self._soil = sorted(self.__symb_counter.items(), key=lambda x: x[1])
        del self.__symb_counter
        self.__gross()

    def __gross(self):
        self.__i = 0
        while len(self._soil) > 0 and self.__i < len(self._soil):
            self.__i, self.__c = 0, 0
            self.__left = self._soil[self.__i][0]
            if len(self._soil) > 1:
                self.__right = self._soil[self.__i + 1][0]
            self.left_to_pop = (self._soil[self.__i][0], self._soil[self.__i][1])
            if len(self._soil) > 1:
                self.right_to_pop = (self._soil[self.__i + 1][0], self._soil[self.__i + 1][1])

            if len(self._soil) > 1:
                self.__root = self._soil[self.__i][1] + self._soil[self.__i + 1][1]
            while self.__root > self._soil[self.__i + self.__c][1]:
                self.__c += 1
                if self.__i + self.__c == len(self._soil):
                    break
            self._soil.insert(self.__c, ((self.__left, self.__right), self.__root))
            self._soil.pop(self._soil.index(self.left_to_pop))
            self._soil.pop(self._soil.index(self.right_to_pop))
            self.__i += 1
        return self.__rec(self._soil[0][0])

    def __rec(self, data, code=''):
        self.__data = data
        self._code = code
        if isinstance(self.__data, tuple):
            return self.__rec(data[0], code + '0'), self.__rec(data[1], code + '1')
        else:
            self.__total_dict[data] = self._code
            return

    def show_codes(self):
        for k, v in self.__total_dict.items():
            print(k, v)

    def get_code(self, symbol):
        self._symbol = symbol
        return self.__total_dict.get(self._symbol)

    def encrypt(self):
        for i in self._str_copy:
            for k, v in self.__total_dict.items():
                if i == k:
                    self.__output += v
                    continue
        return self.__output

    def separate_code(self):
        self.__temp_list = []
        for i in self.__output:
            self.__temp_list.append(i)
        self.__i = 4
        while self.__i < len(self.__temp_list):
            self.__temp_list.insert(self.__i, ' ')
            self.__i += 5
        self.__output = ''
        for i in self.__temp_list:
            self.__output += i
        del self.__temp_list, self.__i
        return self.__output


str_1 = 'tried and tested'
str_2 = 'beep boop beer!'

# объявление переменной класса HuffmanCode:
a = HuffmanCode()
# передача строки для обработки:
a.analyze(str_1)
print(f'Вывод закодированной строки:\n{a.encrypt()}')
print(f'Вывод закодированной строки с разделением кода по 4 символа:\n{a.separate_code()}')
print('Вывод кодов символов:')
a.show_codes()
print(f'Запрос кода по символу "r": {a.get_code("r")}')
print(f'Запрос кода по символу "w": {a.get_code("w")}')
print(f'Вывод корня дерева: {a._soil[0][0]}')
