"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class PilePlates:
	def __init__(self, size):
		self.elems = [[]]
		self.size = size
		
	def is_empty(self):
		return self.elems == [[]]

	def push_in(self, el):
		count = len(self.elems) - 1
		if len(self.elems[count]) < self.size:
			self.elems[count].append(el)
		else:
			self.elems.append([])
			self.elems[count + 1].append(el)
			
	def pop_out(self):
		count = len(self.elems) - 1
		last_el = self.elems[count].pop()
		if len(self.elems[count]) == 0:
			self.elems.pop()
		return last_el

	def get_val(self):
		return self.elems[len(self.elems) - 1]

	def stack_size(self):
		return len(self.elems)	
		
		
first = PilePlates(7)
first.push_in(3)
first.push_in(4)
first.push_in(5)
first.push_in(7)
first.push_in(9)
first.push_in(10)
first.push_in(11)
first.push_in(12)
first.push_in(13)

print(first.elems)
print(first.pop_out())
print(first.pop_out())
print(first.pop_out())
print(first.pop_out())
print(first.pop_out())
print(first.pop_out())
print(first.elems)
print(first.stack_size())
print(first.is_empty())
