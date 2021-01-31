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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

class MyPlates:
    def __init__(self):
        self.my_stack_list = []
        new_obj = StackClass()
        self.my_stack_list.append(new_obj)

    def add_plate(self, el):
        if self.my_stack_list[len(self.my_stack_list) - 1].stack_size() < 4: # 1 стопка = 4 тарелки
            self.my_stack_list[len(self.my_stack_list) - 1].push_in(el)
        else:
            new_obj = StackClass()
            self.my_stack_list.append(new_obj)
            new_obj.push_in(el)

    def stack_count(self):
        return len(self.my_stack_list)

    def plates_in_last_stack(self):
        return self.my_stack_list[len(self.my_stack_list) - 1].stack_size()


ExObj = MyPlates()

while 1 == 1:
    new_elem = input('Введите значение для добавления в стек:   ')
    if len(new_elem) == 0:
        break
    ExObj.add_plate(new_elem)
    print(f'Всего стопок тарелок: {ExObj.stack_count()}')
    print(f'Тарелок в последней стопке: {ExObj.plates_in_last_stack()}')
