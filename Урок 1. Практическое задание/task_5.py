"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого
значения нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком
порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые
методы для реализации это структуры, добавьте новые методы
(не рассмотренные в примере с урока) для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
import random


class PlateStorage:
    def __init__(self):
        self._stacks_of_plates = []

    def is_empty(self):
        return self._stacks_of_plates == []

    def add_plate(self):
        """Добавляем тарелку в стопку, пока тарелок не станет 10,
        иначе начинаем новую стопку"""
        if self.is_empty() or len(self._stacks_of_plates[-1]) == 10:
            self._stacks_of_plates.append(['plate'])
        else:
            self._stacks_of_plates[-1].append('plate')

    def remove_plate(self):
        if not self.is_empty():
            self._stacks_of_plates[-1].pop()
            if len(self._stacks_of_plates[-1]) == 0:
                self._stacks_of_plates.pop()

    def last_stack_amount(self):
        return len(self._stacks_of_plates[-1])

    def plates_amount(self):
        return (len(self._stacks_of_plates) - 1) * 10 + \
               len(self._stacks_of_plates[-1])

    def stacks_amount(self):
        return len(self._stacks_of_plates)


# создаём хранилище тарелок (объект класса Plate_storage())
cupboard = PlateStorage()

# определяем, есть ли тарелки в хранилище
print(cupboard.is_empty())  # -> тарелок нет

# наполняем хранилище
plates_amount = random.randint(1, 100)
for i in range(plates_amount):
    cupboard.add_plate()

# Определяем общее количество тарелок в хранилище
print(cupboard.plates_amount())

# Определяем количество стопок в хранилище
print(cupboard.stacks_amount())

# определяем количество тарелок в последней стопке
print(cupboard.last_stack_amount())

# определяем, есть ли тарелки в хранилище
print(cupboard.is_empty())  # -> тарелки есть

# Добавляем тарелку
cupboard.add_plate()
print(cupboard.last_stack_amount())

# Убираем тарелку
cupboard.remove_plate()
print(cupboard.last_stack_amount())

# Убираем тарелку
cupboard.remove_plate()
print(cupboard.last_stack_amount())

# Определяем общее количество тарелок в хранилище
print(cupboard.plates_amount())
