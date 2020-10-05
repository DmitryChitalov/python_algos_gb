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


class StacksOfPlates:
    def __init__(self):
        self.stacks = []

    def put_plate(self, plate):
        if not self.stacks:
            self.stacks.append(StackOfPlates(10))
        if self.stacks[-1].push_in(plate):
            pass
        else:
            self.stacks.append(StackOfPlates(10))
            self.stacks[-1].push_in(plate)

    def take_plate(self):
        plate = self.stacks[-1].pop_out()
        if self.stacks[-1].is_empty():
            self.stacks.pop()
        return plate


class StackOfPlates:
    def __init__(self, limit):
        self.plates = []
        self.stack_limit = limit

    def is_empty(self):
        return self.plates == []

    def push_in(self, plate):
        if len(self.plates) == self.stack_limit:
            return False
        self.plates.append(plate)
        return True

    def pop_out(self):
        return self.plates.pop()

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        return len(self.plates)


plates_stacks = StacksOfPlates()

# Кладем 100 тарелок. Динамически создаются стэки
for i in range(1, 100):
    plates_stacks.put_plate(f'plate {i}')

# Берем 100 тарелок. Стэки удаляются если пустые
for i in range(1, 88):
    print(plates_stacks.take_plate())
