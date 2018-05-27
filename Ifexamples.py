def using_control_once():
 if 2>1:
  return "Success #1"
  
  
def using_control_again():
 if 45<99:
  return "Success #2"
  
print(using_control_once())
print(using_control_again())



def greater_less_equal_5(answer):
 if answer>5:
  return 1
 elif answer<5:
  return -1
 else:
  return 0

print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# output: -1 , 0, 1

if 8>9:
  print("I don't get printed!")
else:
  print("I get printed!")


def clinic():
  print("You've just entered the clinic!")
  print("Do you take the door on the left or the right?")
  answer = input("Type left or right and hit 'Enter'.").lower()

  if answer == "left" or answer == "l":
    print("Verbal Abuse Room")
  elif answer == "right" or answer == "r":
    print("Argument Room")
  else:
    print("You didn't pick! Try again")

clinic()





