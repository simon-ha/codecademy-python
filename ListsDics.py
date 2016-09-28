# Codecademy lists and dictionaries summary exercise

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint'] # Added an item to the dictionary, pocket
inventory['backpack'].sort() # sorted the backpack
inventory['backpack'].remove('dagger') # removed dagger from backpack
inventory['gold'] = inventory['gold'] + 50 # added 50 to the gold inventory

print inventory