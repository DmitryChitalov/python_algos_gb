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


class StackClass:
    def __init__(self, limit):
        self.elems = []
        self.limit = limit

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems) < self.limit:
            self.elems.append(el)
        elif len(self.elems) == self.limit:
            try:
                self.newinstance.is_empty()
                self.newinstance.push_in(el)
            except:
                self.newinstance = StackClass(self.limit)
                self.newinstance.push_in(el)

    def pop_out(self):
        try:
            return self.elems.pop()
        except IndexError:
            return None

    def get_val(self):
        try:
            return self.elems[len(self.elems) - 1]
        except IndexError:
            return None

    def stack_size(self):
        return len(self.elems)

    def __str__(self):
        result = ''
        for i in list(reversed(self.elems)):
            result += f'{i}\n{"*"*100}\n'
        return result


stack_1 = StackClass(2)
print(stack_1.is_empty())
print(stack_1.get_val())
stack_1.push_in(1)
stack_1.push_in(2)
stack_1.push_in(3)
stack_1.push_in(4)
stack_1.push_in(5)
stack_1.push_in(6)
stack_1.push_in(7)
stack_1.push_in(8)
stack_1.push_in(9)


print('--------')
print(str(stack_1))
print('--------')
print(stack_1.get_val())
print(stack_1.pop_out())
print(stack_1.get_val())
print(stack_1.is_empty())
print(stack_1.newinstance)
print(stack_1.newinstance.newinstance)
print(stack_1.newinstance.newinstance.newinstance)
print(stack_1.newinstance.newinstance.newinstance.newinstance)
print(stack_1.newinstance.newinstance.newinstance.newinstance.get_val())
print(stack_1.newinstance.newinstance.newinstance.newinstance.pop_out())
print(stack_1.newinstance.newinstance.newinstance.newinstance.get_val())