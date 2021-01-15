from count_size import count_size

x1 = float(input('Координата X первая '))
y1 = float(input('Координата Y первая '))
x2 = float(input('Координата X вторая '))
y2 = float(input('Координата Y вторая '))
if x2 == x1:
    print('Error')
    exit()
k = (y2 - y1) / (x2 - x1)
b = (y1 - k * x1)
if b == 0:
    print(f'Уравнение прямой y = {k:.2f}x')
elif b > 0:
    print(f'Уравнение прямой y = {k:.2f}x + {b:.2f}')
else:
    print(f'Уравнение прямой y = {k:.2f}x - {abs(b):.2f}')

-------------------------------------------------
sum_ = 0
var_lst = (x1, y1, x2, y2, k, b)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')
# Под переменные задействованно 144 байт памяти
# 6 * 24 =144 все верно
# Python 3.6.6
# OS - 64bit