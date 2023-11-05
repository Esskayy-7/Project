# Get a text ro be compared with, call it search_value
# search_value will be compared against an existing search
# the length m of search_value must be <= that of text(n): len(search_value) = m; len(text) = n: m <= n
# the found value will initially be false : found -> None
# the loop will iterate until either k < (n - m) + 1, where k is a counter
# The program starts by setting the first point of comparison to text[0], and compares it to search_value[0], if a match is found, it shifts (by increasing i), to the next position, and if false, head is moved to i + 1, where head is where the search starts from  
# while looping, the algorithm stores the location where a match occurs to a location list, and then outputs it to the user

text = input("text to search through: ")
search_value = input("text to be matched with: ")

# the length m of search_value must be <= that of text(n): len(search_value) = m; len(text) = n: m <= n
n = len(text)
m = len(search_value)
locations = []
found = None

k = 0
# the loop will iterate until either k < (n - m) + 1, where k is a counter
while k < (n - m) + 1:
    i = k
    j = 0
    while found != False and j < m:
# The program starts by setting the first point of comparison to text[0], and compares it to search_value[0], if a match is found, it shifts (by increasing i), to the next position, and if false, head is moved to i + 1, where head is where the search starts from
        comp_point = text[i]
        head = search_value[j]
        if comp_point == head:
            i += 1
        else: 
            found = False
        j += 1
    if found != False: 
        locations.append(k)
    found = None
    k = i

print(locations)