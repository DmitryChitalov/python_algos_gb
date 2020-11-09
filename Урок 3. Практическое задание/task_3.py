"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib


class UniqSubstring:
    def __init__(self):
        self.input_str = input('Введите строку: ')
        self.count = 0
        self.result = set()

    def __str__(self):
        return f'Кол-во подстрок в введенной строке: {len(self.result) - 1}'

    @staticmethod
    def result_hash(item):
        result = hashlib.sha256(item.encode('utf-8')).hexdigest()
        return result

    def number_of_substring(self):
        self.count = 0
        while self.count < len(self.input_str):
            j = 0
            while j < len(self.input_str):
                item = self.input_str[self.count:len(self.input_str) - j]
                if item != '':
                    self.result.add(self.result_hash(item))
                j += 1
            self.count += 1
        return self.result


some_str = UniqSubstring()
some_str.number_of_substring()
print(some_str)
