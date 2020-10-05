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


class Stack():
    """
    Не опусташенные стеки складываюся в отдельный список и реализован дополнительный метод опусташения
    стека по номеру стека.
    """

    def __init__(self):
        self.stack_master = []
        self.stack_ = []

    def add_elem(self, elem, flag=10):
        if len(self.stack_) != flag:
            self.stack_.append(elem)

        else:
            self.stack_master.append(self.stack_)
            self.stack_ = []
            self.stack_.append(elem)

    def return_stack(self):
        return self.stack_

    def return_master(self):
        return self.stack_master

    def pop_out_master(self, num_stack=0):
        return self.stack_master[num_stack].pop()

    def pop_out_(self):
        return self.stack_.pop()

    def stack_count(self):
        return len(self.stack_master + self.stack_)

    def is_empty(self):
        return self.stack_ == []


class1 = Stack()
for i in range(30):
    class1.add_elem(f'qwe{i}')

print(class1.return_stack())
print(class1.return_master())
print(class1.pop_out_master(0))
print(class1.pop_out_master(0))
print(class1.pop_out_master(0))
print(class1.return_master())
print(class1.pop_out_())
print(class1.pop_out_())
print(class1.return_stack())
