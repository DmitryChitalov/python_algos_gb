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

    def __init__(self, size):  # Задаем размер стопки тарелок
        self.elements = []
        self.size = size
        self.all_stacks = []

    def is_empty(self):
        return self.elements == []

    def get_empty_stack(self):
        self.elements = []

    def push_in(self, el):  # при превышении размера стека переходим в новый метод
        if self.stack_size() < self.size:
            self.elements.append(el)
        else:
            self.add_stack(el)

    def pop_out(self):
        if self.stack_size() > 0:  # проверяем есть ли что в текущей стопке
            return self.elements.pop()
        else:  # если нет то заполняем текущую стопку последней из списка стеков
            try:
                self.elements = self.all_stacks[len(self.all_stacks) - 1]
                return self.elements.pop()
            except IndexError:  # если список стеков пустой то сообщаем об этом
                print("stack is empty")

    def get_value(self):
        if self.stack_size() > 0:
            return self.elements[len(self.elements) - 1]
        try: # задублировал код, надо бы вывести в отдельный метод но сходу не получилось а разбираться не успевал
            self.elements = self.all_stacks[len(self.all_stacks) - 1]
            return self.elements[len(self.elements) - 1]
        except IndexError:  # если список стеков пустой то сообщаем об этом
            print("stack is empty")

    def stack_size(self):
        return len(self.elements)

    def add_stack(self, el):  # добовляем полный стек в список стеков
        self.all_stacks.append(self.elements)
        self.get_empty_stack()
        self.push_in(el)


my_obj = StackClass(2)
my_obj.push_in(10)
my_obj.push_in(15)
my_obj.push_in(20)
my_obj.push_in(30)
print(my_obj.get_value())
print(my_obj.stack_size())
print(my_obj.pop_out())
print(my_obj.pop_out())
print(my_obj.get_value())
print(my_obj.pop_out())
print(my_obj.pop_out())
print(my_obj.pop_out())
