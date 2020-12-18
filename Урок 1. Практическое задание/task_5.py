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

class Plates:
    def __init__(self):
        self.plates_one = []
        self.plates_two = []
        self.plates_three = []
        self.plates_four = []
        self.plates_five = []
        self.stacks = [self.plates_one, self.plates_two, self.plates_three, self.plates_four, self.plates_five]
        self.stack = 10

    def is_empty(self):
        return self.plates_one == [], self.plates_two == [], self.plates_three == [],\
               self.plates_four == [], self.plates_five == []

    def push_in(self, plate):
        remains = 1
        for i in self.stacks:
            for numb in range(remains, plate+1):
                i.append(numb)
                if len(i) == self.stack:
                    break
            remains += len(i)

    def pop_out(self):
        for i in self.stacks[::-1]:
            if len(i) > 0:
                return i.pop()

    def stack_size(self):
        return len(self.plates_one),  len(self.plates_two), len(self.plates_three),\
               len(self.plates_four), len(self.plates_five)


p = Plates()
p.push_in(27)
print(p.stack_size())
print(p.is_empty())
print(p.pop_out())

print(p.plates_one)
print(p.plates_two)
print(p.plates_three)
print(p.plates_four)
print(p.plates_five)
