"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from statistics import median
from random import randint


def my_median(data):
    left = []
    right = []
    for i in data:
        for j in data:
            if j <= i:
                left.append(j)
            else:
                right.append(j)
        if len(right) < len(left) and len(right) + left.count(i) > len(data)/2:
            return i
        else:
            left.clear()
            right.clear()


a = [3, 3, 3, 5, 2, 3, 3]

print(my_median(a))
print(median(a))

# тестирование алгоритма:
for n in range(8200):
    a = [randint(0, 100) for i in range(101)]
    if my_median(a) != median(a):
        print(my_median(a))
        print(median(a))
        print(n, a)
