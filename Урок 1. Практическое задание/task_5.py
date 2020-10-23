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
"""


class StackClass:
    def __init__(self, number_stacks):
        self.number_stacks = number_stacks
        self.elems = []
        self.stack = []

    def is_empty(self):
        if len(self.elems) > 0:
            return self.elems == []
        elif len(self.stack) > 0:
            self.elems = self.stack[-1]
            return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) >= self.number_stacks:
            self.stack.append(self.elems)
            self.elems = []
            self.elems.append(el)
        else:
            self.elems.append(el)

    def pop_out(self):
        if len(self.elems) > 0:
            return self.elems.pop()
        elif len(self.stack) > 0:
            self.elems = self.stack[-1]
            return self.elems.pop()

    def get_val(self):
        if len(self.elems) > 0:
            return self.elems[len(self.elems) - 1]
        elif len(self.stack) > 0:
            self.elems = self.stack[-1]
            return self.elems[len(self.elems) - 1]

    def stack_size(self):
        if len(self.stack) > 0:
            return len(self.stack) * self.number_stacks + len(self.elems)
        else:
            return len(self.elems)

    def number_full_stacks(self):
        if len(self.stack) > 0:
            return len(self.stack)
        else:
            return 0


SC_OBJ = StackClass(5)

print(f'Стек пустой: {SC_OBJ.is_empty()}')
print(f'Количество стопок: {SC_OBJ.number_full_stacks()}')

# наполняем стек
SC_OBJ.push_in('plate 1')
SC_OBJ.push_in('plate 2')
SC_OBJ.push_in('plate 3')
SC_OBJ.push_in('plate 4')

print(f'Значение первого элемента с вершины стека: {SC_OBJ.get_val()}')
print(f'Количество тарелок: {SC_OBJ.stack_size()}')
print(f'Стек пустой: {SC_OBJ.is_empty()}')  # -> стек уже непустой

SC_OBJ.push_in('plate 5')  # кладем еще один элемент в стек

SC_OBJ.push_in('plate 6')
SC_OBJ.push_in('plate 7')
print(f'Количество тарелок: {SC_OBJ.stack_size()}')
print(f'Количество стопок: {SC_OBJ.number_full_stacks()}')
print(f'Убираем элемент с вершины стека и возвращаем его значение: {SC_OBJ.pop_out()}')
print(f'Убираем элемент с вершины стека и возвращаем его значение: {SC_OBJ.pop_out()}')