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
    def __init__(self, num):
        self.elems = [[]]
        self.num = num

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, val):
        if len(self.elems[len(self.elems) - 1]) < self.num:
            self.elems[len(self.elems) - 1].append(val)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(val)

    def pop_out(self):
        res = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return res


if __name__ == '__main__':
    plates = Plates(3)
    plates.push_in('1')
    plates.push_in('2')
    plates.push_in('3')
    plates.push_in('4')
    plates.push_in('5')
    print(plates)
    print(plates.pop_out())
    print(plates.pop_out())
    print(plates)
