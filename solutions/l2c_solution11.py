#Finish the if/elif/else statement below to evaluate if myInt is divisible by 4, else evaluate if it is divisible by 3.
#Try out myInt for several different values!

#Reminder: We can use the modulo operator to get the remainder. eg: 7 % 3 is equal to 1. (because 2*3 + 1 is equal to 7)

#Hint: If a modulo result is zero, then the left hand operator is wholly divisible by the right hand operator. 

#Example Solution: 
myInt = 12

if myInt % 4 == 0: 
  print("myInt was divisible by four.")
elif myInt % 3 == 0:
  print("myInt was divisible by three but not four.")
else:
  print("myInt was divisible by neither three nor four.")

