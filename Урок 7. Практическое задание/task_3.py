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


import random
import array


m = int(input("Введите m, где число эллементов массива 2m + 1 \n"))

input_list = [random.randint(0, 100) for i in range(2*m+1)]
print(input_list)

# input_list2 = input_list                      # Проверка верности медианы
# print(input_list2)
#
# print()
# print(sorted(input_list2))

while True:
    min_num = input_list.index(min(input_list))
    input_list.pop(min_num)

    max_num = input_list.index(max(input_list))
    input_list.pop(max_num)

    if len(input_list) == 1:
        break

print()
print(input_list)

