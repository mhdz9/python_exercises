zoo_animals = ['elephant', 'zebra', 'tiger', 'lion']

zoo_animals.append('cheetah')
print len(zoo_animals)
print zoo_animals

#zoo_animals.insert(zoo_animals.index('lion'),'giraffe')

for i in zoo_animals:
    if i == 'lion':
        zoo_animals[zoo_animals.index('lion')] = 'giraffe'

zoo_animals.remove('zebra')
print zoo_animals