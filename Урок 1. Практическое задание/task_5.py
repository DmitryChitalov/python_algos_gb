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


class MyStackClass:
    def __init__(self, group_size):
        if type(group_size) != int:
            self.group_size = 10
        else:
            self.group_size = group_size
        self.groups = []
        self.current_group = 0
        self.elems = []

    @property
    def is_empty(self):
        return not bool(self.size)

    @property
    def size(self):
        return len(self.elems) + self.current_group * self.group_size

    def push(self, el):
        if el is not None:
            if self.is_empty:
                self.groups.append([])
                self.elems = self.groups[self.current_group]
            if len(self.elems) == self.group_size:
                self.current_group += 1
                self.groups.append([])
                self.elems = self.groups[self.current_group]
            self.elems.append(el)

    def pop(self):
        if self.is_empty:
            return 'Тарелок больше нет, стек пуст'
        r = self.elems.pop()
        if not len(self.elems):
            self.groups.pop()
            if self.is_empty:
                self.elems = []
            else:
                self.current_group -= 1
                self.elems = self.groups[self.current_group]
        return r

    def get_val(self):
        if not self.is_empty:
            return self.elems[-1]

    def __str__(self):
        if self.is_empty:
            return 'Тарелок больше нет, стек пуст'
        else:
            return f'Стопок: {len(my_stack.groups)}, Тарелок в последней стопке: {len(my_stack.elems)}'


my_stack = MyStackClass(10)
while True:
    ans = input('(+) - добавить тарелку, (-) - убрать тарелку, (q) - выход: ').lower()
    if ans == 'q':
        break
    if ans == '+':
        my_stack.push('тарелка')
    elif ans == '-':
        my_stack.pop()
    print(my_stack)
