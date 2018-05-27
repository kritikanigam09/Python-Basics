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


  def grade_converter(grade):
    if grade>=90:
      return "A"
    elif grade>=80 and grade<=89:
      return "B"
    elif grade>=70 and grade<=79:
      return "C"
    elif grade>=65 and grade<=69:
      return"D"
    else:
      return "F"

    print (grade_converter(92))
    print (grade_converter(70))
    print (grade_converter(61))


