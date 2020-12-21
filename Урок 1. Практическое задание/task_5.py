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


class PlateStack:
    def __init__(self):
        self.elems = [[]]
        #self.elems.insert(0, [])

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems[0]) == 6:
            self.elems.insert(0, [])
        self.elems[0].insert(0, el)

    def pop_stack(self):
        self.elems.pop(0)

    def get_value(self):
        return self.elems[0]

    def stack_quantity(self):
        return len(self.elems)

    def print(self):
        print(self.elems)

# Проверка:

ps_obj = PlateStack()

for i in range(60):
    ps_obj.push_in('plate')

ps_obj.print()
ps_obj.pop_out()
print(ps_obj.stack_size())
