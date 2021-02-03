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
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        self.elems.insert(0, el)

    def pop_out(self):
        return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def stack_size(self):
        return len(self.elems)


class ListOfStacks:
    def __init__(self, max_count_in_one_stack):
        self.stacks = list()
        self.stacks.append(StackClass())
        self.max_count_in_one_stack = max_count_in_one_stack

    def is_empty(self):
        return len(self.elems) == 0

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        last_stack = self.stacks[len(self.stacks) - 1]
        if last_stack.stack_size() < self.max_count_in_one_stack:
            last_stack.push_in(el)
        else:
            new_stack = StackClass()
            new_stack.push_in(el)
            self.stacks.append(new_stack)

    def count_of_stacks(self):
        return len(self.stacks)


stacks = ListOfStacks(3)
stacks.push_in(5)
stacks.push_in(5)
stacks.push_in(5)
stacks.push_in(5)
stacks.push_in(5)
print(f"Количество стопок: {stacks.count_of_stacks()}")
