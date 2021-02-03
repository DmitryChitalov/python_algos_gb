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


class PlatesStack:
    _size: int

    def __init__(self, size):
        self._size = size
        self.plates = [[]]

    def get_plates_size(self):
        return self._size

    def add_palate(self):
        if len(self.plates[len(self.plates) - 1]) < self._size:
            self.plates[len(self.plates) - 1].append("Plate")
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append("Plate")

    def pop_plate(self):
        result = self.plates[len(self.plates) - 1]
        self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return result

    def stacks_count(self):
        return len(self.plates)

    def plates_count(self):
        return len(self.plates) * self._size - (self._size - len(self.plates[len(self.plates) - 1]))

    def get_current_plate(self):
        return self.plates[len(self.plates) - 1][len(self.plates[len(self.plates) - 1]) - 1]


if __name__ == "__main__":
    plates_stack = PlatesStack(3)
    print(f"Количество тварелок в стопке : {plates_stack.get_plates_size()}")
    plates_stack.add_palate()
    plates_stack.add_palate()
    plates_stack.add_palate()
    plates_stack.add_palate()
    plates_stack.add_palate()
    plates_stack.add_palate()
    plates_stack.add_palate()
    print(plates_stack.plates)
    print(f"Количество тарелок: {plates_stack.plates_count()}")
    print(f"Количество стопок: {plates_stack.stacks_count()}")
    plates_stack.pop_plate()
    plates_stack.pop_plate()
    plates_stack.pop_plate()
    plates_stack.pop_plate()
    plates_stack.pop_plate()
    print(plates_stack.plates)
    print(f"Количество тарелок: {plates_stack.plates_count()}")
    print(f"Количество стопок: {plates_stack.stacks_count()}")
    print(plates_stack.get_current_plate())
