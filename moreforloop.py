#Example1

numbers = [7,9,12,54,99]
print("This list contains: ")
for num in numbers:
    print(num)
for num in numbers:
    print(num**2)

#Example2
dice = {'aa':'apple', 'bb':'berry','cc':'cherry'}
for key in dice:
    print(key,dice[key])

#Example3
choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are: ')
for index, item in enumerate(choices):
    print(index+1, item)

#Example 4

list_a = [3,9,17,15,19]
list_b = [2,4,8,10,30,40,50,60,70,80,90]

for a,b in zip(list_a, list_b):
    print(max(a,b))


#Example 5

fruits = ['bananas','apple','orange','tomato','pear','grape']
print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')
        break
    print('A', f)
else:
    print('A fine selection of fruits!')

    



