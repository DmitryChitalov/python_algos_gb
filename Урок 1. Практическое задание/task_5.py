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
    def __init__(self):
        self.elems = [[]]  # двумерный массив

    def is_empty(self):
        return self.elems == []

    def new_stack(self):
        self.elems.append([])  # добавление новой строки при заполнении предыдущей

    def push_in(self, el):
        if len(self.elems[-1]) == 5:  # проверка заполнения
            self.new_stack()
        self.elems[-1].append(el)

    def pop_out(self):
        out = self.elems[-1].pop()  # проверка вывода
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return out

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        self.total_len = 0  # подсчёт общего размера стека
        for i in self.elems:
            self.total_len += len(i)
        return self.total_len



SC_OBJ = StackClass()

# наполняем стек
SC_OBJ.push_in(10)
SC_OBJ.push_in('code')
SC_OBJ.push_in(False)
SC_OBJ.push_in(5.5)
SC_OBJ.push_in(101)
SC_OBJ.push_in('code2323')
SC_OBJ.push_in('asdasdasdas2')
SC_OBJ.push_in(532.5333)


print(SC_OBJ.pop_out())
print(SC_OBJ.stack_size())
