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


class PlateStackClass:
    def __init__(self, max_size):
        self.elems = [[]]
        self.max_size = max_size  # размер стопки

    def __str__(self):
        return str(self.elems)

    def change(self):  # Перекладываем верхние тарелки местами с одной стопки на другую
        print(f"Эти тарелки мы поменяем с соседними стопками "
              f"{[el[-1] for el in self.elems]}")  # Смотрим на верхние тарелки
        i = 0
        while i < len(self.elems):
            self.elems[i][-1], self.elems[i+1][-1] = self.elems[i+1][-1], self.elems[i][-1]
            i += 2
        return self.elems

    def is_empty(self):
        return self.elems == [[]]

    def push(self, el):
        #  Предполагаем, что верхний элемент стопки находится в конце списка
        #  если размер стопки равен пороговому значению то создается новая стопка и туда кладется значение
        if len(self.elems[len(self.elems) - 1]) < self.max_size:
            self.elems[len(self.elems) - 1].append(el)
        else:
            self.elems.append([])
            self.elems[len(self.elems) - 1].append(el)

    def pop(self):
        #  Берем тарелку из крайней стопки, если она пустая удаляем ее
        result = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[len(self.elems) - 1]) == 0:
            self.elems.pop()
        return result

    def stack_size(self):
        #  Общее колличество тарелок
        elem_sum = 0
        for stack in self.elems:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        #  Количество стопок
        return len(self.elems)


plates = PlateStackClass(2)
i = 1
while i <= 12:
    plates.push('Тарелка_' + str(i))
    i += 1


print(f"Общее количество тарелок {plates}")
print(f"Мы поменяли верхние тарелки с соседними {plates.change()}")
print(f"Убранная тарелка {plates.pop()}")
print(f"Общее количество оставшихся тарелок {plates.stack_size()}")
print(f"Общее количество стопок {plates.stack_count()}")
print(f"Конечный результат {plates}")

