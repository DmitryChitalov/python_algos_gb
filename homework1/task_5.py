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

class StackDishes:
    def __init__(self):
        self.elems = []
    def is_empty(self):
        return self.elems == []
    def push_in(self, el):
        if len(self.elems) >= 10:
            print('Создайте новый объект стека тарелок')
        else:
            self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def __str__(self):
        return str(self.elems)

first_stack = StackDishes()
for i in range(10):
    first_stack.push_in(str(i+1) + ' тарелка')

print(first_stack)

first_stack.push_in(str(11) + ' тарелка')

second_stack = StackDishes()
print(second_stack)
second_stack.push_in(str(11) + ' тарелка')
print(second_stack)

first_stack.pop_out()
print(first_stack)