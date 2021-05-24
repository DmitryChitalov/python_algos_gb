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
    def __init__(self):
        self.elements_list = []

    def is_empty(self):
        return self.elements_list == []

    def push_in(self, element):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elements_list.append(element)

    def pop_out(self):
        return self.elements_list.pop()

    def get_val(self):
        return self.elements_list[len(self.elements_list) - 1]

    def stack_size(self):
        return len(self.elements_list)


class Plates:
    def __init__(self):
        self.my_stack_list = []
        new_obj = StackClass()
        self.my_stack_list.append(new_obj)

    def add_plate(self, element):
        if self.my_stack_list[len(self.my_stack_list) - 1].stack_size() < 4:   # 1 стопка = 4 тарелки
            self.my_stack_list[len(self.my_stack_list) - 1].push_in(element)
        else:
            new_obj = StackClass()
            self.my_stack_list.append(new_obj)
            new_obj.push_in(element)

    def stack_count(self):
        return len(self.my_stack_list)

    def plates_in_last_stack(self):
        return self.my_stack_list[len(self.my_stack_list) - 1].stack_size()


ExObject = Plates()

while True:
    new_element = input('Добавить тарелку?(y/n):   ')
    if new_element == 'n':
        print('Как хотите :)')
        break
    elif new_element == 'y':
        ExObject.add_plate('Plate')
        print(f'Всего стопок: {ExObject.stack_count()}')
        print(f'Тарелок в последней стопке: {ExObject.plates_in_last_stack()}')
    else:
        print('Ответ может быть y или n')
