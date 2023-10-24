# create an algorithm for the addition of n-digit numbers where n is an integer including decimals
# Logic behind the algorithm: 
# Take in two numbers x and y
# The length of x will be 'a' : len(x)-->a and 'b' for y: len(y)-->b
# The algorithm adds every digit in the number to its corresponding pair in the other number (x1 + y1)
# If a != b, the larger of the values(a or b) - the smaller of the values (b or a) respectively is assigned to n
# n zeros will be inserted to the front of the smaller integers so that a == b
# The algorithm then carries on like a regular addition algorithm

# Step 1: Take in 2 numbers
entered = False
while entered == False:
    try:
        x = int(input("Enter an integer value for x: " ))
        y = int(input("Enter an integer value for y: " ))
        entered = True
    except:
        print("integers only!")
x = str(x)
y = str(y)

# Step 2: Let the length of x be 'a' : len(x)-->a and 'b' for y: len(y)-->b
a = len(x)
b = len(y)

# Step 3: assign a values for x, and b values for b
list_x = [i for i in x]
list_y = [i for i in y]

# Step 4: If a != b, the larger of the values(a or b) - the smaller of the values (b or a) respectively is assigned to n
zero = []
if a < b:
    n = b - a
    i = 0
    while i < n:
        zero.append(str(0))
        i += 1
    zero.extend(list_x)
    list_x = zero.copy()
elif b < a:
    n = a - b
    i = 0
    while i < n:
        zero.append(str(0))
        i += 1
    zero.extend(list_y)
    list_y = zero.copy()

# print(list_x, list_y)

# Step 6: The algorithm adds every digit in the number to its corresponding pair in the other number (x1 + y1)
solution = []
carry = i = 0
length = len(list_x) - 1
while i < len(list_x): 
    val_x = int(list_x[length])
    val_y = int(list_y[length])
    sum = val_x + val_y + carry
    carry = 0
    if sum >= 10:
        carry = 1
        sum = sum - 10
    solution.append(str(sum))
    length -= 1
    i += 1
    if carry == 1 and i == len(list_x):
        solution.extend(["1"])

length = len(solution) - 1
k = 0
answer = []
while k < len(solution):
    answer.append(solution[length])
    k += 1
    length -= 1

answer = [str(j) for j in answer]
solution = ("").join(answer)

print(solution)