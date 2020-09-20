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


class Plates:
    def __init__(self, max_size=2):
        self.plates = [[]]
        self.max = max_size

    def __str__(self):
        return str(self.plates)

    def add_item(self, item):
        if len(self.plates[len(self.plates) - 1]) < self.max:
            self.plates[len(self.plates) - 1].append(item)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(item)

    def remove_item(self):
        deleted_item = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return deleted_item

    def is_empty(self):
        if self.plates == [[]]:
            print("Стопок нет")
        else:
            print(f'Всего {len(self.plates)} стопки(а)')

    def print_last_value(self):
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
            print(f'Последнее значение - '
                  f'{self.plates[len(self.plates) - 1][len(self.plates[len(self.plates) - 1]) - 1]}')
        else:
            print(f'Последнее значение - '
                  f'{self.plates[len(self.plates) - 1][len(self.plates[len(self.plates) - 1]) - 1]}')

    def get_last_value(self):
        if self.plates != [[]]:
            if len(self.plates[len(self.plates) - 1]) == 0:
                self.plates.pop()
                last_plate = self.plates[len(self.plates) - 1].pop()
                return last_plate
            else:
                last_plate = self.plates[len(self.plates) - 1].pop()
                return last_plate
        else:
            print('Тарелок больше нет')

    def print_total_size(self):
        if self.plates == [[]]:
            print(f'В 0 стопках находится 0 тарелок')
        else:
            count_plates = 0
            count_stacks = len(self.plates)
            for el in self.plates:
                count_plates += len(el)
            print(f'В {count_stacks} стопках находится {count_plates} тарелок')

    def remove_stack(self):
        removed_stack = self.plates.pop()
        return removed_stack

    def remove_all(self):
        self.plates = [[]]


if __name__ == '__main__':
    plates = Plates(3)
    plates.get_last_value()
    plates.is_empty()
    plates.add_item(1)
    plates.add_item(2)
    plates.add_item(3)
    plates.add_item(5)
    plates.add_item(6)
    plates.add_item(7)
    plates.add_item(8)
    print(plates)
    print(plates.get_last_value())
    plates.print_last_value()
    plates.is_empty()
    plates.remove_item()
    print(plates.remove_stack())
    plates.print_total_size()
    plates.remove_all()
    plates.print_total_size()
