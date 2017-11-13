word = raw_input("Enter a string of characters\n")
other_dict = {}

for i in word:
    other_dict[i] = word.count(i)

print other_dict