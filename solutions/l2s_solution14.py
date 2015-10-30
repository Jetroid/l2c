#Write a program that will print out the contents of a multiplication table from 1x1 to 12x12.
# ie. The multiplication table from 1x1 to 3x3 is as follows:
#	1	2	3
#	2	4	6
#	3	6	9

#Hint: You'll probably want to use two for loops for each number.

#Reminder: To print something without putting a newline on the end, you can use print(..., end="\t").
#			You might also want to use tabs so double/triple digit numbers are formatted in a nice table.

#Bonus: See if you can figure out how to print the column headers.

#Write your code below: 

upperLimit = 13

for i in range(1, upperLimit):
    for j in range(1, upperLimit):
        print(str(i * j), end="\t")
    print()