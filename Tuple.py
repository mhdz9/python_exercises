first_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
second_tuple = ()
temp_list = []

for i in first_tuple:
    if i % 2 == 0:
        temp_list.append(i)

second_tuple = (temp_list)

print second_tuple