class Operation16:
    def __init__(self, num_first, num_second):
        self.num_first = num_first
        self.num_second = num_second

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(other.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(other.num_second), 16)))[2:]


first = list(input('Введите первое шеснадцатиричное число: '))
second = list(input('Введите второе шеснадцатиричное число: '))

res_sum = Operation16(first, second) + Operation16(first, second)
res_mul = Operation16(first, second) * Operation16(first, second)
print(f'Сумма чисел = {res_sum}\nПроизведение чисел = {res_mul}') 