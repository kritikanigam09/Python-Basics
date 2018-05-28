#Example1
print("Counting...")
for i in range (20):
    print(i)

#Example2

hobbies = []
for num in range(3):
    hobby = input("Tell me one of your favorite hobbies: ")
    hobbies.append(hobby)
    print(hobbies)

#Example3

thing = "spam!"
for c in thing:
    print(c)

word = "eggs!"
for x in word:
    print(x)

#Example4

phrase = "A bird in the hand..."

for char in phrase:
    if char=="A" or char=="a":
        print("x")
    else:
        print(char)