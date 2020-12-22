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
    def __init__(self):
        self.elems = []
        self.plate_counter = 0 # Добавил счётчик для количества всех тарелок (В конструкторе инициилизируем нулём)
        self.list_of_stacks = []

    def is_empty(self):
        return self.list_of_stacks == [] and self.plate_counter == 0

    def push_in(self, el): # Модифицировал данный метод
        if (not isinstance(el, int)):
            raise ValueError("Неверный индекс стопки")
        if (len(self.elems) == 10):
            self.list_of_stacks.append(self.elems)
            self.plate_counter += 1
            self.elems= []
            self.elems.append(el)
        else:
            self.plate_counter += 1
            self.elems.append(el)

    def pop_out(self): # Также модифицировал данный метод
        if (len(self.elems)):
            self.plate_counter -= 1  # Декрементируем общий счётчик тарелок, если в последней стопке
            # имеются тарелки(хотя бы 1 тарелка)
            return self.elems.pop()
        else: # иначе: если self.elems = 0, то удаляем из self.list_of_stacks последний, пустой список
            # и удаляем из уже последнего заполненного списку последний элемент
            self.list_of_stacks.pop(len(self.list_of_stacks)-1)
            self.plate_counter -= 1
            self.elems = self.list_of_stacks[(len(self.list_of_stacks) - 1)]
            return self.elems.pop()

    def get_all_values(self):
        self.list_of_stacks.append(self.elems)
        return self.list_of_stacks

    def get_all_plate_number(self):
        return self.plate_counter

if __name__ == '__main__':

    plates = PlateStack()

    print(plates.is_empty())  # -> стек пустой

    # наполняем стек
    for i in range (1, 23): # Цикл от 1 до 22(включительно)
        plates.push_in(i)

    print(plates.list_of_stacks) # получаем только заполненные стэки

    print(plates.get_all_values())  # получаем все тарелки (в том числе и из последней - незаполненной стопки)

    print(plates.get_all_plate_number())  # получаем количество всех тарелок в стеке

    print("Последнее значение стека было: ", plates.pop_out())  # получаем значение последнего элемента

    print(plates.get_all_plate_number())  # получаем новое количество всех тарелок в стеке

    print("Последнее значение стека было: ", plates.pop_out())  # (21) получаем значение последнего элемента

    print("Последнее значение стека было: ", plates.pop_out())  # (20) получаем значение последнего элемента

    print("Последнее значение стека было: ", plates.pop_out())  # (19) получаем значение последнего элемента

    print("Последнее значение стека было: ", plates.pop_out())  # (18) получаем значение последнего элемента

    print(plates.is_empty())  # -> стек пустой(нет)


