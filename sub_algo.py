# Subtraction of 2 multiple digit numbers
# Take the input of the 2 numbers from the user a and b
# determine which is bigger
# create a list for each number where the digits will inputted as string list items
# subtract from the right to the left
# if a digit from the first list(a or b) is smaller than the value to be subtracted, then set borrow to 10, add it to the first digit, subtact it and set it equal to the difference: borrow = 10 -> (difference = (digit1 + borrow) - digit2)
# if digit2 is null, set digit2 = 0
# continue until len(subtractor) is reached, then output the results


entered  = False

# Take the input of the 2 numbers from the user a and b
while not entered:  
    try:
        a = int(input("Enter a value for a: "))
        b = int(input("Enter a value for b: "))
        entered = True 
    except:
        print("Numerical values only")

if a < b:
    subtractor = str(b)
    subtracted = str(a)
else: 
    subtractor = str(a)
    subtracted = str(b)

# subtract from the right to the left
    i = 1
    difference = None
    diff_list = []
    borrow = 0
    while i <= len(subtractor):
        try:
            digit1 = int(subtractor[-i])
            digit2 = int(subtracted[-i])
        except:
            digit2 = 0
# If borrow is not None, then reduce digit 1 by 1
        if borrow != 0:
            digit1 -= 1
        borrow = 0

# if a digit from the first string(subtractor) is smaller than the value to be subtracted, then set borrow to 10, add it to the first digit, subtact it and set it equal to the difference: borrow = 10 -> (difference = (digit1 + borrow) - digit2)
        if digit1 < digit2:
            borrow = 10
        difference = (digit1 + borrow) - digit2
        diff_list.append(str(difference))
        i += 1

k = 1
answer = []
while k < len(diff_list) + 1:
    answer.append(diff_list[-k])
    k += 1

answer = [str(j) for j in answer]
solution = ("").join(answer)
print(solution)
