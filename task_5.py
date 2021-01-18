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

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""

class PlatesStacks():

    def __init__(self):
        self.plates_in_stack = []
        self.stacks_of_plates = []

    def plate_add(self):
        if len(self.plates_in_stack) < 5:
            self.plates_in_stack.append('plate')
        else:
            self.stacks_of_plates.append(self.plates_in_stack)
            self.plates_in_stack = []
            self.plates_in_stack.append('plate')

    def plate_take_away(self):
        if self.plates_in_stack:
            self.plates_in_stack.pop(-1)
        elif not self.stacks_of_plates:
            print('тарелок нет')
        else:
            self.plates_in_stack = self.stacks_of_plates[-1]
            self.stacks_of_plates.pop(-1)
            self.plates_in_stack.pop(-1)

    def show_parametres(self):
        print(f'тарелки в стеке {self.plates_in_stack}')
        print(f'заполненные стеки {self.stacks_of_plates}')


plt = PlatesStacks()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_add()
plt.plate_take_away()
plt.plate_take_away()
plt.plate_take_away()
plt.plate_take_away()
plt.show_parametres()