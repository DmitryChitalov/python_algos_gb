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


class Plates:
    """Стопки тарелок, по N штук в каждой"""
    def __init__(self, max_plates: int):
        self.plates = [[]]
        self.count = -1
        self.stack = 0
        self.max_plates = max_plates

    def push_in(self, new_plate):
        """Поместим тарелку в стопку"""
        # Если стопка еще не закончилась, то добавим тарелку в нее
        if self.count < self.max_plates - 1:
            self.count += 1
        # Если стопка закончилась, то начнем новую
        else:
            self.stack += 1
            self.plates.append([])
            self.count = 0

        self.plates[self.stack].append(new_plate)

    def pop_out(self):
        """Заберем тарелку из стопки"""
        # Нечего забирать
        if self.count == -1:
            return False
        # Если в стопке осталась одна тарелка, то ее отдаем и удаляем стопку
        if self.count == 0:
            res = self.plates[self.stack].pop()
            self.plates.pop(self.stack)
            if self.stack > 0:
                self.count = self.max_plates
                self.stack -= 1
            self.count -= 1

        # В стопке больше одной тарелки
        else:
            res = self.plates[self.stack].pop()
            self.count -= 1
        return res

    def get_val(self):
        """Возвращает последнюю тарелку"""
        if self.count >= 0:
            return self.plates[self.stack][self.count]
        return None

    def __str__(self):
        """Строковое представление стопок"""
        res = ""
        for j in self.plates:
            res = res + str(j) + "\n"
        return res

N = int(input("Введите количество тарелок: "))
S = int(input("Введите размер стопки: "))

my = Plates(S)

for i in range(N):
    T_P = 'p' + str(i)
    my.push_in(T_P)

print(my)

n1 = N // 2

print(f"Заберем {n1} тарелок")
for i in range(n1):
    my.pop_out()

print(my)
print(my.get_val())
