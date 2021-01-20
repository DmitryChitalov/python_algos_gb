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

############################################################


class MyStack:

    def __init__(self, max_len):    # сразу инициализируемся
        self.__stacks = []          # создаем стек стеков, чтобы реализовать переполнения
        self.__stack = []           # сам стек
        self.__max_len = max_len    # максимальная величина стека

    def add_el(self, item):         # наполняем стек
        if len(self.__stacks) == 3 and len(self.__stacks[-1]) == self.__max_len:    # проверка на переполненность
            return print('Стек переполнен, создайте новый')

        if len(self.__stack) < self.__max_len:      # еще одна проверка на переполненность самого стека
            self.__stack.append(item)

        else:                                       # наши действия если стек переполнен но стек стеков еще нет
            self.__stacks.append(self.__stack[:])
            self.__stack.clear()
            self.__stack.append(item)

    def del_el(self):
        # проверяю варианты пустоты(наполненности) стека
        if len(self.__stack) != 0:
            self.__stack.pop()
            return

        if len(self.__stacks) != 0 and len(self.__stack) == 0:
            self.__stack = self.__stacks[-1][:]
            self.__stacks.pop()
            return
        else:
            return print('Stack is empty')

    def show_last(self):
        if len(self.__stack) != 0:  # Можно также и обработать ошибку если индекс вне деапазона
            return print(self.__stack[-1])

        if len(self.__stack) == 0 and len(self.__stacks) != 0:
            self.__stack = self.__stacks[-1][:]
            self.__stacks.pop()
            return print(self.__stack[-1])

        return print('Stack is empty')

    def is_empty(self):
        self.__stack = []
        return self.__stack

    def lenstack(self):
        return print(len(self.__stack))

    def showstack(self):
        return print(self.__stack)


a = MyStack(2)
a.show_last()
a.del_el()
a.show_last()
a.add_el(1)
a.show_last()
a.del_el()
a.show_last()
a.add_el(2)
a.is_empty()
a.show_last()
a.add_el(3)
a.add_el(4)
a.add_el(5)
a.add_el(6)
a.add_el(7)
a.show_last()
a.del_el()
a.show_last()
a.lenstack()
a.showstack()

