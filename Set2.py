zoo_animals = {
    'Unicorn': 'Cotton Candy House',
    'Sloth': 'Rainforest Exhibit',
    'Bengal Tiger': 'Jungle House',
    'Atlantic Puffin': 'Arctic Exhibit',
    'Rockhopper Penguin': 'Arctic Exhibit'
}

if 'Sloth' and 'Bengal Tiger' in zoo_animals:
    del zoo_animals['Sloth']
    del zoo_animals['Bengal Tiger']

print zoo_animals