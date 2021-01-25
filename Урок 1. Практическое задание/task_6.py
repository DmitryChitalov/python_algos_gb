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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def get_str(self):
        res = '[' + str(len(self.elems)) +'], <'
        for rec in self.elems:
            res += rec + ', '
        res += '>'
        return res

class TaskBoardClass:
    def __init__(self):
        self.base        = QueueClass()
        self.to_complete = QueueClass()
        self.finished    = QueueClass()

    def add(self, item):
        self.base.to_queue(item)

    def move_to_complete(self):
        buf = self.base.from_queue()
        self.to_complete.to_queue(buf)

    def complete(self):
        buf = self.to_complete.from_queue()
        self.finished.to_queue(buf)

    def finish(self):
        buf = self.base.from_queue()
        self.finished.to_queue(buf)

    def __repr__(self):
        res = ''
        res += 'Базовая очередь: '+self.base.get_str()+'\n'
        res += 'Очередь на доработку: '+self.to_complete.get_str()+'\n'
        res += 'Решенные задачи: '+self.finished.get_str()+'\n'
        return res
##################################################
tb_obj = TaskBoardClass()
tb_obj.add('Вскопать грядки')
tb_obj.add('Вскопать поле для картошки')
tb_obj.add('Починить забор')
tb_obj.add('Вскопать клумбу')
print(tb_obj)
tb_obj.move_to_complete()
tb_obj.move_to_complete()
tb_obj.finish()
print(tb_obj)
tb_obj.finish()
tb_obj.complete()
tb_obj.complete()
print(tb_obj)
##################################################

