n = 1
while n<=10:
    print(n**2)
    n +=1


choice =input('Enjoying the course?(y/n)')
while choice != 'y' and choice != 'n':
    choice = input("Sorry, I didn't catch that. Enter again: ")

count = 0
while count<10:
    print(count)
    count +=1


counts = 0
while True:
    print(counts)
    counts +=1
    if counts>=10:
        break
