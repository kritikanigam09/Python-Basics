from random import randint

count = 0
while True:
    x = randint(1,9)
    guess = int(input("Guess a number between 1 and 9: \n"))

    if guess==x:
        print("You guessed the exact number!")
    elif guess>x:
        print("You guessed too high!")
    elif guess<x:
        print("You guessed too low!")
    else:
        print("Number not in range")
    
    print(x)
    count += 1

    check = input("Type exit to leave the game: \n").lower()

    if check != 'exit':
        continue
    
    else:
        break
print(count)



