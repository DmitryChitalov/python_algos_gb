"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
import sys
import copy
from memory_profiler import profile


class HelloWorld:
	def __init__(self):
		self.hello = "Hello World!!"

	def __call__(self):
		print(self.hello)


def main():
	hi = HelloWorld()
	hi()

	if __name__ == "__main__":
		main()


el = input("Введите елемент: ")

if el.isdigit():
	el = int(el)

print(f"количество ссылов на елемент '{el}'(тип елемента: '{type(el)}'): ", sys.getrefcount(el))
print("1 = Присваивание переменной \n"
      "2 = функция подсчета сылок")
print('size: ', sys.getsizeof(el))


@profile
def func_1():
	x = list(range(100000))
	y = copy.deepcopy(x)
	return y


func_1()

print('#\n' * 3)


@profile
def func_2():
	x = list(range(100000))
	print('size: ', sys.getrefcount(x))
	y = copy.deepcopy(x)
	print('size: ', sys.getrefcount(y))
	del x
	y = None
	return y


func_2()


class Point:
	def __init__(self, x=0, y=0, lst=[]):
		self.x = x
		self.y = y
		self.lst = list(range(100000))

	def __del__(self):
		class_name = self.__class__.__name__
		print(f'{class_name} kill')


@profile
def func():
	pt1 = Point()
	pt2 = pt1
	pt3 = pt1
	print(id(pt1), id(pt2), id(pt3))

	del pt1
	del pt2
	del pt3

func()
