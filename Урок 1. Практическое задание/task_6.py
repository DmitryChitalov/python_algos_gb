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
    def __init__(self, max_size):
        self.elem = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.elem)

    def is_empty(self):
        return self.elem == [[]]

    def push_in(self, el):
        if len(self.elem[len(self.elem) - 1]) < self.max_size:
            self.elem[len(self.elem) - 1].append(el)
        else:
            self.elem.append([])
            self.elem[len(self.elem) - 1].append(el)

    def pop_out(self):
        result = self.elem[len(self.elem) - 1].pop()
        if len(self.elem[len(self.elem) - 1]) == 0:
            self.elem.pop()
        return result

    def get_val(self):
        return self.elem[len(self.elem) - 1][len(self.elem[len(self.elem) - 1]) - 1]

    def stack_size(self):
        elem_sum = 0
        for stack in self.elem:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        return len(self.elem)


s = StackClass(4)
s.push_in(2)
s.push_in(8)
s.push_in('Семен')
s.push_in(5.6)
s.push_in(8.3)
s.push_in('False')
s.push_in(3)
s.push_in('True')
print(s)
print(s.stack_size())
print(s.get_val())
print(s.pop_out())
print(s.stack_count())
print(s)
