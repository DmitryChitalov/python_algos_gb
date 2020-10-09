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
"""


class PlatesStackClass:
    """Класс стопок тарелок"""
    def __init__(self, max_size):
        self.elements = [[]]
        self.max_size = max_size

    def __str__(self):
        """Возвращает строку"""
        return str(self.elements)

    def is_empty(self):
        """Возвращает пустой список стопок тарелок"""
        return self.elements == [[]]

    def push_in(self, el):
        """Добавляет старелку в стопку, при достижении лимита в текущей стопке создает новую"""
        if len(self.elements[len(self.elements) - 1]) < self.max_size:
            self.elements[len(self.elements) - 1].append(el)
        else:
            self.elements.append([])
            self.elements[len(self.elements) - 1].append(el)

    def pop_out(self):
        """Извлекает тарелку из стопки, если в стопке не остается тарелок, удаляет стопку"""
        result = self.elements[len(self.elements) - 1].pop()
        if len(self.elements[len(self.elements) - 1]) == 0:
            self.elements.pop()
        return result

    def show_last_plate(self):
        """Возвращает значение последней тарелки"""
        return self.elements[len(self.elements) - 1][len(self.elements[len(self.elements) - 1]) - 1]

    def plate_count(self):
        """возвращает количество тарелок"""
        elem_sum = 0
        for stack in self.elements:
            elem_sum += len(stack)
        return elem_sum

    def stack_count(self):
        """Возвращает количество стопок"""
        return len(self.elements)


if __name__ == '__main__':
    plates = PlatesStackClass(4)
    for i in range(1, 11):
        plates.push_in(f'Plate{i}')
    print(plates)
    print(plates.pop_out())
    print(plates.show_last_plate())
    print(plates.plate_count())
    print(plates.stack_count())
    print(plates)
