# An algorithm to find the greatest divisor of 2 integers x and y
# Get the 2 integers x and y
#The smaller of the 2 integers is the greatest possible divisor for both of them so that will be initialized as the ceiling
# set a counter n = 1
# let the ceiling be the smaller of the 2 integers x and y
# set the divisor 'div' = 1
# while n < smaller of 2 integers 
    # iterate until a = x % n == 0. and b = y % n == 0 (a common divisor has been found)
    # if the statement above is true:
        # div *= n 
        # new ceiling will be smaller or a and b
        # n = 2 (if n == 1 it leads to an infinite loop because it'll always be true)
    # else:
        # n += 1
# if div == 1 then it means no common divisor could be found


# step 1: Get the 2 integers x and y
entered = False
while not entered:
    try:
        x = int(input("enter an integer for x: "))
        y = int(input("enter an integer for y: "))
        entered = True
    except:
        print("integers only")

# step 2: set a ceiling as a limit of where the counter n can get to 
if x < y:
    ceiling = x/2
else: 
    ceiling = y/2

# step 3: create the function to find the gcd
def gcd_function(x, y, ceiling, div):
    n = 2
    if (x / y == 1) or (y / x).is_integer():
        div = x
        return div
    elif (x / y).is_integer():
        div = y
        return div
    while n <= ceiling:
        p = x / n
        q = y / n
        a = x % n
        b = y % n 
        if a == 0 and b == 0:
            div *= n
            if p > q:
                ceiling = q/2
                return gcd_function(p, q, ceiling, div)
            else:
                ceiling = p/2
                return gcd_function(p, q, ceiling, div)
        else:
            n += 1
    if div == 1:
        print("No common divisor could be found")

    return div

greatest_divisor = gcd_function(x, y, ceiling, 1)
print(f"The greatest common divisor of {x} and {y} is: {greatest_divisor}")
