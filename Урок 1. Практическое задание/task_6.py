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


class DequeClass:
    def __init__(self):
        self.elems = []

    def print_queue(self):
        print (self.elems)

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


baze_queue = DequeClass()
work_queue = DequeClass()
# помещаем объекты в очередь
baze_queue.add_to_rear('task1')
baze_queue.add_to_rear('task2')
baze_queue.add_to_rear('task3')
baze_queue.add_to_rear('task4')
baze_queue.add_to_rear('task5')

for i in range(baze_queue.size()):
    work_queue.add_to_front(f"{baze_queue.remove_from_front()} complete")

baze_queue.print_queue()
work_queue.print_queue()
