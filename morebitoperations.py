# Left and right shift

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right>>2
shift_left = shift_left<<2
print (bin (shift_right))
print (bin (shift_left))

# AND operator 
print (bin(0b1110 & 0b101))

#OR operator
print(bin(0b1110 | 0b101))

#XOR operator 
print(bin(0b1110^0b101))

#Mask concept
num = 0b1100
mask = 0b0100
desired = num & mask
if desired>0:
    print("Bit was on")

# More examples
def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired>0:
        return "on"
    else:
        return "off"
    print(check_bit4(0b1001))   

# To turn a bit in a number on , use '|'
a = 0b10111011
mask = 0b100
desired = a | mask
print(bin(desired))

# To flip bits use XOR

a = 0b110
mask = 0b111
desired = a^mask
print(desired)

a = 0b11101110
mask = 0b11111111
desired = a^mask
print(bin(desired))

#Left/Right shift to slip masks

a = 0b101
mask = (0b1<<9)
desired = a^mask
print(desired)

def flip_bit(number, n):
    bit_to_flip = 0b1<<(n-1)
    result = number^bit_to_flip
    return bin(result)
print(flip_bit(23,4))



