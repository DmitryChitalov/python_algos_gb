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


class StackIsFull(Exception):
    pass


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


class StackOfPlates(StackClass):
    def __init__(self, max_heght: int):
        super().__init__()
        self._max_height = max_heght  # максимальная высота стопки

    def is_not_full(self):  # проверка на заполненность
        return self.stack_size() < self._max_height

    def push_in(self, el):
        if self.is_not_full():  # проверяем на заполненность
            self.elems.append(el)
        else:
            raise StackIsFull('Stack is full! Create new stack!')


class Plate:
    pass


if __name__ == '__main__':
    #  создаем тарелки
    plate_1 = Plate()
    plate_2 = Plate()
    plate_3 = Plate()
    plate_4 = Plate()
    plate_5 = Plate()
    plate_6 = Plate()
    plate_7 = Plate()

    # создаем две стопки максимальной высотой в 3 и 4 тарелки
    stack_1 = StackOfPlates(3)
    stack_2 = StackOfPlates(4)

    # добавляем в первую стопку 3 тарелки
    stack_1.push_in(plate_1)
    stack_1.push_in(plate_2)
    stack_1.push_in(plate_3)
    print(stack_1.stack_size())

    # пробуем добавить четвертую
    try:
        stack_1.push_in(plate_4)
    except StackIsFull as e:
        print(e)

    print(stack_1.stack_size())  # тарелка не добавилась!

    # добавляем остальные тарелки во вторую стопку
    stack_2.push_in(plate_4)
    stack_2.push_in(plate_5)
    stack_2.push_in(plate_6)
    stack_2.push_in(plate_7)
    print(stack_1.stack_size(), stack_2.stack_size())
