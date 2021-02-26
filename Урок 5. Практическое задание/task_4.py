"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

from collections import OrderedDict
from timeit import timeit


class Test1:
    elements_count: int

    def __init__(self, dictionary):
        self.elements_count = len(dictionary)
        self.source = dictionary
        self.dictionary = self.source.copy()

    def add_to_dict(self):
        new_dict = dict()
        for index in range(20):
            new_dict[str(index)] = index

    def enumerate(self):
        temp = None
        for key, value in self.dictionary.items():
            temp = key, value

    def popitem(self):
        item = self.dictionary.popitem()

    def sort(self):
        return sorted(self.dictionary.items(), key=lambda item: item[1])

    def get_from_dict(self):
        for index in range(self.elements_count):
            self.dictionary.get(str(index))

    def update_dict(self):
        self.dictionary.update({str(n): True for n in range(1000, 2000)})

    def time_test(self, message: str, func_name: str, times: int):
        func_name_1 = f"self.{func_name}()"
        self.dictionary = self.source.copy()
        print(message, func_name_1, '\t\t\t', timeit(func_name_1, number=times, globals=locals()))


dict1 = {str(n): True for n in range(10000)}
test1 = Test1(dict1)
test_ordered = Test1(OrderedDict(dict1))
for func_name in ['add_to_dict', 'enumerate', 'popitem', 'sort', 'get_from_dict', 'update_dict']:
    test1.time_test('dict:\t\t\t', func_name, 10000)
    test_ordered.time_test('ordered dict:\t', func_name, 10000)
    print()

'''
dict:			 self.add_to_dict() 		 0.10792240000000002
ordered dict:	 self.add_to_dict() 		 0.1038404

dict:			 self.enumerate() 			 12.2903891
ordered dict:	 self.enumerate() 			 22.7077752 - ЗАМЕТНО МЕДЛЕННЕЕ

dict:			 self.popitem() 			 0.004468700000003878
ordered dict:	 self.popitem() 			 0.011733700000000624 - ЗАМЕТНО МЕДЛЕННЕЕ

dict:			 self.sort() 			     27.7094107
ordered dict:	 self.sort() 			     35.1296571 - ЗАМЕТНО МЕДЛЕННЕЕ

dict:			 self.get_from_dict() 		 68.21986580000001
ordered dict:	 self.get_from_dict() 		 59.69967599999998

dict:			 self.update_dict() 		 5.506209200000001
ordered dict:	 self.update_dict() 		 7.281239699999986 - МЕДЛЕННЕЕ

OrderedDict медленнее во многих сценариях
Смысла исп-ть OrderedDict в Python 3.6 и более поздних версиях нету т.к. dict в этом случае сохраняет порядок.
'''
