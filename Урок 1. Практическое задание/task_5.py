"""
Задание 5.
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

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class PlateStack:

    def __init__(self, max_size):
        self.max_size = max_size
        self.stacks = []

    def push_in(self, el):
        """ Добавить тарелку в стопку"""
        if self.stacks: # проверяем наличие хотя бы одной стопки
            if len(self.stacks[0]) < self.max_size:
                self.stacks[0].insert(0, el)
            else:
                self.stacks.insert(0, list())
                self.stacks[0].insert(0, el)
        else:
            self.stacks.insert(0, list())
            self.stacks[0].insert(0, el)

    def pop_out(self):
        """ Убрать тарелку из стопки"""
        if self.stacks: # удалить можно только при наличии хотя бы одной стопки
            self.stacks[0].pop(0)
            if len(self.stacks[0]) == 0:
                self.stacks.pop(0)

    def count_stacks(self):
        """ Посчитать количество стопок тарелок"""
        return len(self.stacks)

    def get_plate(self):
        return self.stacks[0][0]

    def __str__(self):
        return str(self.stacks)

if __name__ == '__main__':

    a = PlateStack(3)
    a.push_in('Тарелка 1')
    a.push_in('Тарелка 2')
    a.push_in('Тарелка 3')
    a.push_in('Тарелка 4')
    a.push_in('Тарелка 5')

    print(a.count_stacks())
    print(a)

    a.pop_out()
    a.pop_out()

    print(a)
    print(a.count_stacks())

    print(a.get_plate())

    a.pop_out()
    a.pop_out()
    a.pop_out()
    print(a)
    a.pop_out()