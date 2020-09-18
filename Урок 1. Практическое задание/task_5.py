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

class PlatesStackClass:
    amount_of_stacks = 0
    max_stack_size = 3

    def __init__(self, stack_name):
        self.plates = [[]]
        self.stack_name = stack_name

    def __repr__(self):
        return self.stack_name

    def is_empty(self):
        return self.plates == []

    def add_plate(self, el):
        if self.plates_stack_size() < PlatesStackClass.max_stack_size:
            self.plates[PlatesStackClass.amount_of_stacks].append(el)
            print(f'добавлено: {el}')
            print(f'текущий состав стопок {plates_stack_01}:{plates_stack_01.plates}')
        else:
            PlatesStackClass.amount_of_stacks +=1
            self.plates.append([])
            print(PlatesStackClass.amount_of_stacks)
            self.plates[PlatesStackClass.amount_of_stacks].append(el)
            print(f'добавлено: {el}')
            print(f'текущий состав стопки {plates_stack_01}:{plates_stack_01.plates}')

    def remove_plate(self):
        return self.plates.pop()

    def last_plate(self):
        return self.plates[len(self.elems) - 1]

    def plates_stack_size(self):
        return len(self.plates[PlatesStackClass.amount_of_stacks])


plates_stack_01 = PlatesStackClass("Plates_Stack_01")

print(f'Создана группа стопок тарелок {plates_stack_01}')
print(f'максимальный размер одной стопки в {plates_stack_01}: {plates_stack_01.max_stack_size} шт.')

plates_stack_01.add_plate("тарелка 1")
plates_stack_01.add_plate("тарелка 2")
plates_stack_01.add_plate("тарелка 3")
plates_stack_01.add_plate("тарелка 4") #будет добавляться во второй элемент (список) списка, так как max stack size = 3
plates_stack_01.add_plate("тарелка 5")