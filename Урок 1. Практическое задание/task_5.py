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
    def __init__(self, max_size=None):
        if max_size is None:
            max_size = 5
        self.max_size = max_size
        self.number_stack = 0 # для работы с отдельным стеком(если понадобится)
        self.elems = []
        self.stack = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems) < self.max_size:
            self.elems.append(el)
        else:
            self.number_stack += 1
            self.stack.append(self.elems)
            self.elems = []
            self.elems.append(el)

    def pop_out(self):
        """
        Удоляет последнее значение и возвращает его
        В случаее если стек пустой переходит на предыдущий стек
        """
        if len(self.elems) > 0:
            return self.elems.pop()
        else:
            self.number_stack -= 1 if self.number_stack > 0 else 0
            if len(self.stack) > 0:
                self.elems = self.stack.pop()
                return self.elems.pop()
            else:
                return None
            
    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def current_stack_size(self):
        """
        Возращает количество элементов в текущем стеке
        """
        return len(self.elems)
    
    def count_stack(self):
        """
        Возращает количество созданных стеков
        """
        if len(self.elems) == self.max_size or len(self.elems) == 0:
            current_stack = 0
        else:
            current_stack = 1
        count = len(self.stack) + current_stack
        return count


if __name__ == '__main__':
    
    Plate_stack = StackClass()
    
    for i in range(9):
        Plate_stack.push_in(f'plate_{i+1}')
    
    print(Plate_stack.current_stack_size())
    print(Plate_stack.count_stack())

    for i in range(10):
        print(Plate_stack.pop_out())
