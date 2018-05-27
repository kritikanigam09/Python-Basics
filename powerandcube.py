def power(base, exponent):
    result = base**exponent
    print("%d to the power of %d is %d."%(base,exponent,result))

power(37,4)

def cube(number):
 return number*number*number
print (cube(2))

def by_three(number):
 if number%3==0:
    return cube(number)
 else:
    return False
print(by_three(3))

