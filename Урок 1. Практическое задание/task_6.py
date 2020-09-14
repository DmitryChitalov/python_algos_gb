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


class StackClass:
    def __init__(self):
        self.elems = []
        self.elems2 = []
        self.max_size = 3

    def is_empty(self):
        return self.elems == [], self.elems2 == []

    def push_in(self, el):
        self.elems.append(el) if self.stack1_size() < self.max_size else self.elems2.append(el)

    def pop_out(self):
        return self.elems2.pop() if len(self.elems2) != 0 else self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1] if self.elems2 is True else self.elems2[len(self.elems2) - 1]

    def stack1_size(self):
        return len(self.elems)

    def stack2_size(self):
        return len(self.elems2)


if __name__ == '__main__':
    SC_OBJ = StackClass()
    SC_OBJ.push_in('задание_1')
    SC_OBJ.push_in('задание_2')
    SC_OBJ.push_in('задание_3')
    SC_OBJ.push_in('задание_4')
    SC_OBJ.push_in('задание_5')
    SC_OBJ.push_in('задание_6')
    SC_OBJ.push_in('задание_7')

    print(SC_OBJ.get_val())
    print(SC_OBJ.stack1_size())
    print(SC_OBJ.stack2_size())
    print(SC_OBJ.is_empty())
    SC_OBJ.push_in('задание_3')
    print(SC_OBJ.get_val())
    print(SC_OBJ.pop_out())
    print(SC_OBJ.get_val())
