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


class StackClass:
    def __init__(self, max_size_stack=10):
        self.elems = [[]]
        self.max_size_stack = max_size_stack
        self.index = 0

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка
            добавляем новый элемент.
            При достежении максимального размера создаеться новый список
        """
        if self.stack_size() == self.max_size_stack:
            self.new_stack()
        self.elems[self.index].append(el)

    def pop_out(self):
        """
        удаляем последний элемент
        и возвращяем его
        """
        if self.stack_size() == 0:
            self.drop_new_stack()
        return self.elems[self.index].pop()

    def get_val(self):
        return self.elems[self.index][len(self.elems[self.index]) - 1]

    def stack_size(self):
        return len(self.elems[self.index])

    def new_stack(self):
        """
        создаем новый стек
        """
        self.index += 1
        return self.elems.append([])

    def drop_new_stack(self):
        """
        удаляем пустой стек
        """
        self.index -= 1
        return self.elems.pop()

    def print_stack(self):
        """
        для визуального контроля стека, стандартный вывод перезагружать не стал
        """
        print(self.elems)


if __name__ == '__main__':

    SC_OBJ = StackClass(20)

    # наполняем стек
    for num in range(100):
        SC_OBJ.push_in(num)

    for num in range(100, 200):
        SC_OBJ.push_in(num)

    # контроль наполненого стека
    SC_OBJ.print_stack()

    # опустошаем стек и выводим элементы
    for _ in range(100):
        print(SC_OBJ.pop_out())

    SC_OBJ.print_stack()

    for _ in range(100):
        print(SC_OBJ.pop_out())