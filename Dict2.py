my_tuple = raw_input("Enter a string of characters\n")
my_dict = {}

for x in my_tuple:
    my_dict[x] = my_tuple.count(x)

print my_dict