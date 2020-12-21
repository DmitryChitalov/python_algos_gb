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


class PlateStack:
    def __init__(self, max_size):
        self.items = [[]]
        self.max_size = max_size

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == [[]]

    def push(self, item):
        if len(self.items[len(self.items) - 1]) < self.max_size:
            self.items[len(self.items) - 1].append(item)
        else:
            self.items.append([])
            self.items[len(self.items) - 1].append(item)

    def pop(self):
        result = self.items[len(self.items) - 1].pop()
        if len(self.items[len(self.items) - 1]) == 0:
            self.items.pop()
        return result

    def size(self):
        sum_item = 0
        for stack in self.items:
            sum_item += len(stack)
        return sum_item


if __name__ == '__main__':
    plates = PlateStack(5)
    plates.push('1')
    plates.push('2')
    plates.push('3')
    plates.push('4')
    plates.push('5')
    plates.push('6')
    plates.push('7')
    plates.push('8')
    plates.push('9')
    plates.push('10')
    plates.push('11')
    print(plates)
    print(plates.pop())
    print(plates.size())
