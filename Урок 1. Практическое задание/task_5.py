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


class StackPlates:
    """
    Реализует структуру, предусматривающую увеличение количества стеков в зависимости от количества элементов.
    Размер стека (стопки тарелок) принят равным трем. При заполнении текущего стека в структуру автоматически
    добавляется новый стек. Если текущий стек (за исключением первого), опустел, то он удаляется из структуры).
    """

    def __init__(self):
        self.elems = [[]]
        self.current = 0  # константа определяет в каком стеке находимся в данный момент
        self.taken_out = None  # извлекаемая из стопки тарелка

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце текущего списка"""
        if len(self.elems[self.current]) == 3:
            self.elems.append([])
            self.current += 1
            self.elems[self.current].append(el)
        else:
            self.elems[self.current].append(el)

    def pop_out(self):
        """Удаляет тарелку из текущей стопки. Если это не 1-я стопка и кол-во тарелок в ней = 0, удаляет стек под нее"""
        self.taken_out = self.elems[self.current].pop()
        if self.elems[self.current] == [] and self.current != 0:
            self.elems.pop()
        return self.taken_out

    def get_val(self):
        return self.elems[self.current][len(self.elems) - 1]

    def stack_size(self):
        """Возвращает количество стопок нарелок (стеков в структуре) на текущий момент"""
        return len(self.elems)

    def stack_el_size(self):
        """Возвращает количество тарелок в текущей стопке (текущем стеке)"""
        return len(self.elems[self.current])


if __name__ == '__main__':
    plates_one = StackPlates()
    # Добавляем тарелки в стопку (в один стек входит три элемента)
    plates_one.push_in('first plate')
    plates_one.push_in('second plate')
    plates_one.push_in('third plate')

    # Удаляем тарелку из стопки
    plates_one.pop_out()  # удаляется треться тарелка

    print(plates_one.elems)
    print('_' * 100)
    # Добавляем тарелки. Начиная с пятой (так как третья была удалена), тарелки добавляются уже во вторую стопку
    plates_one.push_in('fourth plate')
    plates_one.push_in('fifth plate')
    plates_one.push_in('sixth plate')

    print(plates_one.elems)
    print(plates_one.get_val())  # шестая тарелка лежит сверху второй стопки

    # Количество стопок на данный момент
    print(plates_one.stack_size())
    print('_' * 100)

    plates_one.push_in('seventh plate')
    plates_one.push_in('eighth plate')
    plates_one.push_in('ninth plate')
    plates_one.push_in('tenth plate')

    # Количество тарелок в текущей стопке
    print(plates_one.stack_el_size())

    # Количество стопок на данный момент
    print(plates_one.stack_size())

    print(plates_one.elems)
    print('_' * 100)
    # Проверяем, удаляется ли текущая стопка (за исключением первой), при удалении из нее всех тарелок
    plates_one.pop_out()
    plates_one.pop_out()
    plates_one.pop_out()
    print(plates_one.elems)

    # Последняя тарелка, вынутая на данный момент из текущей стопкм
    print(plates_one.taken_out)
