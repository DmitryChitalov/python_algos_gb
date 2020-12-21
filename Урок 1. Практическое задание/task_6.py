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


class StackOfPlates:
    def __init__(self, size_of_steck):
        self.elems = [[]]
        self.size_of_stack = size_of_steck

    def __str__(self):
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def into(self, plate):  # добавляем тарлку в конец стопки, если стопка заполнена создаем новую и кладём в новую
        if len(self.elems[len(self.elems)-1]) < self.size_of_stack:
            self.elems[len(self.elems)-1].append(plate)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(plate)

    def out_one_plate(self):  # берем тарелку, удаляем стопку, если пустая
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def get_val(self):  # Верхняя тарелка в стопке
        return self.elems[len(self.elems) - 1][len(self.elems[len(self.elems) - 1]) - 1]

    def amount_of_plates(self):  # общее количество тарелок
        amount = 0
        for stack in self.elems:
            amount += len(stack)
        return amount

    def amount_of_stack(self):  # Количество стопок
        return len(self.elems)


pl = StackOfPlates(3)
print(f'В каждой стопке у нас по {pl.size_of_stack} тарелки')
pl.into('Тарелка1')
pl.into('Тарелка2')
pl.into('Тарелка3')
pl.into('Тарелка4')
pl.into('Тарелка5')

n = 0
for i in pl.elems:
    n += 1
    print(f'Стопка {n}: {i}')

print(f'Тарелок всего {pl.amount_of_plates()} шт.')
print(f'Тарелки лежат в {pl.amount_of_stack()} стопках')
print(f'{pl.out_one_plate()} улетела')
print(f'В последней стопке сверху лежит {pl.get_val()}')
