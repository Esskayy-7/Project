import random

sudoku_table = [[ '' for y in range(9)] for x in range(9)]
print(sudoku_table)

i = 0
j = 0
# tracking = []
assigned_values = []
for i in sudoku_table:
    while j < 4:
        k = random.choice([x for x in range(9)])
        rand_val = random.choice([x for x in range(1, 10)])
        assigned_values.append((k, sudoku_table[i][k]))
        for m in assigned_values:
            col_ind, cell_val = m
            if k == col_ind and cell_val != rand_val:
                sudoku_table[i][k] = rand_val
          
        # tracking.append((i, k))
        
        j += 1

print(assigned_values)


