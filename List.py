my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
odd_numbers = []

for i in my_list:
    if i % 2 != 0:
        if i != my_list[0] and i != my_list[len(my_list)-1]:
            odd_numbers.append(i)

print odd_numbers