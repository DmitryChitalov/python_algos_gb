my_list = []
n = 0
my_list.append([])
for i in range(1, 21):
    if len(my_list[n]) // 5 == 0:
        my_list[n].append(i)
    else:
        my_list.append([])
        n += 1
        my_list[n].append(i)

print(my_list)


# my_list[0].append(2)
# my_list[0].append(3)
# my_list[0].append(4)
# my_list[0].append(5)
# my_list.append([])
# my_list[1].append(2)




