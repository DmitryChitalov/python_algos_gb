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
    def __init__(self, name):
        self.elems = []
        self.name = name

    def __str__(self):
        rez = '{:-^11}\n'.format(self.name)
        for x in range(len(self.elems)):
            rez += self.elems[x] .format(self.elems) + '\n'
        return rez

    def is_empty(self):
        return self.elems == []

    def push_front(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        self.elems.insert(0, el)

    def push_back(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def stack_size(self):
        return len(self.elems)


if __name__ == '__main__':

    qc_basic = QueueClass('basic')
    qc_decided = QueueClass('decided')
    qc_rework = QueueClass('rework')

    # Добавляем таски на доску 'basic'
    qc_basic.push_back('task_1')
    qc_basic.push_back('task_2')
    qc_basic.push_back('task_3')
    qc_basic.push_back('task_4')
    qc_basic.push_back('task_5')

    # Выполненные задачи переносим на доску 'decided'
    qc_decided.push_back(qc_basic.pop_out())
    qc_decided.push_back(qc_basic.pop_out())

    # Выполненные задачи переносим на доску 'rework'
    qc_rework.push_back(qc_basic.pop_out())

    print(qc_basic)
    print(qc_decided)
    print(qc_rework)


