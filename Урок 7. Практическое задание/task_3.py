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

lll = [3, 4, 3, 3, 5, 3, 3]

def gnome(sort_list):

    i = 1
    while i < len(sort_list):
        if not i or sort_list[i-1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i-1] = sort_list[i-1], sort_list[i]
            i -= 1
    return sort_list

#print(lll)
#gnome(lll)
#print(lll)




def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i>j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i<j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()

lll = [3, 4, 3, 3, 5, 3, 3]

print(without_sort(lll))

