import random

dl = 10
rd_ls = [random.randint(30, 89) for i in range(dl)]

def bubble_sort(numb_arr):
    a = numb_arr

    len_arr = len(a)
    for i in range(len_arr - 1):
        counter = 0
        for j in range(len_arr - 1 - i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
        if counter == 0:
            break
    return a


print(f'Исходный массив:\n{rd_ls}\n')
print(f'Сортированный массив:\n{bubble_sort(rd_ls)}')