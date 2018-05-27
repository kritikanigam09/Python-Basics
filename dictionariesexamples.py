menu = {}
menu['Chicken Alfredo'] = 14.50
print(menu['Chicken Alfredo'])
print("There are " + str(len(menu)) + "items on the menu")
print(menu)

beatles = ["john", "paul", "george", "ringo", "stuart"]
beatles.remove("stuart")
print(beatles)

my_dict = { "fish": ["c", "a", "r", "p"],
"cash": -4483,
"luck": "good"
}
print(my_dict["fish"][0])

inventory = { 'gold': 500,
'pouch': ['flint', 'twine', 'gemstone'],
'backpack': ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}
inventory['pouch'].sort()
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']= inventory['gold'] + 50
print(inventory)

#Counting number of times the word fizz appeared

def fizz_count(x):
    count=0
    for item in x:
         if item == "fizz":
             count = count+1
             return count

drinks=["fizz","cat","fizz"]
n=fizz_count(drinks)
print(n)

