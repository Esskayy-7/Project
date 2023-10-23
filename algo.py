# creating and algorithim for the addition of 2 digit numbers
# take in 2 numbers x and y
from logging import NullHandler


entered = False
while entered == False:
    try:
        x = int(input("Enter a 2 digit integer value for x: " ))
        y = int(input("Enter a 2 digit integer value for y: " ))
        entered = True
    except:
        print("integers only!")
# let x have values x1 and x2, and y y1 and y2
x = str(x)
y = str(y)
x1 = int(x[0])
x2 = int(x[1])
y1 = int(y[0])
y2 = int(y[1])
carry = s0 = 0

# starting from right to left add y2 to x2 annd let the sum be s2
s2 = x2 + y2

# if s2 > 10 let carry = 1 and s2 = s2 - 10
if s2 >= 10:
    carry = 1
    s2 -= 10 

# moving to the left, add x1 + y1 + carry = s1
s1 = x1 + y1 + carry

# if s1 > 10, carry = 1 and s1 = s1 - 10 and s0 = 1
if s1 >= 10:
    carry = 1
    s1 -= 10
    s0 = 1
# output x(x1x2) + y(y1y2) = sum(s0s1s2)
if s0 == 0:
    s0 = ""
print("sum: " + str(s0)+str(s1)+str(s2))

