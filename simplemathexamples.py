#Summing up the digits of a number

def digit_sum(x):
    total = 0
    while x>0:
        total +=x%10
        x= x//10
        print(x)
        return total


#Calculating the factorial

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x -= 1
        return total


#Is_Prime?

def is_prime(x):
    if x<2:
        return False
    else:
        for n in range(2, x-1):
            if x%n == 0:
                return False
    return True



#Reversing a word

def reverse(text):
    word= " "
    l = len(text) - 1
    while l>=0:
        word = word + text[l]
        l -= 1
        return word


#Anti Vowel

def anti_vowel(text):
    t= " "
    for c in text:
        for i in "aeiou AEIOU":
            if c == i:
                c = " "
        else:
            c = c
            t = t+c
            return t




