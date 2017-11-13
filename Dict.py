my_dict = {'Aide': 'April 10th', 'Melissa': 'June 13th', 'Ernesto': 'April 7th', 'Mireya': 'June 12th', 'Antonio': 'August 25th'}

for name in my_dict:
    print name

choice = raw_input("Enter the name of the person you want to see the birthday of:\n")


if choice in my_dict:
    print my_dict.get(choice)