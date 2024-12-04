'''
--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?


'''

def check_left_up(i, j, matrix):

    if i+1 < 140 and i-1 >= 0 and j+1 < 140 and j-1 >= 0:
        if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S':
            return True
        elif matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M':
            return True
        else:
            return False
    else:
        return False
    
def check_right_up(i, j, matrix):

    if i+1 < 140 and i-1 >= 0 and j+1 < 140 and j-1 >= 0:
        if matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S':
            return True
        elif matrix[i+1][j-1] == 'S' and matrix[i-1][j+1] == 'M':
            return True
        else:
            return False
    else:
        return False
    
def check_mas(i, j, matrix):

    if check_left_up(i, j, matrix) and check_right_up(i , j, matrix):
        return 1
    return 0

def count_x_mas(matrix):

    counter = 0

    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == 'A':
                counter += check_mas(i, j, matrix)

    return counter


input = open("inputpuzzle4.txt", "r")

matrix = []
xmas_counter = 0
for i, row in enumerate(input):
    matrix.append(list(row.strip()))
xmas_counter = count_x_mas(matrix)

print(xmas_counter)