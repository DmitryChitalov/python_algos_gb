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
    """
    Класс представляет последовательность стопок тарелок на столе.
    Промежуточный доступ к каждой стопке не реализован, но, если
    требуется, я сделаю.
    """
    max_plates = 10
    all_stacks = []

    def __init__(self):
        self.elems = []
        StackClass.all_stacks.append(self)

    def is_empty(self):
        return self.elems == []

    def put(self):
        """
        Функция для укладывания тарелок в стопки.
        При достижении предельной высоты, начинается новая стопка.
        """
        if len(StackClass.all_stacks[-1].elems) == StackClass.max_plates:
            print('Новая стопка тарелок.')
            StackClass()
            StackClass.all_stacks[-1].put()
        else:
            print('Кладем тарелку в стопку.')
            StackClass.all_stacks[-1].elems.append('plate')

    def take(self):
        """
        Функция для убирания тарелок из стопок.
        Тарелки убираются в обратном порядке.
        """
        if self.get_size(len(StackClass.all_stacks)) == 0 and \
                len(StackClass.all_stacks) > 1:
            print('Стопка тарелок опустела.')
            StackClass.all_stacks[-1] = None
            StackClass.all_stacks.pop()
            StackClass.all_stacks[-1].take()
        elif self.get_size(len(StackClass.all_stacks)) == 0 and \
                len(StackClass.all_stacks) == 1:
            print('На столе нет тарелок.')
        else:
            print('Забираем тарелку из стопки.')
            StackClass.all_stacks[-1].elems.pop()

    def get_size(self, num):
        return len(StackClass.all_stacks[num-1].elems)

    def get_qnt_stacks(self):
        return len(StackClass.all_stacks)

    def get_content(self, num):
        return StackClass.all_stacks[num-1].elems

if __name__ == '__main__':
    table = StackClass()
    for i in range(12):
        table.put()
    print('Стол пуст.') if table.is_empty() else print(
        'На столе есть тарелки.')
    print(f'На столе {table.get_qnt_stacks()} стопки тарелок.')
    print(f'В первой стопке {table.get_size(1)} тарелок.')
    print(f'Во второй стопке {table.get_size(2)} тарелки.')
    print(f'Содержимое второй стопки: {table.get_content(2)}.')
    print(f'Список стопок тарелок: {StackClass.all_stacks}.')
    for i in range(13):
        table.take()