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

from random import randint

def stack_plates(num_plates):
    '''Контроль количества тарелок в стопке'''
    sc_obj = StackClass()
    i = 1
    while i <= num_plates:
        plate = randint(0, 9)
        sc_obj.push_in(plate)
        i += 1

    stack_string = ""
    while not sc_obj.is_empty():
        stack_string = stack_string + str(sc_obj.pop_out())
    return stack_string

def stack_control(num_stacks, num_plates):
    '''Формирование нужного кол-ва стеков'''
    i = 1
    while i <= num_stacks:
        print(stack_plates(num_plates))
        i += 1
    return

res = stack_control(6, 5)
