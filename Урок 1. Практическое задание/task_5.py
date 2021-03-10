"""
Задание 5.
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

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackClass:
    def __init__(self, num):
        self.elems = [[]]
        self.num = num

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        if len(self.elems[len(self.elems) - 1]) < self.num:
                self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        remove_pl = self.elems[len(self.elems) - 1].pop()
        if len(self.elems) - 1 == 0:
            self.elems.pop()
        return remove_pl

    def get_val(self):
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1])- 1]

    def stack_size(self): # количество тарелок всего
        size = 0
        for st in self.elems:
            size = size + len(st)
        return size

    def num_stack(self):  # количество стопок
        return len(self.elems)


stack_pl = StackClass(5)
stack_pl.push_in('pl_1')
stack_pl.push_in('pl_2')
stack_pl.push_in('pl_3')
stack_pl.push_in('pl_4')
print(stack_pl.stack_size())
print(stack_pl.get_val())
print(stack_pl.num_stack())
stack_pl.push_in('pl_5')
stack_pl.push_in('pl_6')
stack_pl.push_in('pl_7')
print(stack_pl.stack_size())
print(stack_pl.pop_out())
print(stack_pl.stack_size())
print(stack_pl.get_val())
print(stack_pl.stack_size())
print(stack_pl.num_stack())
