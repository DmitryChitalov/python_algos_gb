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


class Stack:
    def __init__(self):
        self.stack_list = [[]]

    def addelem(self, n):
        self.n = n
        if len(self.stack_list[-1]) < 5:
            self.stack_list[-1].append(self.n)
        else:
            self.stack_list.append([self.n])

    def remelem(self):
        if len(self.stack_list[-1]) == 1:
            self.stack_list.pop(-1)
        else:
            self.stack_list[-1].pop(-1)

    def countStack(self):
        print(f' You have {len(self.stack_list)} stacks.')

    def countStackElem(self, i):
        if i > 1 or i <= len(self.stack_list):
            print(f' Stack number {i} has {len(self.stack_list[i-1])} elements.')
        else:
            print('Stack number does not exist.')


a = Stack()
a.addelem('1231')
a.addelem('1231')
a.addelem('1231')
a.addelem('1231')
a.addelem('1231')
a.addelem('1231')
a.addelem('1231')
a.addelem('12s31')
a.remelem()
a.remelem()
a.remelem()
print(a.stack_list)
a.countStackElem(1)
