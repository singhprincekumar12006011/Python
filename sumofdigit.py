""" 
WAP to take two digit number as input from the user
and find the sum of its digit.

"""

x = (input("Enter the two digit number: \n"))
y = x[0]
z = x[1]

sum = int(y) + int(z)
print("Sum of the digit of two number is :" + str(sum))