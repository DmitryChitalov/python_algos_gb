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

from stack import StackClass


class StackOfPlates:
    def __init__(self, s_len=5):
        """
        Конструктор

        list_stacks: список стопок тарелок (список стеков)
        cur_ind: порядковый номер текущей стопки
        max_stack_len: максимальная длина стопки
        """
        self.list_stacks = []
        self.cur_ind = -1
        self.max_stack_len = s_len

    def push_plates(self):
        """
        Положить тарелку в текущую стопку. При переполнении выделить новую стопку
        """
        if self.cur_ind == -1 or self.list_stacks[self.cur_ind].stack_size() >= self.max_stack_len:
            self.cur_ind += 1
            self.list_stacks.append(StackClass())
        self.list_stacks[self.cur_ind].push_in('Plates')

    def pop_plates(self):
        """
        Извлечь тарелку из текущей стопки. Если не хватает, то перейти к предыдущей стопке
        """
        if self.cur_ind == -1:
            raise Exception('Тарелок не осталось')
        elif not self.list_stacks[self.cur_ind].stack_size():
            self.list_stacks.pop()
            self.cur_ind -= 1
            if self.cur_ind == -1:
                raise Exception('Тарелок не осталось')

        self.list_stacks[self.cur_ind].pop_out()

    def visual_stack(self):
        """
        Визуализация текущего состояния стопок
        """
        for i, elem in enumerate(self.list_stacks):
            print(f'Стопка {i}')
            for i in range(elem.stack_size()):
                print('---')


if __name__ == '__main__':
    stack_plates = StackOfPlates(s_len=2)
    stack_plates.push_plates()
    stack_plates.push_plates()
    stack_plates.push_plates()
    stack_plates.push_plates()
    stack_plates.pop_plates()
    stack_plates.visual_stack()



