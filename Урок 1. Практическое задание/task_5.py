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


class PStack:
    plates = []
    plates_stack_sizes = []
    current_stack = 0

    def __init__(self, one_stack_size):
        self.one_stack_size = one_stack_size
        self.plates = [[]]

    def __str__(self):
        return str(self.plates)

    def add_one_plate(self, name):
        if len(self.plates[self.current_stack]) < self.one_stack_size:
            self.plates[self.current_stack].append(name)
        else:
            self.current_stack += 1
            self.plates.append([])
            self.plates[self.current_stack].append(name)


stk = PStack(2)

print(stk)

stk.add_one_plate('za mamu')
print(stk)
stk.add_one_plate('za papu')
print(stk)
stk.add_one_plate('za diadu olega')
print(stk)
stk.add_one_plate('za togo parnya')
print(stk)
stk.add_one_plate('za VDV')

print(stk)
