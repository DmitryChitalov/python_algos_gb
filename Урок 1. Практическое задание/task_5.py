"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""


class StackClass:

    elems: []
    _stack_limit = 4

    def __init__(self, stack_lim=4):
        self.elems = []
        _stack_limit = stack_lim

    def __str__(self):
        print(f"Класс лимитированного {self._stack_limit} стека. Размер можно изменить.")

    def set_limit(self, size):
        self._stack_limit = size

    def get_limit(self):
        return self._stack_limit

    def is_empty(self):
        return self.elems == []

    def get_stack_size(self):
        return len(self.elems)

    def push_in(self, el):
        self.elems.append(el)
        return self.elems

    def pop_out(self):
        return self.elems.pop()

    # lifo: вытаскиваем последний элемент
    def get_value(self):
        return self.elems[len(self.elems) - 1]

    def is_full(self):
        # print(len(self.elems), self._stack_limit)
        return len(self.elems) == self._stack_limit


limited_stack_list = []

limit_stack = StackClass()

lim = 0
print(f"Размер стопки сейчас: {limit_stack.get_limit()}.")

try:
    lim = int(input("Если этот размер Вас устраивает жмите пробел, если нет - введите нужный размер: "))
except ValueError:
    print("Оставляем прежний размер")

# Для начала заполним нашу структуру.
print("Давайте заполним нашу структуру. Когда надоест - нажимайте Enter! ")
while True:
    if lim > 0:
        limit_stack.set_limit(lim)
    stack_el = input("Новый элемент стека: ")
    if stack_el == "":
        if limit_stack.get_stack_size() > 0:
            limited_stack_list.append(limit_stack)
        break  # выход из цикла заполнения.

    limit_stack.push_in(stack_el)
    if limit_stack.is_full():
        print("!")
        limited_stack_list.append(limit_stack)
        limit_stack = StackClass()

for idx, limit_stack in enumerate(limited_stack_list):
    print(f"Содержимое стопки {idx + 1}: ")
    i = limit_stack.get_stack_size()
    while i > 0:
        print(limit_stack.pop_out())
        i -= 1


