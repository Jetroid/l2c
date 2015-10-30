#Use a for loop and the knowledge you know about modulo to create a FizzBuzz program.
#In the program, the following happens:
#	Counting up from 1 to 100:
#		If the number is divisible by 3, print Fizz.
#		If the number is divisible by 5, print Buzz.
#		If the number is divisible by 3 and 5, print FizzBuzz.
#		Otherwise, just print the number.

#Reminder: You can look back at the previous tasks to see how to print, use a for loop and the modulo operator.

#Write your code below: 

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)