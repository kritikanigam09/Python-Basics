def biggest_number(*args):
    print (max(args))
    return max(args)

def smallest_number(*args):
    print (min(args))
    return min(args)
def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)

print(biggest_number(-10,-5,5,10))
print(smallest_number(-10,-5,5,10))
print(distance_from_zero(-10))
print(type(80))
print(type(2.7))
print(type('ring'))
