"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from mymodules import measurer
from pympler import asizeof


class SimpleVsGen:
    def __init__(self, number):
        self.number = number

    @measurer
    def gen_iter(self):
        g = (i * 2 for i in range(self.number) if i % 3 == 0 or i % 5 == 0)
        return print(f'Размер экземпляра = {asizeof.asizeof(g)}')

    @measurer
    def simple_iter(self):
        l = [i * 2 for i in range(self.number) if i % 3 == 0 or i % 5 == 0]
        return print(f'Размер экземпляра = {asizeof.asizeof(l)}')


a = SimpleVsGen(10000)

print(f'--- Генератор ---')
a.gen_iter()
print()

print(f'--- Генераторное выражение ---')
a.simple_iter()

"""
В сравнениее представлено два метода через ГЕНЕРАТОР и генераторное ВЫРАЖЕНИЕ.
--- Генератор ---
Размер экземпляра = 448
Выполнение заняло 0.10424 сек и 0.02344 Miб

--- Генераторное выражение ---
Размер экземпляра = 187544
Выполнение заняло 0.12486 сек и 0.4141 Miб

В итоге видим, что в данном случае ГЕНЕРАТОР потребляет гораздо меньший объем памяти, и его 
использование более чем оправдано!
"""

