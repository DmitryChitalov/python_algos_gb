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

# Долго пыталась реализовать класс так, чтобы он внутри себя создавал новый экзкмпляр класса, но у меня не получилось,
# поэтому попробую сделать так, чтобы внутри экзкмпляра класса лежала несколько стеков

class StackClass:
    def __init__(self):
        self.elems = [[]] # Список списков, чтобы внутри экзкмпляра класса лежала несколько стеков
        self.max_len = 4 # Паксимальная длина (размер стека) пусть будет 4
        self.last = len(self.elems)-1  # Эта переменная для индекса последнего стека, потому что если мы будем
        # использовать просто,например, append как в примере,то добавим элемент вне посленего списка, то есть вне стека
        # Убрала ее, с ней почему-то не работает...

    def __str__(self):  # Чтобы я при проверки могла посмотреть на то, что получается
        return str(self.elems)

    def is_empty(self):
        return self.elems == [[]]

    def is_fool(self):  # Метод для проверки, полон ли последний стек
         if len(self.elems[len(self.elems)-1]) < self.max_len:
             return False
         else:
             return True

    def push_in(self, el):
        if self.is_fool() is True:  # Если стек полон,
            self.elems.append([])  # то сначала мы создаем новый стек.
        self.elems[len(self.elems) - 1].append(el)  # А уже потом добавляем значение на место для последнего элемента
        # Это же происходит и если стек не полон.

    def is_null(self):  # Метод для проверки, пуст ли последний стек
         if len(self.elems[len(self.elems)-1]) == 0:
             return True
         else:
             return False

    def pop_out(self):
        if self.is_null() is True: # Если последний стек пуст
            self.elems.pop() # То мы сначала его удаляем
        return self.elems[len(self.elems) - 1].pop() # А потом обрезаем последний элемент.
        # То же самое если последний стек не пуст

    def get_stak(self):
        return self.elems[len(self.elems) - 1]

    def get_el(self):
        return  self.elems[len(self.elems) - 1][-1]

    def stack_size(self):
        return len(self.elems)  # Это у нас, получается, количество стеков

    def count_els(self):
        result = 0
        for i in self.elems:
            result += len(i)
        return result



A = StackClass()

print(A.is_empty())

A.push_in(10)
A.push_in('code')
A.push_in(False)
A.push_in(5.5)
A.push_in(8)
A.push_in(9)

print(A.get_el())

print(A)
print(A.is_empty())

print(A.pop_out())
print(A)
print(A.pop_out())
print(A)


A.push_in(8)
A.push_in(9)
print(A)

print(A.get_stak())
print(A.get_el())

print(A.pop_out())
print(A)

print(A.stack_size())
print(A.count_els())