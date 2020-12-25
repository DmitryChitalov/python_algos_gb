"""
Задание 7.
Задание на закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".


Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях
"""

class QueueClass:
    def __init__(self):
    	self.base = []
    	self.solve = []
    	self.reject = []
			
    def is_empty_base(self):
    	return self.base == []

    def to_queue_base(self, item):
    	self.base.insert(0, item)

    def from_queue_base(self, to_queue):
    	if to_queue == 'solve':
    		task = self.base.pop()
    		self.solve.append(task)
    		return task
    	elif to_queue == 'reject':
    		task = self.base.pop()
    		self.reject.insert(0, task)
    		return task
    	else:
    		print('Выберите очередь solve или reject')
			
    def list_queue(self, queue):
    	if queue == 'base':
    		print(f"Очередь задач {self.base}")
    	elif queue == 'solve':
    		print(f"Список решенных задач {self.solve}")
    	elif queue == 'reject':
    		print(f"Список на доработку {self.reject}")
    	else:
    		print('Выберите один из списков: base, solve, reject')
    
    def from_queue_reject(self):
    	task = self.reject.pop()
    	self.solve.append(task)
    	return task
    			
    def size(self):
      return len(self.base)


ToDoList = QueueClass()
ToDoList.to_queue_base('1')
ToDoList.to_queue_base('2')
ToDoList.to_queue_base('3')
ToDoList.to_queue_base('4')


ToDoList.from_queue_base('solve')
ToDoList.from_queue_base('reject')
ToDoList.from_queue_base('reject')
ToDoList.from_queue_reject()
ToDoList.from_queue_reject()

ToDoList.list_queue('base')
ToDoList.list_queue('reject')
ToDoList.list_queue('solve')

