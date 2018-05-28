import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!" )

count = 0
while count<3:
    num = random.randint(1,6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count+=1
    
else:
        print("You win!")

#Guessing Game

from random import randint

#generates a number from 1 through 10 inclusive

random_number = randint(1,10)

guesses_left = 3

#start your game!

while guesses_left>0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -=1
else:
    print("You lose.")

