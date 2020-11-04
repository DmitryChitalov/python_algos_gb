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

"""Пример создания стека через ООП"""


class StackClass:
    def __init__(self):
        self.elems = []

    def __str__(self):
        return str(self.elems)

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

    def ream(self, plate, num_in_foot):
        """Реализуем стопку тарелок"""
        j = 0
        try:
            while j < num_in_foot:
                self.push_in(plate.pop(len(plate) - 1))
                j += 1
            return self
        except IndexError:
            return self


if __name__ == '__main__':

    def stacks_of_plates_2(dishes, stack_plates):
        """
        Функция раскладывает тарелки по стопкам и осуществляет красивый вывод.

        dishes: Всего тарелок
        stack_plates: Сколько должно быть в стопе
        """
        plate = [i for i in range(1, dishes + 1)]
        stacks = []
        while True:
            if len(plate) > 0:
                sc_obj = StackClass()
                stacks.append(sc_obj.ream(plate, stack_plates))
            else:
                break

        i = 1
        for k in stacks:
            print(f'Стопка №{i} -> {k}')
            i += 1


    stacks_of_plates_2(dishes=100, stack_plates=10)


