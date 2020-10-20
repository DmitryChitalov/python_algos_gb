"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit, repeat

string = "Выполните различные операции с каждым из объектов и сделайте замеры"
string = string.split(' ')


def norm_dict():
	dict1 = dict()
	for i in range(len(string)):
		dict1[i] = string[i]
	return dict1


def ordered_dict():
	dict2 = OrderedDict()
	for i in range(len(string)):
		dict2[i] = string[i]
	return dict2


norm_dict()
ordered_dict()
# ##############################################
print("normal dict append numbers: ",
      timeit("norm_dict()",
             "from __main__ import norm_dict",
             number=10000))

print("OrderedDict append numbers: ",
      timeit("ordered_dict()",
             "from __main__ import ordered_dict",
             number=10000))
# ###############################################

def del_from_dict(arr):
	x = arr.copy()
	# print(x)
	for el in arr:
		del x[el]

	return x


def del_from_ordereddict(arr):
	x = arr.copy()
	for el in arr:
		del x[el]

	return x


del_from_dict(norm_dict())
del_from_ordereddict(ordered_dict())

# ####################################################################
print("normal dict deleted numbers: ",
      timeit("del_from_dict(norm_dict())",
             "from __main__ import del_from_dict, norm_dict",
             number=10000))

print("OrderedDict deleted numbers: ",
      timeit("del_from_ordereddict(ordered_dict())",
             "from __main__ import del_from_ordereddict, ordered_dict",
             number=10000))
# #####################################################################
# _____________________________________________________________________
print("_"*110)
string2 = "Выполните различные операции с каждым из объектов и сделайте замеры"
string2 = string2.split(' ')
# ##############################
gen_dict = {}
print("_"*110)
for i in range(len(string2)):
	gen_dict[i] = string2[i]
# #################################################################
# ##### создание простого словаря #####


stmt1 = """
some_dict = dict()
for i in range(len(string2)):
	some_dict[i] = string2[i]
"""

stmt1_2 = """
for k, v in gen_dict.items():
	gen_dict.get(k)
	"""

print("append k,v in dict: ",
      repeat(stmt1, 'from __main__ import string2', repeat=4, number=10000))
print("_"*110)
print("extraction value(get) from dict: ",
      repeat(stmt1_2, 'from __main__ import gen_dict', repeat=4, number=10000))
print("_"*110)

# ###################################################################
# ##### создание OrderedDict словаря #####

stmt2 = """
from collections import OrderedDict
some_order_dict = OrderedDict()
for i in range(len(string2)):
	some_order_dict[i] = string2[i]
"""

stmt2_2 = """
from collections import OrderedDict
ord_d = OrderedDict(gen_dict)
for k, v in ord_d.items():
	ord_d.get(k)
	"""

stmt2_3 = """
from collections import OrderedDict
ord_d = OrderedDict(gen_dict)
for k in gen_dict:
	ord_d.move_to_end(k)
	"""

print("append k,v in OrderedDict: ",
      repeat(stmt2, 'from __main__ import string2', repeat=4, number=10000))
print("_"*110)
print("extraction value(get) from OrderedDict: ",
      repeat(stmt2_2, 'from __main__ import gen_dict', repeat=4, number=10000))
print("_"*110)
print("move to end elements OrderedDict: ",
      repeat(stmt2_3, 'from __main__ import gen_dict', repeat=4, number=10000))
print("_"*110)


