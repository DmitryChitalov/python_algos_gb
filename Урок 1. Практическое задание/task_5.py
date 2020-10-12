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

import random


class PlatesStack:
    __num = 0

    def __init__(self, max_stack_size):
        """

        :param max_stack_size: Максимальное число тарелок в стопке
        """
        self.__stacks = []
        self.__max_stack_size = max_stack_size

    def add_plate(self, name=''):
        """Добавление тарелки в стопку

        :param name: Имя тарелки
        :return: Возвращает имя добавленной тарелки
        """
        if name == '':
            name = self.random_name()
        self.__num += 1
        name = f"{self.__num} - {name}"
        if self.stacks_count() == 0:
            self.__stacks.append([name])
            return name
        for stack in self.__stacks:
            if len(stack) < self.__max_stack_size:
                stack.append(name)
                return name
        self.__stacks.append([name])
        return name
    
    def get_plate(self):
        """Взять тарелку из последней стопки

        :return: Возвращает имя взятой тарелки
        """
        if len(self.__stacks) > 0:
            plate = self.__stacks[len(self.__stacks) - 1].pop()
            if len(self.__stacks[len(self.__stacks) - 1]) == 0:
                self.__stacks.pop()
            return plate
        else:
            return None

    def get_plate_from_stack(self, idx_stack):
        """Взять тарелку из определенной стопки

        :param idx_stack: Индекс стопки, из которой берется тарелка
        :return: Возвращает имя взятой тарелки
        """
        if len(self.__stacks[idx_stack]) > 0:
            return self.__stacks[idx_stack].pop()
        else:
            return None

    def plates_show(self):
        """Печать имен всех тарелок во всех стопках

        """
        print('\nВывод тарелок:')
        print('=' * 30, end="\n")
        for i, stack in enumerate(self.__stacks):
            print(f"Стопка {i + 1}:\n{'-' * 30}")
            for j, plate in enumerate(stack):
                print(f"{j + 1}: {plate}")
            print('-' * 30, end='\n\n')

    def stacks_count(self):
        """Количество стопок

        :return: Возвращает количество стопок с тарелками
        """
        return len(self.__stacks)

    def plates_count(self):
        """Количество тареолк в стопках

        :return: Возвращает количество тарелок в каждой стопке
        """
        return [len(stack) for stack in self.__stacks]
    
    def random_name(self):
        """Генератор случайного имени для тарелок

        :return: Возвращает случайное имя для тарелки
        """
        shape = ['Круглая', 'Овальная', 'Квадратная', 'Многоугольная', 'Необычная']
        color = ['Белая', 'Желтая', 'Красная', 'Черная', 'Зеленая', 'Синия', 'Радужная']
        size = ['Маленькая', 'Средеяя', 'Большая', 'Огромная', 'Глубокая', 'Суповая', 'Прямая']
        return f"{random.choice(size)} {random.choice(color)} {random.choice(shape)}"


######################################
plates = PlatesStack(5)

# Положим в стопки 12 тарелок
for i in range(12):
    plates.add_plate()
plates.plates_show()
print(f"Количество стопок: {plates.stacks_count()}")
print(f"Количество торелок по стопкам: {plates.plates_count()}")

# Заберем 3 тарелки
for i in range(3):
    print(f"Забрали тарелку: {plates.get_plate()}")
plates.plates_show()
print(f"Количество стопок: {plates.stacks_count()}")
print(f"Количество торелок по стопкам: {plates.plates_count()}")

# Заберем 2 тарелки из первой стопки
for i in range(2):
    print(f"Забрали тарелку: {plates.get_plate_from_stack(0)}")
plates.plates_show()
print(f"Количество стопок: {plates.stacks_count()}")
print(f"Количество торелок по стопкам: {plates.plates_count()}")

# Добавим 6 тарелок
for i in range(6):
    plates.add_plate()
plates.plates_show()
print(f"Количество стопок: {plates.stacks_count()}")
print(f"Количество торелок по стопкам: {plates.plates_count()}")

# Заберем 20 тарелок
for i in range(20):
    print(f"Забрали тарелку: {plates.get_plate()}")
plates.plates_show()
print(f"Количество стопок: {plates.stacks_count()}")
print(f"Количество торелок по стопкам: {plates.plates_count()}")
