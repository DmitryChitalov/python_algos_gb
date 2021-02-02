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


class Stack_of_Plates:

    def __init__(self, max_size):
        self.plates = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.plates)

    def push(self, plate):
        column_number = len(self.plates) - 1
        if column_number == -1:
            column_number = 0
            column_size = 0
        else:
            column_size = len(self.plates[column_number])

        if column_size < self.max_size:
            self.plates[column_number].append(plate)
        else:
            self.plates.append([])
            self.plates[column_number + 1].append(plate)

    def pop(self):
        #print(len(self.plates))
        column_number = len(self.plates)-1
        column_size = len(self.plates[column_number])
        #print(column_size)
        if column_number == 0 and column_size == 0:
            return print("list is empty")
        else:
            column_size = len(self.plates[column_number])
            self.plates[column_number].pop()
            if column_size - 1 == 0 and column_number != 0:
                self.plates.pop()

    def number_of_columns(self):
        print(len(self.plates))

    def full_number_of_plates(self):
        i = 0
        for column in self.plates:
            for plate in column:
                i += 1
        print(i)

    def show_all_plates(self):
        for column in self.plates:
            for plate in column:
                print(plate)


if __name__ == '__main__':
    plates = Stack_of_Plates(2)
    plates.pop()
    plates.push("plate1")
    plates.pop()
    plates.push("plate2")
    plates.push("plate3")
    plates.push("plate4")
    plates.push("plate5")
    plates.pop()

    plates.show_all_plates()

    plates.number_of_columns()
    plates.full_number_of_plates()
