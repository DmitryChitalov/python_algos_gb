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


class PileOfPlates:
    def __init__(self, plate=False):
        self.plates = []
        self.max_size = 10
        if plate:
            self.plates.append(plate)
        self.current_size = len(self.plates)

    def push_in(self, plate):
        x = self.is_max()
        if not x:
            plates_piles[len(plates_piles) - 1].plates.append(plate)
            plates_piles[len(plates_piles) - 1].current_size += 1
        elif x and len(plates_piles[len(plates_piles) - 1].plates) != 10:
            plates_piles[len(plates_piles) - 1].plates.append(plate)
            self.current_size += 1
        else:
            self.creating_pile(plate)

    def pop_out(self):
        if not plates_piles[len(plates_piles) - 1].is_empty():
            plates_piles[len(plates_piles) - 1].current_size -= 1
            if plates_piles[len(plates_piles) - 1].current_size == 0:
                number = plates_piles[len(plates_piles) - 1].plates.pop()
                del(plates_piles[len(plates_piles) - 1])
                return number
            else:
                return plates_piles[len(plates_piles) - 1].plates.pop()
        else:
            print("Стопка пуста")

    def get_val(self):
        return plates_piles[len(plates_piles) - 1].plates[-1]

    def plates_size(self):
        return len(plates_piles[len(plates_piles) - 1].plates)

    def is_empty(self):
        return plates_piles[len(plates_piles) - 1].plates == []

    def is_max(self):
        return plates_piles[len(plates_piles) - 1].current_size >= self.max_size

    def creating_pile(self, plate):
        plates_piles.append(PileOfPlates(plate))


if __name__ == '__main__':
    plates_piles = []           #Список наших стопок
    pile = PileOfPlates()       #Первая стопка
    plates_piles.append(pile)   #Первая стопка в стеке стопок

    for i in range(10):
        pile.push_in(i)

    pile.push_in(10)
    print(plates_piles[0].plates, plates_piles[1].plates)
    pile.push_in(14)
    print(plates_piles[0].plates, plates_piles[1].plates)

    for i in range(25):
        plates_piles[1].push_in(i)

    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates)

    pile.push_in(36)
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates)

    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, plates_piles[3].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, y)
    y = pile.pop_out()
    print(plates_piles[0].plates, plates_piles[1].plates, plates_piles[2].plates, y)

    yep = pile.get_val()
    print(yep)

    print(pile.plates_size())

