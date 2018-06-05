evens_to_50 = [i for i in range(51) if i%2 == 0]
print(evens_to_50)

new_list = [x for x in range(1,6)]
print(new_list)

doubles = [x*2 for x in range (1,6)]
print(doubles)

doubles_by_3 = [x*2 for x in range (1,12) if (x*2)%3==0]
print(doubles_by_3)

even_squares = [x*x for x in range(1,12) if x%2==0]
print(even_squares)

c = ['c' for x in range (5) if x<3]
print(c) 

cubes_by_four = [x*x*x for x in range(1,11) if x*x*x%4==0]
print(cubes_by_four)

#List Slicing syntax

l = [i**2 for i in range(1,11)]
print(l[2:9:2])

#Omitting Indices

to_five = ['A', 'B', 'C', 'D', 'E']
print(to_five[3:])
print(to_five[:2])
print(to_five[::2])

my_list = range(1,11)
print(my_list[::2])

#Reversing a list

letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])

to_one_hundered = range(101)
backwards_by_tens = to_one_hundered[::-10]
print(backwards_by_tens)

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]
print(odds)
print(middle_third)

threes_and_fives = [x for x in range (1,16) if x%3 == 0 or x%5 == 0]
print(threes_and_fives)

# Anonymous Functions: LAMBDA

my_lisst = range(16)
print(filter(lambda x:x%3==0, my_lisst))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x:x == "Python", languages))

squares = [x**2 for x in range (1,11)]
print(filter(lambda x:x>=30 and x<=70, squares))




