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
from random import randint

from statistics import median

# my_list = [4, 3, 3, 3, 5, 3, 3]
m = int(input("Введите число m: "))
my_list = [randint(0, 100) for el in range(2 * m + 1)]


def my_median(list_arg):
    for idx1, el1 in enumerate(list_arg):
        left = 0
        right = 0
        for idx2, el2 in enumerate(list_arg):
            if el2 < el1:
                left += 1
            if el2 > el1:
                right += 1
        if left < len(list_arg) / 2 and right < len(list_arg) / 2:
            return el1


print(f"my_median(): {my_median(my_list)}")
print(f"median(): {median(my_list)}")


'''
Решение без сортировки и без доволнительных списков.
Один из элементов берется как опорный, а по остальным идут два счетчика:
больше опорного, меньше опорного.
Если оба счетчика оказываются меньше половины длины списка, значит опорный 
элемент является медианой.
'''