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
    def __init__(self, size):
        self.elems = [[]]   # Создаем список списков для возможности хранить несколько стеков
        self.size = size    # Размер стопки

    def __str__(self):
        return str(self.elems)

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if len(self.elems[len(self.elems) - 1]) < self.size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop_out(self):
        self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:   # если стек становится пустым, то удаляем его
            self.elems.pop()

    def elems_size(self):
        return len(self.elems)

    def stack_size(self):
        sum = 0  # Общее кол-во тарелок
        for el in self.elems:
            sum += len(el)
        return sum

plates = StackClass(3)
plates.push_in('_')
plates.push_in('_')
plates.push_in('_')
plates.push_in('_')
plates.push_in('_')
plates.push_in('_')
plates.push_in('_')
print(plates)
plates.pop_out()
print(plates)
print(f'Всего тарелок: {plates.stack_size()} \nВсего стопок: {plates.elems_size()}')
plates.pop_out()
print(f'Всего тарелок: {plates.stack_size()} \nВсего стопок: {plates.elems_size()}')
plates.pop_out()
plates.pop_out()
print(f'Всего тарелок: {plates.stack_size()} \nВсего стопок: {plates.elems_size()}')
plates.push_in('_')
print(f'Всего тарелок: {plates.stack_size()} \nВсего стопок: {plates.elems_size()}')